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
