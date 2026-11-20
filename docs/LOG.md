# Günlük ilerleme

## 2026-11-20
- 19 Kasım çalışılamadı (baş ağrısı); program iki gün geride.
- `python-calamine` requirements.txt'e eklendi ve kuruldu (önce dosya kaydedilmediği için kurulmamıştı).
- `src/clean_tuik.py`: TÜİK dosyası pandas ile ham haliyle okundu (40 × 30). Yapı çözüldü: 4 ölçüm bloğu alt alta, yıl sütunu, ilçe adları `İl(İlçe)-kod` biçiminde.
- Bulgu: 28 ilçe seçildi, dosyada 27 var. Eksik: Kırklareli Demirköy (Bulgaristan sınırı, orman). Neden doğrulanmadı.
- Öğrenilen: `import pandas as pd`; göreli dosya yolu terminalin bulunduğu klasöre göredir; sayıya bakmadan önce etiketine ve birimine bak.

## 2026-11-18
- VS Code'da venv kuruldu, paketler yüklendi (earthengine-api 1.7.53, pandas 3.1.1).
- İki kurulum hatası çözüldü: cryptography 49+ Intel Mac paketi yok, `cryptography<49` sabitlendi (bkz. DECISIONS.md); python.org Python'unun SSL sertifikaları `Install Certificates.command` ile kuruldu.
- `earthengine authenticate` yapıldı. Token repo dışında (`~/.config/earthengine/`).
- İlk araştırma kodu: `src/check_ee.py` (Yiğit yazdı). Tekirdağ (27.51, 40.98) üzerinden Temmuz 2025'teki ilk Sentinel-2 görüntüsünün tarihi: 2025-07-02.
- Öğrenilen: Earth Engine'de kod bir tarif oluşturur, hesap `getInfo()` ile Google sunucusunda yapılır; büyük görüntüler indirilmez.

## 2026-11-15
- Profil: Python temel sözdizimine aşina (Java sayesinde), git push/pull mantığını biliyor, Earth Engine hesabı yok.
- Salıya (17 Kasım) kadar az zaman var.
- Repo kuruldu: klasörler, README, .gitignore, requirements.txt, CLAUDE.md, docs.
- Earth Engine hesabı açıldı ve noncommercial kayıt tamamlandı (proje `werim-514813`, Community tier).
- Mac Intel çıktı; Homebrew yerine Python python.org'dan kurulacak.

## 2026-11-13
- Proje talimatı hazırlandı.
- Tasarım ilhamı için OneSoil, TEMA ve Doktar siteleri incelendi; logo eskizleri çıkarıldı.
