# AI Delivery Agent

**AI-Assisted Portfolio Risk Analysis & Decision Support**

[English](#english) | [Türkçe](#türkçe)

---

<a id="english"></a>

# English

## Overview

AI Delivery Agent is a prototype designed to support portfolio-level project delivery analysis and management decision-making.

The objective is not simply to identify which projects are at risk. The Agent is designed to help answer questions such as:

- Why is a project at risk?
- What is the possible root cause?
- Which other projects may be affected by a dependency?
- Is the issue actually related to resource capacity?
- If another resource is available, could reallocation create risk in another project?
- What do budget, ROI, and KPI data indicate?
- Where should management attention be focused based on the available data?

The Agent combines structured project data with information extracted from project documentation to create a portfolio-level management view.

---

## Prototype Data Sources

The prototype simulates an enterprise project portfolio using synthetic data.

The analysis uses:

- **Jira-style data** — issues, blockers, dependencies, assignees, effort, milestones
- **Confluence-style project documentation** — Objective, Scope, Risk, Decision
- **Financial data** — Expected ROI, CAPEX, OPEX, approved budget, actual cost
- **Resource data** — skills, allocation, capacity
- **KPI data** — target and current values

In a real enterprise environment, the same design could be extended through authorized APIs and integrations with enterprise systems.

No live enterprise integrations are implemented in this prototype.

---

## Structured + Unstructured Information

The Confluence-style project information was not provided to the Agent as pre-structured columns.

The Agent works with project documents and extracts relevant information such as:

- Objective
- Scope
- Risk
- Decision

This allows structured portfolio data and unstructured project documentation to be considered within the same analysis.

---

## Decision Flow

The Agent follows the decision-support flow:

**Risk Detection → Root Cause Candidate Analysis → Resource / Capacity Analysis → Recommendation → Human Approval**

A project delay is not automatically treated as a resource problem.

The analysis considers blockers, dependencies, effort, resource/capacity information, financial data, KPI information, and other available delivery signals before producing a conclusion.

When a resource-related issue is supported by the available data, alternative resources can be evaluated based on:

- Skill compatibility
- Capacity
- Current assignments
- Project priorities
- Dependency impact
- Potential impact on other projects

If the available data does not support a safe alternative, the Agent should state this rather than inventing one.

---

## Delivery Risk Analysis

The current decision policy evaluates delivery risk across seven dimensions:

1. Schedule
2. Blocker
3. Effort
4. Dependency
5. Resource / Capacity
6. Financial Delivery Risk
7. KPI / Outcome Risk

A single metric does not automatically determine the overall risk.

For example, the existence of a blocker, dependency, approaching deadline, high budget utilization, or KPI gap is not treated as sufficient evidence on its own.

The Agent is designed to evaluate multiple supporting signals and avoid creating artificial risk simply to produce a result.

---

## Root Cause Candidate Analysis

Risk detection and root cause analysis are treated as separate steps.

The Agent does not automatically attribute a delivery problem to developer performance or resource capacity.

Possible root-cause categories include:

- Resource / Capacity
- Technical / System
- Dependency
- Access / Infrastructure
- Requirement / Scope
- External / Vendor
- UNKNOWN

When the available evidence is insufficient, the Agent uses a **Root Cause Candidate** or **UNKNOWN** rather than presenting an unsupported conclusion as fact.

---

## Grounding & Traceability

During testing, an output was identified that did not match the underlying source data.

This led to grounding and traceability becoming an explicit part of the Agent design.

The analysis distinguishes between:

- **FACT** — directly supported by source data
- **CALCULATED** — derived from source data using a repeatable calculation
- **INFERENCE** — a logical conclusion based on available facts and/or calculations
- **UNKNOWN** — required information is missing or insufficient

The Agent is instructed not to invent missing data, unsupported thresholds, people, dates, system information, or conclusions.

This makes it possible to distinguish what the Agent knows, what it calculates, what it infers, and where the available data is insufficient.

---

## Human-in-the-Loop

A core design principle is:

**The Agent recommends. The manager decides.**

The Agent can:

- Analyze project data
- Detect and explain risks
- Investigate possible root causes
- Evaluate available evidence
- Suggest possible actions

Critical actions are not intended to be applied without explicit human approval.

These include:

- Resource reassignment
- Deadline or milestone changes
- Scope changes
- Priority changes
- Risk acceptance or closure
- Changes to source-system data

The separation between recommendation and execution is part of the governance model.

---

## Agent Policy & Governance

The Agent's decision behavior is defined through a persistent policy layer rather than a standalone hard-coded risk script.

### `agent_policy/SKILL.md`

Defines the Agent's operating rules, including:

- Delivery risk evaluation
- Grounding requirements
- Root cause behavior
- Resource/capacity analysis
- Management reporting rules
- Human Approval controls
- Output and reporting behavior

### `agent_policy/references/karar-politikasi-v1.md`

Contains the detailed decision policy used by the Agent for portfolio delivery analysis.

The policy was iteratively refined during development to reduce unsupported assumptions and keep conclusions and recommendations traceable to the available project data.

---

## Data Validation

The repository also includes a Python validation script used to check the consistency of the prototype data.

This script supports data-quality checks before portfolio analysis is performed.

It is separate from the Agent's decision policy.

---

## Management Reporting View

The Agent is designed to help a manager understand the portfolio without reviewing every underlying data source individually.

The management view is intended to answer questions such as:

- What is the overall portfolio status?
- Which projects require attention?
- What is causing the problem?
- What could be affected?
- Is resource capacity contributing to the issue?
- Is a safe resource alternative available?
- Are there relevant financial or KPI signals?
- Which deliveries or milestones require attention?
- What action should management consider?

The objective is decision support rather than simply producing a risk dashboard.

---

## Development Approach

The prototype was developed using **Hermes and VS Code** with an agentic development approach.

The data model, decision rules, risk logic, guardrails, reporting behavior, and test scenarios were defined and refined through natural-language instructions and iterative testing.

A Python script was also used for prototype data validation.

The development process included reviewing Agent outputs against the underlying source data and refining the policy when unsupported assumptions or inconsistencies were identified.

---

## Prototype Scope

This repository is a prototype built with a synthetic eight-project portfolio.

It demonstrates the decision logic, grounding approach, governance model, and portfolio-analysis concept.

It does **not** represent a production deployment or a live connection to Jira, Confluence, HR, financial, or other enterprise systems.

In an enterprise implementation, authorized APIs, access controls, data governance, auditability, and system-specific integration requirements would need to be implemented separately.

---

## Repository Structure

```text
ai-delivery-agent/
│
├── agent_policy/
│   ├── SKILL.md
│   └── references/
│       └── karar-politikasi-v1.md
│
├── confluence_docs/
│   ├── PRJ-001_Confluence_Project_Overview.docx
│   ├── PRJ-002_Confluence_Project_Overview.docx
│   ├── ...
│   └── PRJ-008_Confluence_Project_Overview.docx
│
├── projects.csv
├── jira_issues.csv
├── financials.csv
├── people.csv
├── project_people.csv
├── kpi.csv
├── validate_data.py
└── README.md
```

---

<a id="türkçe"></a>

# Türkçe

## Genel Bakış

AI Delivery Agent, proje portföyü seviyesinde delivery analizi yapmak ve yönetim kararlarını desteklemek amacıyla geliştirilmiş bir prototiptir.

Amaç yalnızca “Hangi proje riskli?” sorusunu cevaplamak değildir.

Agent aşağıdaki soruların birlikte değerlendirilmesine yardımcı olacak şekilde tasarlanmıştır:

- Proje neden riskli?
- Olası root cause nedir?
- Bir dependency başka hangi projeleri etkileyebilir?
- Sorun gerçekten resource/capacity kaynaklı mı?
- Uygun başka bir kaynak varsa, kaynak değişikliği başka bir projeyi riske atabilir mi?
- Bütçe, ROI ve KPI verileri ne söylüyor?
- Mevcut verilere göre yönetimin dikkati nereye yönelmeli?

Agent, yapılandırılmış proje verileri ile proje dokümanlarından çıkarılan bilgileri aynı analiz içinde değerlendirerek portföy seviyesinde bir yönetim görünümü oluşturmayı amaçlar.

---

## Prototip Veri Kaynakları

Prototip, sentetik veriler kullanılarak oluşturulmuş bir kurumsal proje portföyünü simüle eder.

Analizde kullanılan veri grupları:

- **Jira benzeri veriler** — issue, blocker, dependency, assignee, effort, milestone
- **Confluence benzeri proje dokümanları** — Objective, Scope, Risk, Decision
- **Finansal veriler** — Expected ROI, CAPEX, OPEX, approved budget, actual cost
- **Kaynak verileri** — skill, allocation, capacity
- **KPI verileri** — target ve current değerler

Gerçek bir kurumsal ortamda aynı tasarım, yetkilendirilmiş API'ler ve kurumsal sistem entegrasyonları üzerinden genişletilebilir.

Bu prototipte canlı kurumsal sistem entegrasyonu bulunmamaktadır.

---

## Yapılandırılmış + Yapılandırılmamış Bilgi

Confluence benzeri proje bilgileri Agent'a hazır kolonlar halinde verilmemiştir.

Agent proje dokümanları üzerinden aşağıdaki gibi bilgileri değerlendirir:

- Objective
- Scope
- Risk
- Decision

Böylece yapılandırılmış portföy verileri ile proje dokümanlarındaki yapılandırılmamış bilgiler aynı analiz kapsamında ele alınabilir.

---

## Karar Akışı

Agent'ın karar destek akışı:

**Risk Tespiti → Root Cause Candidate Analysis → Resource / Capacity Analysis → Recommendation → Human Approval**

Bir projenin gecikmesi otomatik olarak kaynak problemine bağlanmaz.

Analizde blocker, dependency, effort, resource/capacity, finansal veriler, KPI bilgileri ve mevcut diğer delivery sinyalleri birlikte değerlendirilir.

Kaynak problemi mevcut verilerle destekleniyorsa alternatif kaynak değerlendirmesinde aşağıdaki unsurlar dikkate alınır:

- Skill uyumu
- Capacity
- Mevcut görevler
- Proje öncelikleri
- Dependency etkisi
- Değişikliğin diğer projelere olası etkisi

Mevcut veriler güvenli bir alternatif kaynağı desteklemiyorsa Agent'ın bunu açıkça belirtmesi ve alternatif uydurmaması beklenir.

---

## Delivery Risk Analizi

Mevcut karar politikası delivery riskini yedi boyutta değerlendirir:

1. Takvim
2. Blocker
3. Efor
4. Dependency
5. Resource / Capacity
6. Finansal Delivery Riski
7. KPI / Outcome Riski

Tek bir metrik otomatik olarak genel risk sonucunu belirlemez.

Örneğin bir blocker veya dependency bulunması, deadline'ın yaklaşması, bütçe kullanımının yüksek olması ya da KPI'ın target'a ulaşmamış olması tek başına yeterli risk kanıtı olarak değerlendirilmez.

Agent birden fazla destekleyici sinyali birlikte değerlendirecek ve yalnızca sonuç üretmek amacıyla yapay risk oluşturmayacak şekilde tasarlanmıştır.

---

## Root Cause Candidate Analysis

Risk tespiti ile root cause analizi birbirinden ayrı değerlendirilir.

Agent bir delivery problemini otomatik olarak developer performansına veya resource capacity'ye bağlamaz.

Olası root cause kategorileri:

- Resource / Capacity
- Technical / System
- Dependency
- Access / Infrastructure
- Requirement / Scope
- External / Vendor
- UNKNOWN

Yeterli kanıt bulunmadığında kesin bir root cause üretmek yerine **Root Cause Candidate** veya **UNKNOWN** kullanılır.

---

## Grounding ve İzlenebilirlik

Testler sırasında Agent tarafından üretilen bir sonucun kaynak veriyle uyuşmadığı tespit edildi.

Bu nedenle grounding ve izlenebilirlik Agent tasarımının açık bir parçası haline getirildi.

Analizde aşağıdaki ayrım kullanılır:

- **FACT** — doğrudan kaynak veriden doğrulanabilen bilgi
- **CALCULATED** — kaynak verilerden tekrarlanabilir bir hesaplamayla elde edilen bilgi
- **INFERENCE** — mevcut fact ve/veya calculated bilgilerden yapılan mantıksal çıkarım
- **UNKNOWN** — karar için gerekli bilginin eksik veya yetersiz olması

Agent'ın eksik veri, desteklenmeyen threshold, kişi, tarih, sistem bilgisi veya sonuç uydurmaması karar politikasının bir parçasıdır.

Bu yaklaşım Agent'ın neyi bildiğini, neyi hesapladığını, nerede çıkarım yaptığını ve nerede yeterli veri bulunmadığını ayrıştırmayı amaçlar.

---

## Human-in-the-Loop

Temel tasarım prensibi:

**Agent önerir. Kararı yönetici verir.**

Agent:

- Proje verilerini analiz edebilir
- Riskleri tespit edip açıklayabilir
- Olası root cause'ları araştırabilir
- Mevcut kanıtları değerlendirebilir
- Olası aksiyonlar önerebilir

Ancak kritik aksiyonların açık insan onayı olmadan uygulanmaması tasarımın bir parçasıdır.

Bunlara örnek olarak:

- Resource reassignment
- Deadline veya milestone değişikliği
- Scope değişikliği
- Priority değişikliği
- Risk kabulü veya kapatılması
- Kaynak sistem verilerinin değiştirilmesi

verilebilir.

Recommendation ile execution'ın ayrılması yönetişim modelinin temel parçalarından biridir.

---

## Agent Karar Politikası ve Yönetişim

Agent'ın karar verme davranışı, tek başına hard-coded bir risk scripti yerine kalıcı bir politika katmanı üzerinden tanımlanmıştır.

### `agent_policy/SKILL.md`

Agent'ın çalışma kurallarını tanımlar. Bunlar arasında:

- Delivery risk değerlendirmesi
- Grounding gereksinimleri
- Root cause davranışı
- Resource/capacity analizi
- Yönetici raporlama kuralları
- Human Approval kontrolleri
- Çıktı ve raporlama davranışı

bulunur.

### `agent_policy/references/karar-politikasi-v1.md`

Agent'ın portföy delivery analizinde kullandığı detaylı karar politikasını içerir.

Politika, geliştirme sırasında desteklenmeyen varsayımları azaltmak ve sonuçlarla önerilerin mevcut proje verileriyle izlenebilir olmasını sağlamak amacıyla iteratif olarak geliştirilmiştir.

---

## Veri Doğrulama

Repository'de prototip verilerinin tutarlılığını kontrol etmek amacıyla kullanılan bir Python validation scripti de bulunmaktadır.

Bu script portföy analizi öncesinde veri kalitesinin kontrol edilmesini destekler.

Validation scripti Agent'ın karar politikasından ayrı bir katmandır.

---

## Yönetici Raporlama Görünümü

Agent, yöneticinin her veri kaynağını ayrı ayrı incelemesine gerek kalmadan portföyün durumunu değerlendirmesine yardımcı olacak şekilde tasarlanmıştır.

Yönetim görünümünün aşağıdaki sorulara cevap vermesi amaçlanır:

- Portföyün genel durumu nasıl?
- Hangi projeler dikkat gerektiriyor?
- Sorunun nedeni ne?
- Neler etkilenebilir?
- Resource capacity probleme katkı sağlıyor mu?
- Güvenli bir alternatif kaynak var mı?
- Önemli finansal veya KPI sinyalleri bulunuyor mu?
- Hangi teslimatlar veya milestone'lar dikkat gerektiriyor?
- Yönetimin hangi aksiyonu değerlendirmesi gerekiyor?

Amaç yalnızca bir risk dashboard'u üretmek değil, karar desteği sağlamaktır.

---

## Geliştirme Yaklaşımı

Prototip **Hermes ve VS Code** kullanılarak agentic development yaklaşımıyla geliştirilmiştir.

Veri modeli, karar kuralları, risk mantığı, guardrail'ler, raporlama davranışı ve test senaryoları doğal dil üzerinden tanımlanmış ve iteratif testlerle geliştirilmiştir.

Bir Python scripti prototip verilerinin doğrulanmasında da kullanılmıştır.

Geliştirme sürecinde Agent çıktıları kaynak verilerle karşılaştırılmış; desteklenmeyen varsayımlar veya tutarsızlıklar tespit edildiğinde karar politikası geliştirilmiştir.

---

## Prototip Kapsamı

Bu repository, sekiz projelik sentetik bir portföy kullanılarak oluşturulmuş bir prototiptir.

Decision logic, grounding yaklaşımı, governance modeli ve portföy analiz yaklaşımını göstermektedir.

Production ortamında çalışan veya Jira, Confluence, İK, finans ya da diğer kurumsal sistemlere canlı bağlı bir çözüm değildir.

Gerçek bir kurumsal uygulamada yetkilendirilmiş API'ler, erişim kontrolleri, veri yönetişimi, auditability ve sisteme özgü entegrasyon gereksinimlerinin ayrıca uygulanması gerekir.

---

## Repository Yapısı

```text
ai-delivery-agent/
│
├── agent_policy/
│   ├── SKILL.md
│   └── references/
│       └── karar-politikasi-v1.md
│
├── confluence_docs/
│   ├── PRJ-001_Confluence_Project_Overview.docx
│   ├── PRJ-002_Confluence_Project_Overview.docx
│   ├── ...
│   └── PRJ-008_Confluence_Project_Overview.docx
│
├── projects.csv
├── jira_issues.csv
├── financials.csv
├── people.csv
├── project_people.csv
├── kpi.csv
├── validate_data.py
└── README.md
```

---

## Key Principle

**AI supports the decision. Human accountability remains with the manager.**

## Temel Prensip

**AI kararı destekler. Nihai sorumluluk yöneticide kalır.**
