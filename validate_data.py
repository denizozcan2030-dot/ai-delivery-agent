import csv, json, os

def read_csv(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

jira = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/jira_issues.csv')
projects = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/projects.csv')
financials = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/financials.csv')
project_people = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/project_people.csv')
kpi = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/kpi.csv')

# 4. JIRA dependency validation
all_issue_keys = set(r['Issue_Key'] for r in jira)
linked_keys = set(r['Linked_Issue_Key'] for r in jira if r['Linked_Issue_Key'])
print(f'Total unique Issue_Keys: {len(all_issue_keys)}')
print(f'Unique Linked_Issue_Keys referenced: {len(linked_keys)}')
orphan_refs = linked_keys - all_issue_keys
print(f'Orphan references (referenced but dont exist): {sorted(orphan_refs)}')

# Cross-project dependencies
print('\n--- Cross-project dependencies ---')
cross_deps = []
for row in jira:
    if row['Linked_Issue_Key'] and row['Linked_Issue_Key'] in all_issue_keys:
        src_proj = row['Project_ID']
        tgt_proj = None
        for r in jira:
            if r['Issue_Key'] == row['Linked_Issue_Key']:
                tgt_proj = r['Project_ID']
                break
        if tgt_proj and src_proj != tgt_proj:
            cross_deps.append((src_proj, row['Issue_Key'], row['Link_Type'], tgt_proj, row['Linked_Issue_Key']))

cross_deps = list(set(cross_deps))
for src, skey, ltype, tgt, tkey in cross_deps:
    print(f'  {src} {skey} --({ltype})--> {tgt} {tkey}')

# 5. Data completeness per project
project_ids = set(r['Project_ID'] for r in projects)
project_names = {r['Project_ID']: r['Project_Name'] for r in projects}
print('\n=== DATA COMPLETENESS PER PROJECT ===')
for pid in sorted(project_ids):
    pname = project_names[pid]
    has_fin = any(r['Project_ID'] == pid for r in financials)
    has_kpi = any(r['Project_ID'] == pid for r in kpi)
    has_res = any(r['Project_ID'] == pid for r in project_people)
    conf_path = f'C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/confluence_docs/{pid}_Confluence_Project_Overview.docx'
    has_conf = os.path.exists(conf_path)
    print(f'  {pid} ({pname}): Finance={has_fin}, KPI={has_kpi}, Resource={has_res}, Confluence={has_conf}')

# 6. Duplicate checks
print('\n=== DUPLICATE CHECKS ===')
for name, data in [('projects', projects), ('financials', financials), ('people', people), ('kpi', kpi), ('project_people', project_people)]:
    pass  # will add people import

# Jira duplicate issue keys
jira_keys = [r['Issue_Key'] for r in jira]
jira_key_counts = {}
for k in jira_keys:
    jira_key_counts[k] = jira_key_counts.get(k, 0) + 1
jira_dupes = [k for k, v in jira_key_counts.items() if v > 1]
if jira_dupes:
    print(f'  jira: {len(jira_dupes)} duplicate Issue_Keys: {jira_dupes}')
else:
    print(f'  jira: No duplicate Issue_Keys')

# project_people duplicate (Project_ID, Employee_ID)
pp_pairs = [(r['Project_ID'], r['Employee_ID']) for r in project_people]
pp_pair_counts = {}
for p in pp_pairs:
    pp_pair_counts[p] = pp_pair_counts.get(p, 0) + 1
pp_dupes = [p for p, v in pp_pair_counts.items() if v > 1]
if pp_dupes:
    print(f'  project_people: {len(pp_dupes)} duplicate Project_ID+Employee_ID pairs: {pp_dupes}')
else:
    print(f'  project_people: No duplicate Project_ID+Employee_ID pairs')

# KPI duplicate (Project_ID, KPI_ID)
kpi_pairs = [(r['Project_ID'], r['KPI_ID']) for r in kpi]
kpi_pair_counts = {}
for p in kpi_pairs:
    kpi_pair_counts[p] = kpi_pair_counts.get(p, 0) + 1
kpi_dupes = [p for p, v in kpi_pair_counts.items() if v > 1]
if kpi_dupes:
    print(f'  kpi: {len(kpi_dupes)} duplicate Project_ID+KPI_ID pairs: {kpi_dupes}')
else:
    print(f'  kpi: No duplicate Project_ID+KPI_ID pairs')

# Financials duplicate Project_ID
fin_ids = [r['Project_ID'] for r in financials]
fin_id_counts = {}
for pid in fin_ids:
    fin_id_counts[pid] = fin_id_counts.get(pid, 0) + 1
fin_dupes = [pid for pid, v in fin_id_counts.items() if v > 1]
if fin_dupes:
    print(f'  financials: {len(fin_dupes)} duplicate Project_ID: {fin_dupes}')
else:
    print(f'  financials: No duplicate Project_ID')

# Employee allocation sums
print('\n--- Employee Allocation Sums ---')
alloc_sums = {}
for r in project_people:
    eid = r['Employee_ID']
    alloc = int(r['Project_Allocation_Percent'])
    alloc_sums[eid] = alloc_sums.get(eid, 0) + alloc
for eid, total in sorted(alloc_sums.items()):
    if total > 100:
        ename = None
        for r in project_people:
            if r['Employee_ID'] == eid:
                ename = r['Employee_Name']
                break
        print(f'  OVERALLOCATED: {eid} ({ename}) = {total}%')