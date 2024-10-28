import json
import requests,json,sys,time
from fake_useragent import UserAgent
from colorama import Fore, Style, init
from datetime import datetime


class Ff:
    def ll(js):
        try:
            print(json.dumps(js, indent=4))  
        except Exception as e :
            print(js)
        
    def countdown(total_seconds):
        for remaining in range(total_seconds, 0, -1):
            # Menghitung jam, menit, dan detik tersisa
            hrs, mins, secs = remaining // 3600, (remaining % 3600) // 60, remaining % 60
            # Format string waktu
            timer = f"{hrs:02}:{mins:02}:{secs:02}"
            
            # Menampilkan timer tanpa berpindah baris
            sys.stdout.write('\r' + timer)  # Menggunakan '\r' untuk kembali ke awal baris
            sys.stdout.flush()  # Memastikan output ditampilkan
            time.sleep(1)  # Tunggu 1 detik

        print("\nCountdown selesai!")

class Output:
    def __init__(self):
        # Inisialisasi Colorama
        init(autoreset=True)
    
    def get_current_time(self):
        return datetime.now().strftime("[%d/%m/%Y %H:%M]")  # Mengembalikan waktu saat ini

    def warning(self, message):
        print(f"{Fore.WHITE} {self.get_current_time()} {Fore.YELLOW} {message} {Style.RESET_ALL}")
        
    def success(self, message):
        print(f"{Fore.WHITE} {self.get_current_time()} {Fore.GREEN} {message} {Style.RESET_ALL}")
    
    def danger(self, message):
        print(f"{Fore.WHITE} {self.get_current_time()} {Fore.RED} {message} {Style.RESET_ALL}")
        
    def banner(self):
        banner=f"""
                {Fore.WHITE}
                @@@@@@   @@@@@@@@   @@@@@@@@     @@@@@@   
                @@@@@@@@  @@@@@@@@  @@@@@@@@@@  @@@@@@@@  
                @@!  @@@  @@!       @@!   @@@@  @@!  @@@  
                !@!  @!@  !@!       !@!  @!@!@  !@!  @!@  
                @!@!@!@!  @!!!:!    @!@ @! !@!  !!@!!@!!  
                !!!@!!!!  !!!!!:    !@!!!  !!!    !!@!!!  
                !!:  !!!  !!:       !!:!   !!!       !!!  
                :!:  !:!  :!:       :!:    !:!       !:!  
                ::   :::   ::       ::::::: ::  ::::: ::  
                :    : :   :        : : :  :    : :  : .
                                                        
                  {Fore.YELLOW} 🦋 https://t.me/AIRDORP_AUTOBOT 🦋
                bisa request bot jika garapan berpotensi
                {Style.RESET_ALL}
             """
        print(banner)
        
