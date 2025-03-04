import socket

def get_ip_address(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} IP adresi: {ip}")
        print("\nKod @furkan.1903a tarafından yapıldı!")
    except socket.gaierror:
        print("Geçersiz domain veya bağlantı hatası.")

# Kullanıcıdan domain al
domain = input("IP adresini öğrenmek istediğiniz siteyi girin: ")
get_ip_address(domain)
