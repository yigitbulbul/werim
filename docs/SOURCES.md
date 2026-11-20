# Kaynaklar

Her kaynak için: ne, nereden (link), ne zaman indirildi, lisans.

## Veri
- TÜİK bitkisel üretim istatistikleri, ilçe bazında: https://biruni.tuik.gov.tr/medas/
  - İndirildi 2026-11-18 (Yiğit). Dosya: `data/raw/tuik_aycicegi_ilce.xls` (git'te yok).
  - Seçim yolu: Konu "Bitkisel Üretim İstatistikleri" → Ölçüm "Tahıllar ve diğer bitkisel ürünler" → Ürün "[01.11.95.00.01] Ayçiçeği Tohumu (Yağlık)" → Ürün niteliği ve ölçü birimi: hepsi (ekilen alan, hasat edilen alan, verim, üretim miktarı) → Zaman 2017–2025 → Düzey: ilçe, Tekirdağ + Kırklareli + Edirne (28 ilçe; Ergene ve Kapaklı ayrı).
  - İçerik (2026-11-20): 4 blok alt alta (ekilen alan da, hasat edilen alan da, verim kg/da, üretim ton), her biri 2017–2025. 28 değil 27 ilçe sütunu var: Kırklareli Demirköy yok. Neden (ekim olmaması?) doğrulanmadı; TÜİK'te tek başına kontrol edilecek.
- Sentinel-2 L2A (Google Earth Engine): COPERNICUS/S2_SR_HARMONIZED
- ERA5-Land (Google Earth Engine): ECMWF/ERA5_LAND/DAILY_AGGR
- ESA WorldCover (Google Earth Engine): ESA/WorldCover/v200

## Literatür
- NASA Harvest haberi: Ukrayna ayçiçeği ekili alan haritası, radar uydularıyla 20 m çözünürlükte (2024). https://www.nasaharvest.org/news/first-its-kind-high-resolution-map-ukrainian-sunflower-cropland-allows-new-estimates. Yiğit buldu, 2026-11-15.
  - Asıl makale: https://www.sciencedirect.com/science/article/pii/S2666017224000233 (ScienceDirect otomatik erişimi engelledi; tam metin henüz okunmadı).
- NASA Harvest haberi: "Mapping the World's Sunflowers". https://www.nasaharvest.org/news/mapping-worlds-sunflowers. Okundu 2026-11-15. Doğrulanan bilgiler:
  - Sentinel-1 (ESA) SAR radar verisi kullanılıyor.
  - Olgun ayçiçeği tablası kalıcı olarak doğuya bakar. Radar yansıması inen ve çıkan geçişlerde öngörülebilir biçimde farklılaşır, mısırda bu fark yok. Model ayçiçeğini buradan ayırt ediyor.
  - Model Ukrayna 2022 saha verisiyle eğitildi. Ukrayna 2018–2020, Macaristan, Fransa, Rusya ve ABD 2018'de yüksek doğrulukla test edildi.
  - Makale: Qadir, A. vd., "A generalized model for mapping sunflower areas using Sentinel-1 SAR data", Remote Sensing of Environment (haberde açık erişim deniyor). Künye (yıl, cilt, DOI) makaleden doğrulanacak.

## Tasarım ilhamı
- https://onesoil.ai/en
- https://www.tema.org.tr/
- https://www.doktar.com/tr/
