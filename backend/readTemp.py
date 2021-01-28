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

        if int(readTemp()[12]) == 0:
                lamp = 'ON'
        if int(readTemp()[12]) == 1:
                lamp = 'OFF'

        if int(readTemp()[14]) == 0:
                vent = 'ON'
                aspr = 'ON'
        if int(readTemp()[14]) == 1:
                vent = 'OFF'
                aspr = 'OFF'
        
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
        aspr.text = aspr

        vent = ET.SubElement(info, 'vent')
        vent.text = vent

        lamp = ET.SubElement(info, 'lamp')
        lamp.text = lamp

        tree.write('../data.xml')

        AtualRefresh(Data()[0],
                     Data()[1],
                     temperatura,
                     umidade,
                     lamp = lamp,
                     vent = vent,
                     aspr = aspr)
                     
        CalcPsic(temperatura, umidade)
        
        sleep(10)
        Atualizar()
        

        

