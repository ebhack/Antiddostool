 İstatistik ve Kara Listeyi Logla
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
