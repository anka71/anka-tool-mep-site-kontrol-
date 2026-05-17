import os
import time
import requests
from urllib.parse import urlparse
from pyfiglet import Figlet
from colorama import Fore, Style, init

init(autoreset=True)

# Phoenix Açılışı
phoenix = f"""
{Fore.RED}
                 (  .      )
             )           (              )
                   .  '   .   '  .  '  .
          (    , )       (.   )  (   ',
           .' ) ( . )    ,  ( ,     )   ( .
        ). , ( .   (  ) ( , ')  .' (  ,    )
       (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                 PHOENIX SYSTEM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

os.system("clear")
print(phoenix)
time.sleep(2)

# Başlık
os.system("clear")
fig = Figlet(font='slant')
print(Fore.RED + fig.renderText('ANKA TOOL'))


def kontrol_et(url):
    print(Fore.YELLOW + "\n[+] Site kontrol ediliyor...\n")

    if not url.startswith("http"):
        url = "https://" + url

    parsed = urlparse(url)
    domain = parsed.netloc

    supheli = [
        "login-free",
        "secure-login",
        "verify",
        "free-mep",
        "fake"
    ]

    puan = 0

    # HTTPS kontrolü
    if url.startswith("https://"):
        print(Fore.GREEN + "[✓] HTTPS kullanılıyor")
        puan += 1
    else:
        print(Fore.RED + "[!] HTTPS kullanılmıyor")

    # Şüpheli kelime kontrolü
    for kelime in supheli:
        if kelime in domain:
            print(Fore.RED + f"[!] Şüpheli domain kelimesi bulundu: {kelime}")
            puan -= 2

    # IP kontrolü
    if any(char.isdigit() for char in domain):
        print(Fore.YELLOW + "[!] Domain içinde sayı/IP benzeri yapı bulundu")
        puan -= 1

    try:
        r = requests.get(url, timeout=5)

        print(Fore.CYAN + f"\n[+] HTTP Durum Kodu: {r.status_code}")

        headers = r.headers

        if "Content-Security-Policy" in headers:
            print(Fore.GREEN + "[✓] CSP güvenlik başlığı mevcut")
            puan += 1
        else:
            print(Fore.YELLOW + "[!] CSP güvenlik başlığı yok")

        if "X-Frame-Options" in headers:
            print(Fore.GREEN + "[✓] X-Frame-Options mevcut")
            puan += 1
        else:
            print(Fore.YELLOW + "[!] X-Frame-Options yok")

    except Exception as e:
        print(Fore.RED + f"[!] Siteye bağlanılamadı: {e}")
        return

    print(Fore.MAGENTA + "\n========== SONUÇ ==========")

    if puan >= 2:
        print(Fore.GREEN + "[✓] Site temel kontrollerde güvenli görünüyor")
    elif puan >= 0:
        print(Fore.YELLOW + "[!] Site dikkatli kullanılmalı")
    else:
        print(Fore.RED + "[X] Site şüpheli görünüyor")


while True:
    print(Fore.RED + """

1 > 01 : MEP siteyi kontrol et
2 > 02 : Çıkış
3 > 03 : Rehberlik
""")

    secim = input(Fore.WHITE + "Numara yazınız: ")

    if secim == "1" or secim == "01":
        hedef = input(Fore.CYAN + "\nKontrol edilecek siteyi gir: ")
        kontrol_et(hedef)

    elif secim == "2" or secim == "02":
        print(Fore.RED + "\nANKA TOOL kapatılıyor...")
        time.sleep(1)
        break

    elif secim == "3" or secim == "03":
        print(Fore.YELLOW + """

[REHBERLIK]
- HTTPS olmayan sitelere dikkat et
- Şifreni her sitede kullanma
- Resmi MEB adreslerini kontrol et
- Garip domain uzantılarına dikkat et
- Bilgilerini paylaşmadan önce URL'yi doğrula

""")

    else:
        print(Fore.RED + "[!] Geçersiz seçim")
