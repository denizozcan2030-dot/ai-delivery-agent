import csv
import os


# Base directory: folder where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_csv(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


# Load project data
jira = read_csv("jira_issues.csv")
projects = read_csv("projects.csv")
financials = read_csv("financials.csv")
people = read_csv("people.csv")
project_people = read_csv("project_people.csv")
kpi = read_csv("kpi.csv")


# 4. JIRA dependency validation
all_issue_keys = set(r["Issue_Key"] for r in jira)
linked_keys = set(
    r["Linked_Issue_Key"]
    for r in jira
    if r["Linked_Issue_Key"]
)

print(f"Total unique Issue_Keys: {len(all_issue_keys)}")
print(f"Unique Linked_Issue_Keys referenced: {len(linked_keys)}")

orphan_refs = linked_keys - all_issue_keys
print(
    f"Orphan references (referenced but dont exist): "
    f"{sorted(orphan_refs)}"
)


# Cross-project dependencies
print("\n--- Cross-project dependencies ---")

cross_deps = []

for row in jira:
    if (
        row["Linked_Issue_Key"]
        and row["Linked_Issue_Key"] in all_issue_keys
    ):
        src_proj = row["Project_ID"]
        tgt_proj = None

        for r in jira:
            if r["Issue_Key"] == row["Linked_Issue_Key"]:
                tgt_proj = r["Project_ID"]
                break

        if tgt_proj and src_proj != tgt_proj:
            cross_deps.append(
                (
                    src_proj,
                    row["Issue_Key"],
                    row["Link_Type"],
                    tgt_proj,
                    row["Linked_Issue_Key"],
                )
            )

cross_deps = list(set(cross_deps))

for src, skey, ltype, tgt, tkey in cross_deps:
    print(
        f"  {src} {skey} --({ltype})--> "
        f"{tgt} {tkey}"
    )


# 5. Data completeness per project
project_ids = set(r["Project_ID"] for r in projects)

project_names = {
    r["Project_ID"]: r["Project_Name"]
    for r in projects
}

print("\n=== DATA COMPLETENESS PER PROJECT ===")

for pid in sorted(project_ids):
    pname = project_names[pid]

    has_fin = any(
        r["Project_ID"] == pid
        for r in financials
    )

    has_kpi = any(
        r["Project_ID"] == pid
        for r in kpi
    )

    has_res = any(
        r["Project_ID"] == pid
        for r in project_people
    )

    conf_path = os.path.join(
        BASE_DIR,
        "confluence_docs",
        f"{pid}_Confluence_Project_Overview.docx",
    )

    has_conf = os.path.exists(conf_path)

    print(
        f"  {pid} ({pname}): "
        f"Finance={has_fin}, "
        f"KPI={has_kpi}, "
        f"Resource={has_res}, "
        f"Confluence={has_conf}"
    )


# 6. Duplicate checks
print("\n=== DUPLICATE CHECKS ===")


# Jira duplicate issue keys
jira_keys = [
    r["Issue_Key"]
    for r in jira
]

jira_key_counts = {}

for key in jira_keys:
    jira_key_counts[key] = (
        jira_key_counts.get(key, 0) + 1
    )

jira_dupes = [
    key
    for key, count in jira_key_counts.items()
    if count > 1
]

if jira_dupes:
    print(
        f"  jira: {len(jira_dupes)} "
        f"duplicate Issue_Keys: {jira_dupes}"
    )
else:
    print("  jira: No duplicate Issue_Keys")


# project_people duplicate (Project_ID, Employee_ID)
pp_pairs = [
    (r["Project_ID"], r["Employee_ID"])
    for r in project_people
]

pp_pair_counts = {}

for pair in pp_pairs:
    pp_pair_counts[pair] = (
        pp_pair_counts.get(pair, 0) + 1
    )

pp_dupes = [
    pair
    for pair, count in pp_pair_counts.items()
    if count > 1
]

if pp_dupes:
    print(
        f"  project_people: {len(pp_dupes)} "
        f"duplicate Project_ID+Employee_ID pairs: "
        f"{pp_dupes}"
    )
else:
    print(
        "  project_people: "
        "No duplicate Project_ID+Employee_ID pairs"
    )


# KPI duplicate (Project_ID, KPI_ID)
kpi_pairs = [
    (r["Project_ID"], r["KPI_ID"])
    for r in kpi
]

kpi_pair_counts = {}

for pair in kpi_pairs:
    kpi_pair_counts[pair] = (
        kpi_pair_counts.get(pair, 0) + 1
    )

kpi_dupes = [
    pair
    for pair, count in kpi_pair_counts.items()
    if count > 1
]

if kpi_dupes:
    print(
        f"  kpi: {len(kpi_dupes)} "
        f"duplicate Project_ID+KPI_ID pairs: "
        f"{kpi_dupes}"
    )
else:
    print(
        "  kpi: "
        "No duplicate Project_ID+KPI_ID pairs"
    )


# Financials duplicate Project_ID
fin_ids = [
    r["Project_ID"]
    for r in financials
]

fin_id_counts = {}

for pid in fin_ids:
    fin_id_counts[pid] = (
        fin_id_counts.get(pid, 0) + 1
    )

fin_dupes = [
    pid
    for pid, count in fin_id_counts.items()
    if count > 1
]

if fin_dupes:
    print(
        f"  financials: {len(fin_dupes)} "
        f"duplicate Project_ID: {fin_dupes}"
    )
else:
    print(
        "  financials: "
        "No duplicate Project_ID"
    )


# Employee allocation sums
print("\n--- Employee Allocation Sums ---")

alloc_sums = {}

for r in project_people:
    eid = r["Employee_ID"]
    alloc = int(r["Project_Allocation_Percent"])

    alloc_sums[eid] = (
        alloc_sums.get(eid, 0) + alloc
    )

for eid, total in sorted(alloc_sums.items()):
    if total > 100:
        ename = None

        for r in project_people:
            if r["Employee_ID"] == eid:
                ename = r["Employee_Name"]
                break

        print(
            f"  OVERALLOCATED: "
            f"{eid} ({ename}) = {total}%"
        )
