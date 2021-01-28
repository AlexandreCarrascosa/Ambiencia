import xml.etree.ElementTree as ET
import pywhatkit as kit
import serial
from glob import glob
from time import sleep
from datetime import datetime
from subprocess import check_output
from update import Timer, Atualizar
from atualreplace import AtualRefresh
from CalcPsic import CalcPsic
from sys import platform

if platform == 'win32':
        conexao = serial.Serial('COM4', 9600)
else:
        conexao = serial.Serial('/dev/ttyACM0', 9600)

path = '../data.xml'
tree = ET.parse(path)
root = tree.getroot()

def readTemp():
        while True:
                read = conexao.readline().strip()
                valor = str(read)
                terminal = valor.split("'")[1]
                
                return terminal
        
def Data():
        atual = datetime.now()
        data = atual.strftime("%d/%m/20%y")
        hora = atual.strftime("%H:%M")
        
        return data, hora
        
        

while True:
        msg = "Dados escritos!\nIniciando contagem para próximo registro:"
        Timer(0, 10, msg)
        #print(f'{Data()[0]}, {Data()[1]}, {readTemp()}')
        umidade = readTemp()[0:5]
        temperatura = readTemp()[6:10]

        print(readTemp()[10])
        
        info = ET.SubElement(root, 'Info')
        
        data = ET.SubElement(info, 'data')
        data.text = Data()[0]
        
        hora = ET.SubElement(info, 'hora')
        hora.text = Data()[1]
        
        temp = ET.SubElement(info, 'temp')
        temp.text = temperatura
        
        umid = ET.SubElement(info, 'umd')
        umid.text = umidade
        
        aspr = ET.SubElement(info, 'aspr')
        aspr.text = 'OFF'

        vent = ET.SubElement(info, 'vent')
        vent.text = 'OFF'

        lamp = ET.SubElement(info, 'lamp')
        lamp.text = 'OFF'

        tree.write('../data.xml')

        AtualRefresh(Data()[0],
                     Data()[1],
                     temperatura,
                     umidade)
                     
        CalcPsic(temperatura, umidade)
        
        sleep(10)
        Atualizar()
        

        if float(temperatura) > 32:
                kit.sendwhatmsg("+5566999087650", "Temperatura acima de 32ºC, verifique a Estufa!")

