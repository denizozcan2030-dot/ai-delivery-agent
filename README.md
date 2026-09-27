# AI Delivery Agent

**AI-Assisted Portfolio Risk Analysis & Decision Support**

[English](#english) | [Türkçe](#türkçe)

---

# English

## Overview

AI Delivery Agent is a decision-support prototype built around a synthetic portfolio of 8 technology projects.

The goal was not simply to answer **“Which project is at risk?”** but to help evaluate the questions that come next:

- Why is the project at risk?
- What is the root cause?
- Which other projects could be affected by a dependency?
- Is the problem actually caused by insufficient resources?
- If another suitable resource is available, could reallocating that person create risk elsewhere?
- What do budget, ROI, CAPEX, OPEX, and KPIs indicate?
- Where should management attention be focused at a given point in time?

The result is an AI Delivery Agent designed to bring these questions into a single decision-support flow.

> **The agent recommends. The manager decides.**

---

## Data Sources

The prototype combines synthetic data representing common enterprise systems and information sources:

**Jira-style data**
- Issues, blockers, dependencies
- Assignees, effort, milestones

**Confluence-style project documents**
- Objective
- Scope
- Risk
- Decision

**Financial data**
- ROI, CAPEX, OPEX
- Budget and actual cost

**Resource / People data**
- Skills
- Allocation
- Capacity

**KPI data**
- Target and actual values

All data in this repository is synthetic. No real company or personal data is used.

---

## Structured + Unstructured Information

Confluence-style information was not provided to the agent as pre-structured columns.

The agent reads the project documents and extracts information such as **Objective, Scope, Risk, and Decision**, then evaluates it together with structured project, Jira, financial, resource, and KPI data.

This allows structured data and unstructured project documentation to contribute to the same portfolio analysis.

---

## Decision Flow

**Risk Detection → Root Cause Analysis → Resource Optimization → Recommendation → Human Approval**

### Risk Detection

The agent evaluates indicators including project progress, deadlines, blockers, blocker age, dependencies, effort, financial information, and KPI performance.

### Root Cause Analysis

A delayed project is not automatically treated as a resource problem.

The agent evaluates blockers, dependencies, and other available evidence to determine the likely cause of the risk.

### Dependency Impact

When a dependency contributes to a risk, the analysis considers which other projects may also be affected.

This extends the analysis from an individual project view to a portfolio-level view.

### Resource Optimization

If the evidence indicates a resource-related problem, the agent evaluates alternatives based on:

- Required skills
- Available capacity
- Current allocation
- Existing project responsibilities

It also considers whether moving a resource could create additional risk in another project.

If there is no suitable alternative, the agent should state this instead of forcing a recommendation.

### Recommendation & Human Approval

The agent uses the available project, dependency, resource, financial, and KPI context to generate a recommendation.

Critical actions such as resource changes, project priorities, or delivery date changes are not applied without human approval.

---

## Grounding & Traceability

During testing, I identified a case where an agent-generated result did not match the underlying source data.

As a result, grounding and traceability became an explicit part of the design.

Agent outputs are separated into four categories:

- **FACT** — directly supported by source data
- **CALCULATED** — derived from available data
- **INFERENCE** — interpretation based on available evidence
- **UNKNOWN** — cannot be reliably determined from the available data

This makes it clearer what the agent knows, what it calculates, where it makes an inference, and where the available evidence is insufficient.

---

## Human-in-the-Loop

The prototype is designed as a decision-support system, not an autonomous decision-maker.

**Agent recommends → Human reviews → Human approves or rejects**

Resource allocation, priority, and delivery date decisions remain under human control.

---

## Data Validation

Before portfolio analysis, the datasets are checked for consistency, including:

- Project ID consistency
- Employee ID consistency
- Jira issue references
- Dependency relationships
- Orphan Jira records
- Cross-file reference errors

Python validation scripts are included in the repository.

---

## Management View

The default management-level output is intentionally concise:

**Project Name | Overall Status | Upcoming Critical Milestone / Date | Short Note**

Detailed analysis can then explain the evidence behind the status, root cause, dependency impact, resource considerations, and recommendation.

---

## Development Approach

The prototype was developed using:

- **Hermes**
- **Visual Studio Code**
- **Python-based data validation**
- **Synthetic enterprise data**
- **Agentic development approach**

I defined and iteratively refined the data model, decision rules, risk logic, guardrails, and test scenarios through natural-language instructions.

The focus was not only on generating an output, but also on defining how the agent should evaluate portfolio information, how its conclusions should be grounded, and where human approval should remain mandatory.

---

## Prototype Scope

This repository represents a prototype and does **not** contain live enterprise integrations.

Because I did not have access to corporate systems, Jira, Confluence, finance, resource/HR, and KPI information were simulated through an 8-project synthetic dataset and project documents.

In a real enterprise environment, the same design could be extended through authorized APIs and integrations to retrieve current information from approved systems.

The core question behind the project is:

> **Where is the problem, why is it happening, what is the impact, and what can we do about it?**

with one important boundary:

> **The final decision belongs to the human manager.**

---

## Repository Structure

```text
ai-delivery-agent/
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
└── validate_data2.py
```

---

# Türkçe

## Genel Bakış

AI Delivery Agent, 8 projelik sentetik bir teknoloji portföyü üzerinde geliştirdiğim bir karar destek prototipidir.

Amacım yalnızca **“Hangi proje riskli?”** sorusuna cevap veren bir yapı oluşturmak değildi. Agent'ın bu sorudan sonra bir yöneticinin değerlendirmesi gereken konulara da birlikte bakabilmesini hedefledim:

- Proje neden riskli?
- Root cause nedir?
- Bir dependency başka hangi projeleri etkileyebilir?
- Sorun gerçekten kaynak yetersizliği mi?
- Uygun başka bir kaynak varsa, bu kişinin kaydırılması başka bir projeyi riske atar mı?
- Bütçe, ROI, CAPEX, OPEX ve KPI'lar ne söylüyor?
- T anında yönetimin dikkati nereye yönelmeli?

Ortaya bu soruları tek bir karar destek akışında değerlendirmek üzere tasarlanan bir AI Delivery Agent çıktı.

> **Agent önerir. Kararı yönetici verir.**

---

## Veri Kaynakları

Prototipte kurumsal sistemleri ve bilgi kaynaklarını temsil eden sentetik veriler birlikte kullanıldı:

**Jira benzeri veriler**
- Issue, blocker, dependency
- Assignee, effort, milestone

**Confluence benzeri proje dokümanları**
- Objective
- Scope
- Risk
- Decision

**Finansal veriler**
- ROI, CAPEX, OPEX
- Bütçe ve gerçekleşen maliyet

**Kaynak / İK verileri**
- Yetkinlik
- Allocation
- Capacity

**KPI verileri**
- Hedef ve gerçekleşen değerler

Repository'deki verilerin tamamı sentetiktir. Gerçek şirket veya kişisel veri kullanılmamıştır.

---

## Yapılandırılmış + Yapılandırılmamış Bilgi

Confluence benzeri bilgiler Agent'a hazır kolonlar halinde verilmedi.

Agent proje dokümanlarını okuyarak **Objective, Scope, Risk ve Decision** gibi bilgileri çıkarır ve bunları yapılandırılmış proje, Jira, finans, kaynak ve KPI verileriyle birlikte değerlendirir.

Böylece yapılandırılmış veriler ile proje dokümanlarındaki yapılandırılmamış bilgiler aynı portföy analizinde birleşir.

---

## Karar Akışı

**Risk Tespiti → Root Cause Analysis → Resource Optimization → Recommendation → Human Approval**

### Risk Tespiti

Agent; proje ilerlemesi, deadline, blocker'lar, blocker yaşı, dependency'ler, effort, finansal bilgiler ve KPI performansı gibi göstergeleri değerlendirir.

### Root Cause Analysis

Bir proje gecikiyorsa Agent bunu doğrudan kaynak problemine bağlamaz.

Blocker'ları, dependency'leri ve mevcut diğer kanıtları değerlendirerek riskin muhtemel nedenini belirlemeye çalışır.

### Dependency Etkisi

Bir dependency riske katkıda bulunuyorsa, bundan başka hangi projelerin etkilenebileceği de değerlendirilir.

Böylece analiz tek bir projeden portföy seviyesine taşınır.

### Resource Optimization

Sorunun kaynakla ilişkili olduğuna dair kanıt varsa Agent alternatifleri şu bilgiler üzerinden değerlendirir:

- Gerekli yetkinlik
- Mevcut capacity
- Allocation
- Mevcut proje sorumlulukları

Bir kaynağın başka bir projeden alınmasının o projede yeni bir risk oluşturup oluşturmayacağı da dikkate alınır.

Uygun alternatif yoksa Agent'ın zorla bir öneri üretmesi yerine bunu belirtmesi beklenir.

### Recommendation & Human Approval

Agent; proje, dependency, kaynak, finans ve KPI bağlamını birlikte değerlendirerek bir öneri oluşturur.

Kaynak değişikliği, proje önceliği veya teslimat tarihi gibi kritik aksiyonlar insan onayı olmadan uygulanmaz.

---

## Grounding ve İzlenebilirlik

Testler sırasında Agent'ın ürettiği bir sonucun kaynak veriyle uyuşmadığı bir durum tespit ettim.

Bu nedenle grounding ve izlenebilirliği tasarımın açık bir parçası haline getirdim.

Agent çıktıları dört kategoriye ayrılır:

- **FACT** — kaynak veri tarafından doğrudan desteklenen bilgi
- **CALCULATED** — mevcut verilerden hesaplanan bilgi
- **INFERENCE** — mevcut kanıtlara dayanarak yapılan çıkarım
- **UNKNOWN** — mevcut verilerle güvenilir şekilde belirlenemeyen bilgi

Bu ayrım, Agent'ın neyi bildiğini, neyi hesapladığını, nerede çıkarım yaptığını ve nerede yeterli veri olmadığını daha görünür hale getirir.

---

## Human-in-the-Loop

Prototip otonom karar veren bir sistem olarak değil, karar destek sistemi olarak tasarlandı.

**Agent önerir → İnsan değerlendirir → İnsan onaylar veya reddeder**

Kaynak değişikliği, öncelik ve teslimat tarihi gibi kritik kararlar insan kontrolünde kalır.

---

## Veri Doğrulama

Portföy analizinden önce veri setleri arasındaki tutarlılık kontrol edilir:

- Project ID tutarlılığı
- Employee ID tutarlılığı
- Jira issue referansları
- Dependency ilişkileri
- Orphan Jira kayıtları
- Dosyalar arası referans hataları

Bu kontroller için kullanılan Python validation scriptleri repository'de bulunmaktadır.

---

## Yönetici Görünümü

Varsayılan yönetici çıktısı bilinçli olarak kısa tutuldu:

**Proje Adı | Genel Durum | Yaklaşan Kritik Nokta / Tarih | Kısa Not**

Gerektiğinde detay analiz; durumun arkasındaki kanıtları, root cause'u, dependency etkisini, kaynak değerlendirmesini ve öneriyi açıklar.

---

## Geliştirme Yaklaşımı

Prototipi geliştirirken:

- **Hermes**
- **Visual Studio Code**
- **Python tabanlı veri doğrulama**
- **Sentetik kurumsal veri**
- **Agentic development yaklaşımı**

kullandım.

Veri modelini, karar kurallarını, risk mantığını, guardrail'leri ve test senaryolarını doğal dil üzerinden tanımlayarak Agent'ın davranışını iteratif olarak geliştirdim.

Amaç yalnızca bir çıktı üretmek değil; Agent'ın portföy bilgisini nasıl değerlendireceğini, sonuçlarını hangi verilere dayandıracağını ve hangi noktalarda insan onayının zorunlu kalacağını tasarlamaktı.

---

## Prototip Kapsamı

Bu repository bir prototiptir ve **canlı kurumsal sistem entegrasyonları içermez.**

Gerçek kurumsal sistemlere erişimim olmadığı için Jira, Confluence, finans, kaynak/İK ve KPI yapılarını 8 projelik sentetik veri seti ve proje dokümanları üzerinden simüle ettim.

Gerçek bir kurumsal ortamda aynı tasarım, yetkilendirilmiş API'ler ve entegrasyonlar aracılığıyla onaylı sistemlerden güncel verilerin alınabileceği şekilde genişletilebilir.

Projenin temel sorusu:

> **Nerede sorun var, neden var, etkisi ne ve ne yapabiliriz?**

En önemli sınırı ise:

> **Son karar insandadır.**

---

## Repository Yapısı

```text
ai-delivery-agent/
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
└── validate_data2.py
```
