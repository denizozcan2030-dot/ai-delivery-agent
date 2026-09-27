import csv, json, os

def read_csv(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

jira = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/jira_issues.csv')
projects = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/projects.csv')
financials = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/financials.csv')
people = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/people.csv')
project_people = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/project_people.csv')
kpi = read_csv('C:/Users/Asus/OneDrive/Desktop/ai-delivery-agent/kpi.csv')

# 6. Duplicate checks
print('\n=== DUPLICATE CHECKS ===')
for name, data in [('projects', projects), ('financials', financials), ('people', people), ('kpi', kpi), ('project_people', project_people)]:
    seen = set()
    dupes = 0
    for row in data:
        key = tuple(sorted(row.items()))
        if key in seen:
            dupes += 1
        seen.add(key)
    if dupes > 0:
        print(f'  {name}: {dupes} duplicate rows')
    else:
        print(f'  {name}: No duplicate rows')

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