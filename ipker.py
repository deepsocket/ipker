import os
import time
import colorama
import requests
import pprint
import subprocess
import readline
from colorama import Fore

class Banner:
	ban = ['cat', './banner/ban']
	creator = "deepsocket"
	version = None

def funtion_banner():
	try:
		print(Fore.RED)
		subprocess.run(Banner.ban)
		print(Fore.GREEN+"creator :", Banner.creator, "\nversion:", Banner.version)
		print(Fore.WHITE)
	except OSError:
		print("Error al ejecutar el banner")
def show():
	try:
		print("[*]Iniciando Ipker")
		time.sleep(2)
	except OSError:
		print("error")

def Ip_info_collect(scanf):
	try:
		response = requests.post('http://ip-api.com/json/{}'.format(scanf))
		clen = response.json()
		convert = dict(clen)
		print(Fore.RED)
		print(Fore.BLUE+"as :", Fore.RED+convert['as'])
		print(Fore.BLUE+"ciudad :", Fore.RED+convert['city'])
		print(Fore.BLUE+"Codigo de pais :", Fore.RED+convert['countryCode'])
		print(Fore.BLUE+"provedor :", Fore.RED+convert['isp'])
		print(Fore.BLUE+"latitud : ", Fore.RED+str(convert['lat']))
		print(Fore.BLUE+"longitud :", Fore.RED,convert['lon'])
		print(Fore.BLUE+"org :", Fore.RED+convert['org'])
		print(Fore.BLUE+"direccion :", Fore.RED+convert['query'])
		print(Fore.BLUE+"region :", Fore.RED+convert['region'])
		print(Fore.BLUE+"RegionName :", Fore.RED+convert['regionName'])
		print(Fore.BLUE+"estado :", Fore.RED+convert['status'])
		print(Fore.BLUE+"timezone", Fore.RED+convert['timezone'])
		print(Fore.BLUE+"zip :", Fore.RED+convert['zip'])
		print(Fore.YELLOW+"\nProceso terminado"+Fore.WHITE)
		#pprint.pprint(convert)
	except OSError:
		print("Error de conexion, peticion post rechazada!")
def global_funtion():
	user_global = input("+Escribe la direccion: ")
	try:
		if(user_global != ""):
			show()
			funtion_banner()
			Ip_info_collect(user_global)
		else:
			print("Debes especificar una IpAddress")
	except OSError:
		print("Error al ejecutar programa")
global_funtion()
