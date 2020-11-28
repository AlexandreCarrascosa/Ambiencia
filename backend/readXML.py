import xml.etree.ElementTree as ET
from xml.dom import minidom

path = '/home/alexandre/Documents/GitHub/Ambiencia/data.xml'

root = ET.parse(path).getroot()


for child in root:
	for i in child:
		item = i.tag //Lê o nome do item
		value = i.text //Lê o valor do item
		
		print(f'{item}: {value}')
		


	

