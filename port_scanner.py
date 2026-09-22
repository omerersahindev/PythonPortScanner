import socket
import sys
from datetime import datetime

# Hedef IP veya Alan Adı
target_host = input("Taranacak Hedef IP veya Domain (ör: scanme.nmap.org): ")

try:
    target_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print("\n[!] Domain çözümlenemedi.")
    sys.exit()

print("-" * 50)
print(f"Hedef Taranıyor: {target_ip}")
print(f"Tarama Başlangıcı: {str(datetime.now())}")
print("-" * 50)

# Yaygın Portlar Listesi
ports_to_scan = [21, 22, 80, 443, 8080, 3306]

try:
    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port}: AÇIK")
        else:
            print(f"[-] Port {port}: Kapalı")
        s.close()

except KeyboardInterrupt:
    print("\n[!] Tarama kullanıcı tarafından iptal edildi.")
    sys.exit()

except socket.error:
    print("\n[!] Sunucuya bağlanılamadı.")
    sys.exit()