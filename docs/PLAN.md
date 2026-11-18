# Program (TÜBİTAK 2204-A)

Son başvuru: 4 Ocak 2027, 17:30. İç hedef: 2 Ocak'ta gönderilmiş olması.

Hedef sonuç ("vay" grafiği, karar 2026-11-18): Kurak bir yılda ilçe ortalaması verimi fazla tahmin ederken Werim'in düşüşü Haziran sonundan yakaladığını gösteren grafik. Kurak yıl(lar) varsayılmaz, veriden (ERA5 yağışı ve TÜİK verimi) belirlenir. Grafik bunu göstermezse, göstermediği dürüstçe raporlanır.

## Tatil sonu (18–22 Kasım): Tekirdağ
| Gün | İş | Bitti sayılır |
|---|---|---|
| Çar 18 | TÜİK dosyasını pandas ile aç ve temizle | `data/processed/tuik_yield.csv`, 28 ilçe × 9 yıl |
| Per 19 | İlçe sınırı verisini seç ve Earth Engine'e yükle | 28 ilçe eşleşiyor (Ergene ve Kapaklı dahil) |
| Cum 20 | Bulut ve tarım alanı maskesi. Kontrol: 2017–2018 için S2 L2A var mı? | Bir ilçe, bir yıl için Temmuz NDVI'ı |
| Cmt 21 – Paz 22 | 11 ilçe × 9 yıl NDVI | Tekirdağ NDVI tablosu |
| Paz 22 (son iş) | İlk bakış: Tekirdağ Temmuz NDVI ve verim saçılım grafiği (99 nokta). Sonuç değil, yön kontrolü. | Grafik `notebooks/` içinde |

## Okul dönemi 1 (23 Kasım – 6 Aralık): Tek tablo
- 23–29 Kasım: Kırklareli NDVI (8 ilçe); ERA5-Land Nisan–Temmuz yağış ve sıcaklık.
- 30 Kasım – 6 Aralık: `data/processed/dataset.csv` (ilçe-yıl satırları). Edirne ayrı işaretli. Kurak yıl adaylarını veriden belirle.
- 6 Aralık civarı: danışman öğretmenle 10 dakikalık ara kontrol.

## Okul dönemi 2 (7–20 Aralık): Model
- 7–13 Aralık: Baseline'lar (önceki yıl, ilçe ortalaması). Doğrusal regresyon, leave-one-year-out, MAE ve MAPE.
- 14–20 Aralık: Gerekirse random forest. 3 grafik:
  1. Tahmin ve gerçek verim
  2. Yıl yıl hata: model ve iki baseline
  3. Kuraklık yılı: o yıl için ilçe ortalaması tahmini, Werim tahmini ve gerçek verim ("vay" grafiği)

## Rapor (21 Aralık – 2 Ocak)
- 21–27 Aralık: Türkçe rapor taslağı (TÜBİTAK formatı)
- 28–31 Aralık: Danışman kontrolü ve düzeltmeler
- 2 Ocak: Gönderim
- 3–4 Ocak: Tampon

## Açık noktalar
- Yiğit'in Aralık sınav haftası? Öğrenince yük kaydırılacak.
