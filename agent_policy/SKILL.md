---
name: delivery-risk-policy
description: "Apply Karar Politikası v1 for 7-dim risk analysis."
category: project-management
tags: [risk, delivery, policy, governance]
auto_load: true
version: "1.0.0"
author: "AI Delivery Agent"
license: "MIT"
metadata:
  hermes:
    tags: [risk, delivery, policy, governance]
    related_skills: []
---

## When to Use

Use this skill when performing **delivery risk analysis** for the AI Delivery Agent portfolio (projects PRJ-001 through PRJ-008). It loads the binding policy (Karar Politikası v1) that governs:

- 7-dimension risk evaluation (Schedule, Blocker, Effort, Dependency, Resource/Capacity, Financial, KPI/Outcome)
- FACT / CALCULATED / INFERENCE / UNKNOWN evidence labeling
- No synthetic thresholds, scoring, or data
- Human-in-the-loop: DETECT → EXPLAIN → RECOMMEND → HUMAN DECISION → ACTION
- Default output: short Executive Summary; detailed evidence only on request

The policy reference file is at `references/karar-politikasi-v1.md`.

---

# AI Delivery Agent — Delivery Risk Policy (v1)

Bu skill, AI Delivery Agent'ın risk analizlerindeki **kalıcı çalışma kurallarını** tanımlar. Politika metni tek kaynakta tutulur: `references/karar-politikasi-v1.md`.

## 1. Politika Kaynağı

**Source of Truth**: `references/karar-politikasi-v1.md` dosyası.  
Bu dosya Karar Politikası v1'in **tam metnini** içerir. SKILL.md bu dosyaya referans verir; politika metni kopyalanmaz.

## 2. Çalışma Prensipleri (Özet)

### Veri ve Grounding
- **Kaynaklar**: Sadece önceden tanımlı dosyalar (`projects.csv`, `jira_issues.csv`, `financials.csv`, `people.csv`, `project_people.csv`, `kpi.csv`, `confluence_docs/`)
- **Dış kaynak yok**: İnternet araması, varsayılan sistemler, sentetik veri üretilmez
- **Sınıflandırma**: Her önemli bulgu **FACT / CALCULATED / INFERENCE / UNKNOWN** etiketiyle sunulur
- **CALCULATED** için formül açıkça belirtilir

### Risk Değerlendirme (7 Boyut)
1. Takvim Riski
2. Blocker Riski
3. Efor Riski
4. Bağımlılık Riski
5. Kaynak / Kapasite Riski
6. Finansal Delivery Riski
7. KPI / Outcome Riski

**Kurallar**:
- Tek metrik → HIGH **yok**; en az 2-3 destekleyici sinyal birleşimi gerekir
- Normal operasyon risk olarak etiketlenmez
- **LOW** = "mevcut veriler anlamlı delivery tehdidi göstermiyor" (hiç risk yok değil)
- Eşik/ağırlık/scoring modeli **oluşturulmaz** (şirket politikası yoksa)
- Risk seviyesi güvenilir ayrıştırılamıyorsa **UNKNOWN**

### Root Cause
- Kesin "Root Cause = X" üretilmez
- "OLASI ANA NEDEN / ROOT CAUSE CANDIDATE" kullanılır
- Developer performansı hakkında kanıtsız çıkarım yok

### KPI Özel Kuralı
- KPI Target Direction / Comparator **isimden tahmin edilmez**
- Tanımlı kaynakta explicit yoksa → **UNKNOWN**

### Business Impact & Customer Impact
- Delivery Risk'ten **ayrı** değerlendirilir
- Strategic Priority, Expected ROI, CAPEX, Approved Budget kullanılır
- Resmi eşik yoksa sınıflandırma **UNKNOWN**; FACT'ler gösterilir
- Customer/User Impact verisi yoksa → **UNKNOWN**

### Management Attention
- Delivery Risk + Business Impact birleşimiyle
- Şirket onaylı model yoksa **UNKNOWN**; bu hata değil

### Human-in-the-Loop
- **DETECT → EXPLAIN → RECOMMEND → HUMAN DECISION → ACTION**
- Agent: resource reassignment, scope/deadline/priority değişikliği **uygulamaz**
- Bu aşamada (Aşama 1): **RECOMMENDATION YOK** — sadece DETECT + EXPLAIN

### Veri Kaynağı ve UNKNOWN Kuralı
- Gerekli veri ana kaynakta yoksa → sadece önceden tanımlı kurumsal kaynaklar kontrol edilir
- Hiçbir tanımlı kaynakta bilgi yoksa → tahmin **yapılmaz**, **UNKNOWN** döndürülür
- Bu kural KPI Target Direction için de geçerlidir

## 3. Çıktı Formatı

### Varsayılan: Kısa Yönetici Özeti (Executive Summary)
**Hedef kitle**: Yönetici / Üst yönetim (teknik olmayan)
**Dil**: Açık, sade, teknik jargonsuz Türkçe

**ZORUNLU 4 BÖLÜM** (her biri en fazla 1-2 kısa cümle):

1. **Ne oluyor?** — Durumun özeti (örn: "Bulut altyapı projesinde kritik bir onay süreci gecikiyor ve bu da 5 diğer projeyi etkiliyor.")
2. **Neden önemli?** — İş etkisi (örn: "Bu gecikme, ödeme sistemleri ve mobil uygulamalar da dahil kritik sistemlerin canlıya geçişini riske atıyor.")
3. **Ne öneriyorsun?** — Seçenekler (örn: "Onay sürecini hızlandırmak için müdahale edebiliriz, teslim tarihini kaydırabiliriz, ya da geçici bir çözüm yolu deneyebiliriz.")
4. **Eksik bilgi / Yönetici kararı gerekiyorsa nedir?** — Bilgi boşlukları ve karar noktaları (örn: "Onay yetkisi kime ait, süreç ne kadar sürer, geçici çözüm güvenlik politikalarına uygun mu? Bu konularda yönetim kararı bekleniyor.")

**RAPOR DİLİ VE TPM TERMİNOLOJİSİ**

Raporun tamamı doğal, açık ve kurumsal Türkçe cümlelerle yazılmalıdır.

Ancak sektörde ve Technical Product / Project Management çalışmalarında yerleşik olarak kullanılan İngilizce teknik terimleri **Türkçeleştirme**.

Örneğin gerektiğinde şu terimler kullanılmaya devam edebilir:
Development, SIT, UAT, Go-Live, Production, blocker, dependency, milestone, allocation, capacity, skill, root cause, delivery risk, KPI, ROI, CAPEX, OPEX, API, TPM, PO, PM, DevOps, QA, CI/CD, DR.

**Milestone ve iş adları (Jira Summary, Milestone adı vb.)** raporlarda **doğal Türkçe** yazılır. Örn: "Payment API Integration Complete" → "Ödeme API entegrasyonu tamamlandı", "Migration Cutover Routing Ready" → "Migration cutover yönlendirme hazır".

Ama teknik terimleri Türkçe cümlelerin içine anlamsız veya mekanik biçimde yerleştirme.
Kelime kelime çeviri nedeniyle doğal olmayan ifadeler üretme.

**KULLANILMAYACAK İFADELER (örnekler):**
"kalite kapıları", "değerlendirmesi bekliyor", "darboğaz sistematik", "compliance-driven proje", "downstream etkisi", "gating dependency", "aşağı akış projesi", "milestone bugün due", "kritik yolundaki anahtar proje".

Amaç teknik terminolojiyi kaldırmak DEĞİLDİR.
Amaç: DOĞAL TÜRKÇE CÜMLE + DOĞRU TPM/PO/PM TEKNİK TERMİNOLOJİSİ kullanmaktır.

**CÜMLE YAPISI VE OKUNABİLİRLİK**

Raporun tamamında kısa, açık ve tek anlamlı cümleler kullan.

Bir cümlenin içine: neden + etki + belirsizlik + öneri + kaynak durumu gibi birden fazla mesajı sıkıştırma.
Noktalı virgülle uzun ve karmaşık cümleler oluşturma.
Her cümlenin ne söylediği ilk okumada anlaşılmalıdır.

Mümkün olduğunda şu düşünce sırasını kullan: Durum → Neden → Etki → Öneri.

ÖRNEK (KÖTÜ): "Test kapasitesi darboğazı tüm proje kalite kapılarını etkiler; bu konu yönetim planlaması ve/veya dış kaynak destek değerlendirmesi bekliyor. Kaynak değişikliği mevcut verilerde mümkün değil."

ÖRNEK (DOĞRU): "Test capacity riski bulunuyor. Selin Arslan 6 projede test faaliyetlerinden sorumlu. Mevcut ekipte aynı skill set'e sahip uygun bir alternatif kaynak bulunmuyor. Bu durum projelerin SIT ve UAT süreçlerini etkileyebilir. Test işlerinin öncelikleri ve ek kaynak ihtiyacı değerlendirilmelidir."

Bu örnek sabit metin DEĞİLDİR. Her run'da güncel veriye göre sonucu yeniden üret.

---

**YASAK (varsayılan raporun hiçbir bölümünde gösterilmez):**
- FACT, CALCULATED, INFERENCE, UNKNOWN etiketleri
- Internal ID: PRJ-xxx, EMP-xxx, IAM-xxx, DAT-xxx, CLD-xxx, PAY-xxx, MOB-xxx, CSP-xxx, AIR-xxx, CRM-xxx, KPI-xxx
- Internal ID prefix: IAM-, PAY-, CLD-, DAT-, CRM-, PRJ- (veya Jira/internal key formatında benzeri)
- Jira Issue Key: PAY-102, CLD-605, IAM-705, DAT-503, vb.
- Teknik hesaplama / formül (%240, 9 gün, 156 saat, vb.)
- İngilizce sistem terimleri (gating, downstream, critical path, temporal impossibility, cascade, workaround, RACI, escalation, SLA, FTE, CI/CD, DR, UAT, vb.)
- Veri doğrulama tabloları, allocation tabloları, root cause teknik analizi

> Bu detaylar **arka planda kanıt olarak tutulur** ve yalnızca kullanıcı **"detay"**, **"kanıt"**, **"teknik detay"**, **"açıkla"**, **"proje bazlı"**, **"FACT"**, **"jira"**, **"formül"** gibi ifadeler kullandığında gösterilir.

**UNKNOWN gösterimi**: "Bu bilgi mevcut kaynaklarda bulunamadı" / "Bu konuda yeterli veri yok" gibi doğal Türkçe ifadelerle.

**Internal ID / Jira Key Gösterim Yasağı (Tüm Rapor Bölümleri):**
Varsayılan yönetici raporunun **hiçbir bölümünde** (Portföy Tablosu, Yönetici Dikkati, Kaynak & Kapasite, Finans & KPI, Yaklaşan Teslimatlar) IAM-xxx, PRJ-xxx, EMP-xxx, DAT-xxx, CLD-xxx, PAY-xxx, MOB-xxx, CSP-xxx, AIR-xxx, CRM-xxx, KPI-xxx, Jira Issue Key (PAY-102, CLD-605, IAM-705, DAT-503 vb.) veya başka herhangi bir internal ID gösterilmez. Analizde kullanılabilirler ancak raporda ilgili işin/bağımlılığın/anlaşılır doğal adı kullanılır.

### Detay Modu (İsteğe Bağlı)
Kullanıcı yukarıdaki tetikleyici ifadelerden birini kullandığında:
- Proje bazlı 7 boyut değerlendirmesi
- Her boyut için FACT / CALCULATED (formül) / INFERENCE / UNKNOWN dayanakları (tam teknik detayla)
- Root Cause Candidate (teknik analiz dahil)
- Business Impact FACT'leri
- Customer Impact & Management Attention
- Jira Issue Key'ler, allocation tabloları, hesaplama formülleri, dependency grafikleri

---

## 6. İNSAN ONAYİ (HUMAN APPROVAL) KURALI

**Agent şunları YAPABİLİR:**
- Veri analizi yapma
- Risk tespiti ve açıklama
- Olası ana neden (root cause candidate) araştırma
- Çözüm seçenekleri önerme

**Agent şunları KULLANICI AÇIK ONAYI OLMADAN YAPAMAZ:**
- Görev veya kaynak ataması değiştirme
- Proje tarihi (deadline, milestone) değiştirme
- Kapsam (scope) veya öncelik değiştirme
- Risk kabul etme / kapatma
- Kaynak sistemlerde (CSV, Jira, Confluence, vb.) veri oluşturma, değiştirme, silme
- Herhangi bir "uygula", "kaydet", "gönder", "atama" eylemi

**Onay Süreci:**
1. Agent öneri sunduğunda: **ne değiştirmek istediğini** ve **beklenen etkisini** sade Türkçe açıklar
2. Kullanıcı **"Onaylıyorum"**, **"uygula"**, **"evet"** gibi açık onay verene kadar **hiçbir değişiklik yapmaz**
3. "Düşünüyorum", "bakalım", "belki" gibi belirsiz yanıtlar onay SAYILMAZ
4. Onay alınıcaya kadar agent sadece analiz ve öneri modunda kalır

> Bu kural Aşama 1'den itibaren geçerlidir. Agent asla "varsayılan olarak uygular" veya "sessizce değiştirir" davranışı sergilemez.

## 7. PORTFÖY SEVİYESİ YÖNETİCİ RAPORU (Varsayılan Çıktı)

**Tetikleyici**: Kullanıcı "portföy durumu", "genel durum", "portföy özeti", "tüm projeler", "portföyün güncel durumu", "yönetici raporu" gibi ifadeler kullandığında.

**Davranış**: Portföyün **tamamını** değerlendir (sadece en kritik projeye odaklanma). Tüm 7 veri kaynığını ve 46 bilgi grubunu arka planda tarama yap, ancak çıktıda yöneticinin tek bakışta portföyü görüp karar alabileceği **sade tablo + 4 yönetici özeti** formatında sade, doğal Türkçe sun.

---

### ÇIKTI FORMATI

#### 1 — PORTFÖY TABLOSU

8 projenin tamamı, 6 sütun:

| Proje | Aşama | Durum | Sorumlu | Ana Sorun | Önerilen Aksiyon |
|---|---|---|---|---|---|
| [Proje Adı (gerekirse Türkçe karşılık)] | [Development / SIT / UAT / Go-Live / Production / Belirlenemedi] | [🟢 Normal / 🟡 Takip Gerekiyor / 🔴 Riskli / ⚫ Bloke] | [Ad Soyad / Belirlenemedi] | [1 kısa cümle: en önemli problem / "Kritik sorun görünmüyor"] | [1 kısa cümle: ne yapılabileceği / "Yönetim kararı bekliyor" / "Mevcut verilerle güvenli kaynak aktarımı doğrulanamadı" / "Kaynak değişikliği ana problemi çözmez; [asıl neden] bekleniyor"] |

**Sütun Kuralları:**

- **Proje**: resources/projects.csv'deki Project_Name. İngilizce ad teknik olmayan yönetici için zor ise yanına parantezle kısa Türkçe karşılık. Jira kodları (PRJ-xxx) gösterilmez.
- **Aşama**: Sadece kaynaklardan (Jira issue status dağılımı, milestone, Confluence) doğrulanabiliyorsa. Kurumsal terimler: **Development / SIT / UAT / Go-Live Preparation / Production**. Proje tek bir net aşamadaysa o aşama yazılır. Birden fazla aşama varsa en ileri/güncel aşama gösterilir; belirsiz yan yana sıralama yapmaz. Doğrulanamıyorsa **UNKNOWN** gösterilir; stage uydurulmaz.
- **Durum**: Arka planda 7 boyut + Business Impact + Management Attention birleşik sinyaliyle. **Sadece** 🟢 🟡 🔴 ⚫. Tek metrik → risk değil. Normal operasyon risk değil. Sınıflandırma güvenilir değilse 🟡 Takip Gerekiyor.
- **Sorumlu**: project_people.csv'de Role_In_Project = "Project Lead" / "Program Lead" / "Product Lead" / "DevOps Lead" / "Security Lead" vb. açıkça tanımlıysa. Yoksa Confluence "Approvals/Decisions" sahibi. Hiçbiri yoksa **"Belirlenemedi"**. Kişi/uydurma yok.
- **Ana Sorun**: Riskli/Bloke projelerde — riskin **temel nedeni + teslimata etkisi** teknik olmayan dille 1 cümle. Normal projelerde: "Kritik sorun görünmüyor".
- **Önerilen Aksiyon**: Veriler destekliyorsa uygulanabilir çözüm 1 cümle. **Kesinlik/tarih/yetki/sonuç uydurma** ("bugün tamamlanmalı", "şu tarihe ertelenmeli", "kesin gecikecek" YASAK). Kanıta uygun dil: "Onay sürecinin tamamlanma tarihi netleştirilmeli ve teslimata etkisi değerlendirilmeli." **Kaynak/kişi değişikliği önerisi verilecekse**: Önce güvenli aktarım doğrulanmalı (skill eşleşmesi + allocation + aktif görevler + diğer projelere etki + öncelikler). Uygun kişi varsa: "X işinin Y kişisine aktarılması değerlendirilebilir (neden: ...)". Yoksa: **"Mevcut verilerle güvenli bir kaynak aktarımı doğrulanamadı."** Kaynak değişikliği ana problemi çözmezse: **"Kaynak değişikliği ana problemi çözmez; [asıl neden] bekleniyor."** Hiçbir atama onay olmaz değiştirilmez.

> **Arka Planda Kullanılan (Tabloya Yazılmayan):** Delivery Risk, Business Impact, Management Attention, KPI Durumu, Finansal Durum (ROI, CAPEX, OPEX, Budget, Actual Cost). Bu sınıflandırmalar tabloya yazılmaz; yalnızca özetlerde anlamlı bulgu olarak yansıtılır.

---

#### 2 — YÖNETİCİ DİKKATİ

Sadece gerçekten yönetici dikkati gerektiren **en önemli 2–3 proje**.

Her biri için şu formatı kullan:

```
Proje: [Proje adı]

Neden:
[Problemin neden yönetici dikkati gerektirdiğini 1 kısa cümleyle açıkla.]

Etkisi:
[Delivery, milestone, dependency, finans, KPI veya diğer projelere etkisini 1 kısa cümleyle açıkla.]

Öneri:
[Yönetimin değerlendirmesi gereken aksiyonu 1 kısa cümleyle açıkla.]
```

Bir alan gerçekten iki cümle gerektiriyorsa en fazla 2 kısa cümle kullan.

Internal ID, ham Jira analizi veya gereksiz teknik kanıt gösterme.

Risk Engine / Business Impact / Management Attention teknik sınıflandırmaları kullanıcıya anlatılmaz; arka planda kullanılır.

---

#### 3 — KAYNAK & KAPASİTE

**Proje Riski ile Resource/Capacity Riski Bağımsız Değerlendirilir.** Bir proje Riskli veya Bloke olduğu için otomatik olarak Resource/Capacity kaynaklı risk tespit edildi sonucu üretilmez. Her Riskli/Bloke proje için capacity kontrolü yapılır ancak sonuç yalnızca **Risk Var / Risk Yok / UNKNOWN** olabilir ve mevcut verilerle kanıtlanmalıdır.

**Proje Sorumlusu ile Kritik Resource Ayrımı:** Proje sorumlusu delivery/accountability açısından gösterilir. Developer, QA, DevOps, Data Engineer vb. yalnızca gerçekten projeye atanmışsa veya ilgili aktif iş/dependency ile kaynaklardan doğrulanmış ilişkisi varsa Kritik Kaynak olarak gösterilebilir. Kaynak ilişkisi doğrulanamıyorsa kişiyi rapora ekleme.

**Allocation Yorumlaması:** Tarih aralığı bulunmayan allocation kayıtlarının toplamını eşzamanlı workload olarak kabul etme. %240 allocation gibi CALCULATED değeri gösterebilirsin ancak bundan "aşırı yüklü", "bu yükle işi çözemeyecek", "gecikmenin nedeni capacity" gibi sonuçlar çıkarma. Böyle bir sonuç için zaman çakışması veya başka doğrudan kapasite kanıtı gerekir; yoksa **UNKNOWN** veya "capacity katkısı doğrulanamadı" yaz.

**Root Cause Önceliklidir:** Blocker security approval, environment, dependency, vendor, technical issue vb. kaynaklıysa capacity'yi ana neden gibi sunma. Capacity yalnızca kanıt varsa **contributing factor** olarak gösterilebilir. Örneğin security approval ana blokaj ise açıkça: "Ana neden security approval dependency; resource capacity'nin gecikmeye katkısı doğrulanamadı."

**"Tek Yetkinlik Sahibi" İfadesi:** Yalnızca mevcut people/skill verisi bunu doğruluyorsa kullan. Daha güvenli ifade: "Mevcut ekip verilerinde aynı skill set'e sahip başka doğrulanmış kaynak bulunamadı." Şirket genelinde başka kimse yokmuş gibi yorum yapma.

**Riskli/Bloke Hiçbir Proje Analizden Kaybolmaz:** Her biri için **Project Risk → Root Cause → Resource/Capacity Check → Delivery Impact → Recommendation** değerlendirmesi yapılmalıdır. Capacity riski yoksa bunu açıkça göster ve gerçek root cause'u takip etmeye devam et.

**Kapasite/darboğaz riski tespit edilen HER önemli kişi için şu sabit formatta detaylı analiz (Başlık: \"Kritik Kaynak Analizi\"):**

```
Ad Soyad — Rol

Kapasite Durumu:
[Allocation toplamı, kaç projede, tarih aralığı yoksa eşzamanlılık varsayılmaz uyarısı]

Çalıştığı Projeler:
[Doğal proje adlarıyla; internal ID (PRJ-xxx) göstermez]

Neden:
[Kapasite riskinin temel nedeni: yüksek allocation, tek yetkinlik sahibi, aktif bloke/bağımlılık, çoklu kritik sorumluluk vb.]

Etkilenen İşler / Teslimatlar:
[İlgili proje doğal adları ve teslimat türleri (örn: migration cutover, production infra, test ortamı)]

Ana Neden:
[Bloke/gecikmenin asıl sebebi bu kişinin kapasitesi mi, yoksa güvenlik onayı / bağımlılık / teknik problem mi?]

Capacity Risk Sonucu:
[Risk Var / Risk Yok / UNKNOWN — mevcut grounding kurallarına göre belirlenir]

Alternatif Kaynak:
[Uygun aday varsa: "X (Rol) — Y yetkinliği var, Z projede allocation %, aktarımın diğer projelere etkisi değerlendirildi, [ilgili iş] için değerlendirilebilir." / Uygun aday yoksa: "Mevcut verilerle güvenli bir kaynak aktarımı doğrulanamadı. Gerekli yetkinlik (örn: Kubernetes, IAM, QA Automation) başka kişide yok."]

Öneri:
[Kaynak değişikliği root cause'u çözüyorsa: "X işinin Y kişisine aktarılması değerlendirilebilir (neden: ...)." / Çözmüyorsa: "Kaynak değişikliği ana problemi çözmez; [asıl neden: güvenlik onayı / bağımlılık / teknik blokaj vb.] bekleniyor." / Hiçbir atama onay olmadan değiştirilmez.]
```

**Arka planda analiz (raporda yukarıdaki formatta özetlenir, ham tablo yazılmaz):**
- Skill / allocation / aktif görevler / proje öncelikleri / dependency etkisi
- Alternatif çalışanların skill'leri, mevcut allocation'ları, aktif görevleri, diğer projelere etkisi
- Allocation kayıtlarında tarih aralığı yoksa toplamları kesin eşzamanlı yük olarak **sunma**
- "En boş kişi" otomatik "en uygun kişi" **değildir**
- Kaynak değişikliği root cause'u çözmüyorsa önerme
- Internal ID (IAM-xxx, PRJ-xxx, DAT-xxx, CLD-xxx, PAY-xxx, MOB-xxx, CSP-xxx, AIR-xxx, CRM-xxx, KPI-xxx, EMP-xxx) **göstermez**; ilgili işin doğal adını kullanır
- Kaynakta olmayan kesin tarih/kişi/yetki/sonuç uydurmaz ("bugün tamamlanmalı", "şu tarihe ertelenmeli", "kesin gecikecek" YASAK)

---

#### 4 — FİNANS & KPI

**Finans Tablosu (8 Proje):**

| Proje | Expected ROI (%) | CAPEX (TL) | OPEX (TL) | Approved Budget (TL) | Actual Cost (TL) | Budget Kullanımı (%) |
|---|---|---|---|---|---|---|
| [Proje Adı] | [Değer] | [Değer] | [Değer] | [Değer] | [Değer] | [Değer] |

*(Tüm 8 proje tabloya eklenir.)*

Yalnızca yönetici dikkati gerektiren finansal durumlar (bütçe kullanımı yüksek ve kritik işler devam ediyor, ROI düşük compliance-driven, vb.) yorumlanır. Kaynakta olmayan finansal yorum, eşik veya puanlama üretilmez.

**KPI:** Target ve Current değerlendirilir. KPI hedef yönü (yüksek/düşük iyi) kaynakta tanımlı değilse **her satıra "Belirlenemedi" YAZILMAZ**. Bu bölümde **bir kez** doğal dilde:

> "KPI ölçümleri mevcut ancak bazı KPI'ların hedef yönü kaynaklarda tanımlı olmadığı için başarı durumu güvenilir şekilde sınıflandırılamıyor."

Hedef yönü doğrulanabilen KPI varsa normal değerlendirilir.

---

#### 5 — YAKLAŞAN TESLİMATLAR (14 GÜN)

Analysis Date = çalıştırma gününün **güncel tarihi**.

Önümüzdeki 14 gün içindeki önemli milestone, SIT, UAT, Go-Live, Production tarihleri. Gecikmişler ve yaklaşanlar tablo halinde gösterilir.

| Proje | Milestone / Teknik İş | Hedef Tarih | Durum |
|---|---|---|---|
| [Proje Adı] | [Milestone veya teknik iş adı] | [YYYY-MM-DD] | [Gecikmiş / Bugün / Yaklaşıyor] |

Kalan gün = Teslim Tarihi - Analysis Date. Kaynak tarihleri değiştirilmez.

---

### KALICI ANALİZ KURALLARI

- 46 bilgi grubu rapora yazılmaz; **ANALİZDE** kullanılır.
- Risk varsa: **Risk → Neden → Etki → Çözüm** zinciri.
- Kaynak problemi ihtimali varsa: **Risk → Neden → Kapasite/Skill kontrolü → Alternatif kişi → Etki kontrolü → Öneri** zinciri tamamlanır.
- Bir projede problem arama zorunluluğu yok. Normal proje 🟢 kalabilir.
- **Risk ≠ Issue**: Risk = gelecekteki belirsizlik, Issue = mevcut problem.
- Yüksek allocation → performans hatası **DEĞİL**.
- Bağımlılık tek başına risk **DEĞİL**.
- KPI hedef uzaklığı geliştirme aşamasında tek başına başarısızlık **DEĞİL**.
- Yüksek bütçe tüketimi tek başına finansal risk **DEĞİL**.
- FACT/CALCULATED/INFERENCE/UNKNOWN arka planda; raporda **gösterilmez**.
- Gerekli veri ana kaynakta yoksa → sadece önceden tanımlı kurumsal kaynaklar kontrol edilir. Dış sistem/internet varsayımı yok. Doğrulanamazsa doğal Türkçe ile belirtilir.
- **Human Approval**: Agent analiz/öneri üretir; atama/tarih/scope/priority/risk kapatma/veri değişikliği **kullanıcı açık onayı ("Onaylıyorum", "uygula", "evet") ALMADAN YAPILMAZ**. Öneri ile uygulama kesin ayrılır.

---

### RAPOR TAMAMLANMA KRİTERİ

Varsayılan rapor **kısa ve taranabilir**. Ama "kısa" = analiz eksikliği **değil**. Tüm analiz arka planda; yöneticiye sadece karar için sonuç.

Bir TPM 30–60 saniyede şunların cevabını almalı:
1. Portföy genel nasıl?
2. Hangi proje yolunda/sorunlu?
3. Her proje hangi aşamada?
4. Sorun ne?
5. Kim sorumlu?
6. Neden sorun?
7. Ne yapmalı?
8. Kaynak darboğazı kim/neden?
9. Başka kişiye güvenli aktarım mümkün mü?
10. Finans/KPI önemli durum var mı?
11. Yaklaşan/geciken teslimatlar neler?

Bu cevaplanmıyorsa rapor tamamlanmamış sayılır.

---

## 4. Kullanım

Bu skill `auto_load: true` olduğu için her oturumda otomatik yüklenir.  
Risk analizi çalıştırıldığında bu kurallar **varsayılan** olarak uygulanır.  
Kullanıcı her seferinde politikayı tekrar **vermek zorunda kalmaz**.

## 8. ANALİS TARİHİ (ANALYSIS DATE) KURALI

**Tüm tarih bazlı hesaplamalarda** (kalan gün, deadline yaklaşımı, milestone gecikmesi, SLA süreleri, vb.) **sabit/tahmini tarih KULLANILMAZ**.

**Analysis Date** = Analizin çalıştırıldığı günün **güncel tarihi** (sistem saati / kullanıcı ortamı).

**Kaynak Veri Tarihleri (değiştirilmez, verinin güncellik tarihi olarak kabul edilir):**
- `Measurement_Date` (KPI ölçüm tarihi)
- `Financial_Data_As_Of` (Mali veri tarihi)
- `Status_Changed_Date` (Jira durum değişim tarihi)
- `Created_Date`, `Updated_Date`, `Due_Date` (Jira tarihleri)
- `Start_Date`, `Deadline_Date`, `Milestone_Due_Date` (Proje plan tarihleri)

**Kullanım:**
- `Kalan Gün = Deadline_Date (veya Milestone_Due_Date) - Analysis Date`
- `Gecikme = Analysis Date - Due_Date` (pozitifse gecikmiş)
- `Veri Yaşı = Analysis Date - Measurement_Date` (veri ne kadar eski)

**Analysis Date güvenilir belirlenemiyorsa:**
- **Tarih bazlı hiçbir sonuç ÜRETİLMEZ**
- Kullanıcıya: *"Analiz tarihi güvenilir belirlenemediği için tarih bazlı hesaplamalar (kalan gün, gecikme, vb.) yapılamadı. Bu bölüm atlandı."*
- Sadece tarih bağımsız bulgular raporlanır.

> Bu kural, portföy raporu, proje bazlı analiz, risk motoru çıktısı — **tüm** tarih bazlı çıktılara geçerlidir.
