#!/usr/bin/python
import sys

from bottle import route, post, request, run
import psutil 
import os
import logging

logging.basicConfig(filename='archivo_salida_system_info.log', level=logging.INFO, format='%(message)s')

def crear_fichero_si_no_existe(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'w') as f:  # Se abre en modo escritura ('w')
            pass  # No se realiza ninguna acción, simplemente se crea el archivo
        f.close()  # Se cierra el archivo después de crearl

def añadir_a_fichero(nombre_archivo, texto):
    f = open(nombre_archivo, 'a')
    f.write(texto + '\n')
    f.close()
    
@route('/systemPerformance')
def getSystemPerformance():
    cpu =  psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    logging.info('devuelto cpu: '+ str(cpu) +', ram: ' + str(ram))
    systemPerformance = {'cpu': cpu, 'ram': ram}
    return dict(data=systemPerformance)


#/@post('/logines') # or @route('/login', method='POST')
#/def do_login():
#/   username = request.forms.get('username')
#/    password = request.forms.get('password')
#/    systemPerformance = {'cpu': username, 'ram': password}

#/    return dict(data=systemPerformance)
#/logines?username=pavon&password=1234

if __name__ == "__main__":
    run(host='localhost', port=3300, debug=True)