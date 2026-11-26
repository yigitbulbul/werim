# Claude'un yaptıkları

Jüri "bunu sen mi yaptın" diye sorarsa: Claude'un katkıları burada, Yiğit'in kendi çalışması LOG.md'de.

## 2026-11-13
- OneSoil, TEMA ve Doktar sitelerini inceleyip renk, font ve içerik yapısını özetledi.
- Logo ve ikon eskizleri çizdi (henüz seçilmedi).

## 2026-11-15
- Klasör yapısını oluşturdu.
- README.md, .gitignore, requirements.txt, CLAUDE.md ve docs/ dosyalarını yazdı.
- İlk commit'i attı.
- Okuldaki TÜBİTAK proje hocası için TÜBİTAK 2204-A proje özetini (Türkçe, tek sayfa) taslak olarak yazdı: https://claude.ai/artifact/8s1TWvLz4F5o6o9D7xNfAn. İçerik CLAUDE.md'deki proje tanımından derlendi, yeni veri ya da sonuç eklenmedi.
- Araştırma kodu: henüz yok (kural 2: araştırma kodunu Yiğit yazar).

## 2026-11-18
- venv kurulumunu adım adım anlattı; Yiğit komutları kendisi çalıştırdı.
- cryptography kurulum hatasının sebebini buldu (49+ sürümlerinde Intel Mac paketi yok) ve `cryptography<49` sabitlemesini önerdi; satırı Yiğit ekledi. DECISIONS.md kaydını Claude yazdı.
- SSL sertifika hatası için python.org'un resmi `Install Certificates.command` çözümünü gösterdi.
- `src/check_ee.py`: kodu Yiğit yazdı. Claude planı ve ipuçlarını verdi, `ee.Initialize(project=...)` satırını hazır verdi, satır 3–4'teki eksik değişken atamasını açıkladı; çift nokta hatasını Yiğit kendisi buldu.
- Commit öncesi gizli bilgi kontrolünü yaptı. Commit ve push'u Yiğit VS Code'dan yaptı (2cef5e9).
- Bu günün LOG.md girişini taslak olarak yazdı.
- docs/PLAN.md programını yazdı (Yiğit'in onayıyla). Kuraklık yılı grafiği hedefi Yiğit'le birlikte seçildi. SOURCES.md'ye TÜİK indirme yolunu ekledi.

## 2026-11-20
- `clean_tuik.py`: kodu Yiğit yazdı; Claude `read_excel` satırını ve inceleme için `iloc`/`dropna` satırlarını örnek olarak verdi.
- Terminal çıktısı okunaksız olunca dosya yapısını Claude çalıştırıp özetledi (4 blok, 27 ilçe). Eksik ilçeyi (Demirköy) Yiğit ipucuyla aradı; nedeni hakkındaki açıklama Claude'un doğrulanmamış tahmini.
- Okuldaki TÜBİTAK proje hocasına cevap mesajlarını Yiğit'in üslubuyla taslak olarak yazdı.

## 2026-11-26
- `clean_tuik.py`: kodu Yiğit yazdı. Claude `melt`, `rename`/`astype`, regex deseni `(.+)\((.+)\)-(\d+)`, `merge` ve sağlama formülü için örnek satırlar verdi; fonksiyona dönüştürmeyi adım adım anlattı. Sıralama hatalarını ve parametresiz fonksiyon hatasını Yiğit ipucuyla düzeltti.
- Claude, TÜİK verisinin tutarlılığını ayrıca kontrol etti (en büyük fark < 0.5 kg/da, harvested > sown satırı yok).
- İlçe sınırı kaynaklarını Earth Engine'de sorgulayarak karşılaştırdı (GAUL 2015 ve geoBoundaries); `?` karakterinin gerçek soru işareti olduğunu ve Türkiye'de iki "Saray" olduğunu kontrol etti.
- `check_boundaries.py` ve `match_districts.py`: kodu Yiğit yazdı; Claude iskelet ve ipuçları verdi, `to_gb_name` içindeki iki düzeltme satırını (merkez eki, 5 harfin `?` olması) hazır verdi.
- Yiğit'in isteğiyle WPILib VS Code ayarlarında Auto Save'i açtı (repo dışı).
- `match_districts.py` karşılaştırma ve kaydetme kısmı: Yiğit yazdı, Claude `iterrows`, `isin`, `~` örneklerini verdi.
- `ndvi_one.py`: ilk sürümü Yiğit Claude'un verdiği parçalarla yazdı (bulut maskesi, NDVI, medyan, WorldCover maskesi, orman testi). Fonksiyona dönüştürme (`july_ndvi`) Yiğit'in isteğiyle Claude tarafından yapıldı: Yiğit'in satırları yeniden sıralandı ve parametreleştirildi, yeni mantık eklenmedi; Yiğit kapsam sorusunu doğru cevapladı.
- Görüntü sayılarını (karo 35TNF, tarihler, 2017–2019) Claude ayrıca sorguladı. PLAN.md'yi 20 Aralık rapor tarihine göre Claude güncelledi (Yiğit onayıyla). GençBizzTech sitesini okuyup özetledi, IDEAS.md'ye not düştü.
