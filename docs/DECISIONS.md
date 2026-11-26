# Kararlar

| Tarih | Karar | Neden |
|---|---|---|
| 2026-11-13 | Tanıtım sitesi ve logo TÜBİTAK takviminin dışında, tek oturumluk iş olarak yapılacak. | Tek öncelik TÜBİTAK 2204-A; site araştırma günlerini yememeli. |
| 2026-11-13 | Sitede uydurma rakam yok; araştırma sorusu ve gerçek veri kaynakları gösterilecek. | Henüz kullanıcı ya da sonuç yok; kural 5. |
| 2026-11-15 | Logo ürün bağımsız (ayçiçeği odaklı değil), global bir işaret olacak. Son seçim yurt dışı danışman öğretmeniyle yapılacak. | Werim ileride başka ürün ve bölgelere açılabilir. |
| 2026-11-15 | Python 3.14 kullanılacak (macOS'un 3.9.6'sı yerine); python.org universal2 yükleyicisiyle kurulacak. | Mac Intel işlemcili, Homebrew desteklemiyor. 3.15 çok yeni (kütüphaneler hazır değil), 3.12 artık yükleyici almıyor. |
| 2026-11-15 | werim reposu public kalacak (Yiğit'in yurt dışı danışman öğretmeninin kararı; okuldaki TÜBİTAK proje hocası ayrı kişi). | Commit geçmişi işin adım adım Yiğit tarafından yapıldığını gösterir. Veri ve kimlik bilgileri zaten .gitignore ile dışarıda. Her commit öncesi `git status` kontrol edilecek. |
| 2026-11-15 | CLAUDE.md repodan ve git geçmişinden çıkarıldı, .gitignore'a eklendi. Sadece yerelde duruyor. | Kişisel bilgi içeriyor; repo public. |
| 2026-11-15 | Earth Engine: `werim-514813` projesi, noncommercial (academic), Community tier. Kayıt 15 Mayıs 2028'e kadar geçerli. | Ücretsiz ve kart gerektirmiyor. İş yükü küçük, 150 EECU-saat muhtemelen yeter. |
| 2026-11-18 | `requirements.txt` içinde `cryptography<49` sabitlendi. | cryptography 49 ve sonrası Intel Mac için hazır paket (wheel) yayınlamıyor; pip kaynak koddan derlemeye çalışıyor ve Rust olmadığı için hata veriyor. 48.0.1'in Intel Mac paketi var. `==48.0.1` yerine `<49`: 48.x güvenlik yamaları gelirse alınabilsin. |
| 2026-11-18 | Hedef "vay" sonucu: kuraklık yılı grafiği (ilçe ortalaması, Werim tahmini ve gerçek verim). Raporun 3 grafiğinden biri olacak. Program `docs/PLAN.md`'de. | Ortalama verim baseline'ı normal yıllarda güçlü olabilir; uydu verisinin asıl değeri olağan dışı yıllarda görülür. Kurak yıllar veriden belirlenecek, varsayılmayacak. |
| 2026-11-25 | Araştırma işi (kod, veri, Earth Engine) Windows PC'de yerel olarak yürütülecek. Mac'teki Claude oturumu haftalık "ortaklar toplantısı" için kullanılacak: takvim, kapsam ve "vay" sonucu kontrolü. Toplantıdan önce Mac'te `git pull` yapılır, Claude LOG.md'yi okur. | Mac yavaş. Bulut oturumu CLAUDE.md, TÜİK dosyası ve Earth Engine girişini göremez; kimlik bilgileri buluta konmayacak. |
