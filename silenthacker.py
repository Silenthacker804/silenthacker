import os
import random
import threading
import time
import string

try:
    import requests
    from datetime import datetime
    from user_agent import generate_user_agent
except ModuleNotFoundError:
    os.system('pip install user-agent')
    os.system('pip install requests')

cls = lambda : os.system('cls' if os.name == 'nt' else 'clear')
# ----------------[ ColoRs ]-----
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
F = '\033[2;32m'  # اخضر
C = "\033[1;97m"  # ابيض
B = '\033[2;36m'  # سمائي
# ---------------------------[CoDe BY GDO]------------------------
Op = "7"
azo = f'{Z}━' * 25
print(azo +
f"\n {X}« {C}Welcome To {X}ĞĐØ {C}Tool {X}»\n" +azo)

def pas():
    J = input(f"{X}[{C}⌯{X}]{C} ENTER Password {X}»{C} ")
    if J == Op:
        print(f"\n {F} ♔︎ GOOD LUCK ♔︎ ")
        time.sleep(1);cls()
    else:
        print(f'{Z}  ERORR BRO ');pas()

def azz():
    gdo0 = (f"""{X}                                                        

  .88888.  888888ba   .88888.  
 d8'   `88 88    `8b d8'   `8b 
 88        88     88 88     88 
 88   YP88 88     88 88     88 
 Y8.   .88 88    .8P Y8.   .8P 
  `88888'  8888888P   `8888P' 

    {X}« {C}Script UserNames {X}»
{X}┏{Z}━━━━━━━━━━━━━━━━━━━━━━━━━━{X}┓
{Z}┃{C} ⌯ Developer {Z}›{C} @GDO00     {Z}┃
{Z}┃{C} ⌯ Channel   {Z}›{C} @GDO_0     {Z}┃
{Z}┃{C} ⌯ Channel   {Z}›{C} @GDOTOOLS  {Z}┃
{Z}┃{C} ⌯ Bot store {Z}›{C} @kt7ktbot  {Z}┃ 
{Z}┃{C} ⌯ Github    {Z}›{C} @GDO00     {Z}┃
{X}┗{Z}━━━━━━━━━━━━━━━━━━━━━━━━━━{X}┛""")
    for o in gdo0.splitlines():
        time.sleep(0.05)
        print(o)


pas()
azz()

token = input(f'{X} [{C}⌯{X}] {C}ENTER TOKEN{X} » ' + C)
ID = input(f'{X} [{C}⌯{X}] {C}ENTER ID{X} » ' + C)
use = string.ascii_letters

message_id = requests.post(
	url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=ʜᴇʟʟᴏ ᴍʏ ғʀɪᴇɴᴅ ◔‌◔"
	).json()['result']["message_id"]

def get_user():
	user = ''.join(
			random.choice(
				random.choice(
					random.choice(use + "_.")
				)
			) for i in range(random.randint(5,7))
		)
	return user if user[0] != '.' and ".." not in user and '.' not in user[-1] and ('.' in user or '_' in user) and (user.count('.') < 2) else get_user()

def main():
    ht, bd = 0, 0
    while True:
        user = get_user()
        with requests.Session() as azoz:
            headers = {"User-Agent": str(generate_user_agent())}
            data = azoz.get(
                url="https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", 
                headers=headers
            ).cookies.get_dict()
        response = requests.post(
            url='https://www.instagram.com/accounts/web_create_ajax/attempt/',
            headers={"accept": '*/*',
                     'accept-encoding': "gzip, deflate, br",
                     "accept-language": "ar,en;q=0.9",
                     "content-length": "383",
                     "content-type": "application/x-www-form-urlencoded",
                     "cookie": f'mid={data["mid"]}; ig_did={data["ig_did"]};ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; datr=1AowYgO84Ejd51RFZGIapmbk; ig_direct_region_hint="CLN\05453358207778\0541688796486:01f71cfca83b40e08f4455a3c69feeefeadf41a6c7a76553e488c59b2ae8ae624b229f08"; shbid="15813\05453358207778\0541689148844:01f7d1c6791d8190c1c1903a32c63fda8a72a91405faad7bc23f83066265b367c4fc04ef"; shbts="1657612844\05453358207778\0541689148844:01f7abef005a2c35962e3880fd1de92c761afc12b8c5849e063f0c368c972e163af643b0"; rur="LDC\05453358207778\0541689148887:01f7fd3581f7650425803d85c4caa8eff267ad008011b894b92ab54fb7968b071ab81cca"; csrftoken={data["csrftoken"]}',
                     'origin': "https://www.instagram.com",
                     "referer": "https://www.instagram.com/accounts/emailsignup/",
                     "sec-ch-prefers-color-scheme": "light",
                     "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                     "sec-ch-ua-mobile": "?0",
                     "sec-ch-ua-platform": "Windows",
                     "sec-fetch-dest": "empty",
                     "sec-fetch-mode": "cors",
                     "sec-fetch-site": "same-origin",
                     "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                     "viewport-width": "617",
                     "x-asbd-id": "198387",
                     "x-csrftoken": str(data['csrftoken']),
                     "x-ig-app-id": "936619743392459",
                     "x-ig-www-claim": "0",
                     "x-instagram-ajax": "d66974950786",
                     "x-requested-with": "XMLHttpRequest"},
            data={
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:GDOTools',
                "email": "gdotools56432@gmail.com",
                "username": str(user),
                "first_name": "GDO Tools",
                "client_id": "Yemn3AAEAAGx56yZBU5-oiVvPQ4e",
                "seamless_login_enabled": "1",
                "opt_into_one_tap": "false"}
        ).text
        
        if "This username isn't available. Please try another." in response or '"username_is_taken"}' in response or '"Try Again Later",' in response:
            bd += 1
            
            requests.post(
                f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={message_id}&text=⌯ 𝙲𝙷e𝙲𝚔  𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 ⸙\n•──────────────•\n▩ 𝙷𝙸𝚃 » {ht}\n▩ 𝙱𝙰𝙳 » {bd}\n▩ ᴜsᴇʀ » {user}\n•──────────────•")
        else:
            ht += 1
            requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌲ ʜɪ ɴᴇᴡ ᴜsᴇʀ ɪɴꜱᴛᴀ ʙʏ ĞĐØ ᯓ\n•─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─•\n⎙ ᴜsᴇʀɴᴀᴍᴇ  » {user}\n•─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─•\n ◔͜͡◔ ʙʏ › @GDOTools - @GDO_0 .")
        print(f"\r{X} • BaD {Z}› {X}{bd} | {F} GooD {C}› {F}{ht} | {X}~ {C}User {X}» {C}{user}")

for i in range(20):
	threading.Thread(target=main()).start()
	threading.Thread(target=main()).start()