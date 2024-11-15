import socket
import time
import threading
from ipaddress import ip_address
from collections import defaultdict

# IP Adresinizi buraya girin
YOUR_IP_ADDRESS = "192.168.1.1"  # Örnek IP, kendi IP adresinizi buraya girin

# Global Kara Liste ve Trafik İstatistikleri
blacklist = set()
traffic_data = defaultdict(lambda: {'count': 0, 'size': 0})  # Kaydetmek için bir sözlük

# Paket Dinleyici (Packet Sniffer)
def start_sniffer():
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sniffer.bind((YOUR_IP_ADDRESS, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    return sniffer

# IP Engelleme Fonksiyonu
def block_ip(ip):
    blacklist.add(ip)
    print(f"IP Engellendi: {ip}")

# DDoS Saldırısı Tespiti
def detect_ddos(source_ip, packet_size, threshold_count=1000, threshold_size=1000000):
    """Anormal DDoS saldırısı tespiti: Hem paket sayısı hem de toplam paket boyutu"""
    traffic_data[source_ip]['count'] += 1
    traffic_data[source_ip]['size'] += packet_size

    # Eğer belirli bir süreyi geçtiyse, istatistikleri sıfırla
    current_time = time.time()
    if traffic_data[source_ip]['count'] > threshold_count or traffic_data[source_ip]['size'] > threshold_size:
        print(f"!!! DDoS saldırısı tespit edildi: {source_ip} !!!")
        block_ip(source_ip)
        traffic_data[source_ip] = {'count': 0, 'size': 0}  # Engellenen IP'nin verilerini sıfırla

# Saldırı İzleme ve Engelleme Fonksiyonu
def monitor_and_block():
    sniffer = start_sniffer()
    
    while True:
        packet, _ = sniffer.recvfrom(65565)  # 65,535 bayta kadar paket al
        
        ip_header = packet[14:34]
        source_ip = '.'.join(map(str, ip_header[12:16]))  # IP adresini al
        packet_size = len(packet)
        
        if ip_address(source_ip) not in blacklist:
            # DDoS tespiti yap
            detect_ddos(source_ip, packet_size)
        else:
            print(f"Engellenen IP'den gelen paket: {source_ip}")
            
# İstatistik ve Kara Listeyi Logla
def log_traffic_stats():
    while True:
        time.sleep(60)  # Her dakika bir istatistik kaydı
        print(f"\n--- Kara Liste ---")
        for ip in blacklist:
            print(f"Engellenmiş IP: {ip}")
        print(f"\n--- Trafik İstatistikleri ---")
        for ip, stats in traffic_data.items():
            print(f"IP: {ip} - Paket Sayısı: {stats['count']} - Toplam Paket Boyutu: {stats['size']} bytes")

# Başlangıç Fonksiyonu
def start_monitoring():
    # Trafik loglamayı arka planda başlat
    threading.Thread(target=log_traffic_stats, daemon=True).start()

    # Ağ trafiğini izle ve engelleme işlemini başlat
    monitor_and_block()

if __name__ == "__main__":
    start_monitoring()
Rapor
'drose
'drose
Moderasyon Tim Lideri



7 Tem 2013
8,924
1,316
Bugün 19:48
Yeri işaretle
#7
Paylaşım Kuralları
Paylaşım Kuralları Yapılan uygulamalar THT misyonuna ve forum kurallarına karşı herhangi bir faaliyeti olmamalıdır. Alttaki şablona uygun açılmayan konular kategoride tutulmayacaktır. Yazılım /proje ismi Yazılım/proje'nin Github sayfası Yazılım/proje hakkında açıklamalar Ekran görüntüleri
www.turkhackteam.org www.turkhackteam.org
Rapor
Buraya yanıt vermek için yeterli yetkiniz yok.
Paylaş:
Facebook
Twitter
Telegram
Reddit
E-posta
Link

 Çöp Tenekesi ÇÖP 
TurkHackTeam
Sitemizde yer alan içerikler hakkındaki şikayetlerinizi bilgi [at] turkhackteam.org mail adresimize bildirebilirsiniz. Please Report Abuse, DMCA, Scamming, Harassment, Crack or any Illegal Activities to bilgi [at] turkhackteam.org

Bağlantılar
KVKK
Gizlilik
Hakkımızda
Reklam verin
İletişim
Bağlantılar
İhbar
Misyon
Siber güvenlik
Yardım merkezi
Neler yeni
Yeni mesajlar
Yeni profil mesajları
Haber akışınız
Son aktivite
Sosyal medya sayfalarımız
Facebook
Twitter
Telegram
Reddit
E-posta
Link
import socket
import time
import threading
from ipaddress import ip_address
from collections import defaultdict

# IP Adresinizi buraya girin
YOUR_IP_ADDRESS = "192.168.1.1"  # Örnek IP, kendi IP adresinizi buraya girin

# Global Kara Liste ve Trafik İstatistikleri
blacklist = set()
traffic_data = defaultdict(lambda: {'count': 0, 'size': 0})  # Kaydetmek için bir sözlük

# Paket Dinleyici (Packet Sniffer)
def start_sniffer():
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sniffer.bind((YOUR_IP_ADDRESS, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    return sniffer

# IP Engelleme Fonksiyonu
def block_ip(ip):
    blacklist.add(ip)
    print(f"IP Engellendi: {ip}")

# DDoS Saldırısı Tespiti
def detect_ddos(source_ip, packet_size, threshold_count=1000, threshold_size=1000000):
    """Anormal DDoS saldırısı tespiti: Hem paket sayısı hem de toplam paket boyutu"""
    traffic_data[source_ip]['count'] += 1
    traffic_data[source_ip]['size'] += packet_size

    # Eğer belirli bir süreyi geçtiyse, istatistikleri sıfırla
    current_time = time.time()
    if traffic_data[source_ip]['count'] > threshold_count or traffic_data[source_ip]['size'] > threshold_size:
        print(f"!!! DDoS saldırısı tespit edildi: {source_ip} !!!")
        block_ip(source_ip)
        traffic_data[source_ip] = {'count': 0, 'size': 0}  # Engellenen IP'nin verilerini sıfırla

# Saldırı İzleme ve Engelleme Fonksiyonu
def monitor_and_block():
    sniffer = start_sniffer()
    
    while True:
        packet, _ = sniffer.recvfrom(65565)  # 65,535 bayta kadar paket al
        
        ip_header = packet[14:34]
        source_ip = '.'.join(map(str, ip_header[12:16]))  # IP adresini al
        packet_size = len(packet)
        
        if ip_address(source_ip) not in blacklist:
            # DDoS tespiti yap
            detect_ddos(source_ip, packet_size)
        else:
            print(f"Engellenen IP'den gelen paket: {source_ip}")
            
# İstatistik ve Kara Listeyi Logla
def log_traffic_stats():
    while True:
        time.sleep(60)  # Her dakika bir istatistik kaydı
        print(f"\n--- Kara Liste ---")
        for ip in blacklist:
            print(f"Engellenmiş IP: {ip}")
        print(f"\n--- Trafik İstatistikleri ---")
        for ip, stats in traffic_data.items():
            print(f"IP: {ip} - Paket Sayısı: {stats['count']} - Toplam Paket Boyutu: {stats['size']} bytes")

# Başlangıç Fonksiyonu
def start_monitoring():
    # Trafik loglamayı arka planda başlat
    threading.Thread(target=log_traffic_stats, daemon=True).start()

    # Ağ trafiğini izle ve engelleme işlemini başlat
    monitor_and_block()

if __name__ == "__main__":
    start_monitoring()
