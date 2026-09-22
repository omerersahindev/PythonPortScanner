# 🔍 Python Port Scanner

Bu proje, belirlenmiş bir hedef IP adresi veya domain üzerindeki yaygın TCP portlarının (HTTP, HTTPS, SSH, MySQL vb.) açık olup olmadığını tarayan hafif bir Python aracıdır.

---

## 🛠️ Özellikler
- **Socket Programlama:** `socket` kütüphanesi kullanarak hızlı TCP bağlantı testleri gerçekleştirir.
- **Domain Çözümleme:** Verilen web adreslerinin (ör. `scanme.nmap.org`) IP karşılığını otomatik bulur.
- **Zamanaşımı Kontrolü:** Yanıt vermeyen portlarda takılmaması için zaman aşımı (timeout) mekanizması barındırır.

---

## 🚀 Kullanım

1. Bu depoyu klonlayın veya `port_scanner.py` dosyasını indirin.
2. Terminal veya Komut İstemi (CMD) üzerinden çalıştırın:

```bash
python port_scanner.py
