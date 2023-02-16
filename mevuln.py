import os

target_IP = input("Introduzca la dirección IP del equipo a escanear: ") 

def verificar_vulnerabilidades():
	scan = 'nmap  -A -oN ./mevulnlogs/mevuln.txt ' + target_IP
	informe = os.system(scan)
	
	if informe == 0:
		print ("Vulnerabilidades encontradas. Revisa mevuln.txt en la carpeta mevulnlogs para más detalles.")
	else:
		print ("No se han encontrado vulnerabilidades de seguridad.")
		
verificar_vulnerabilidades()
