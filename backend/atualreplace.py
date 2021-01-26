import xml.etree.ElementTree as ET
from glob import glob

def AtualRefresh(data, hora, temp, umd, aspr="OFF", vent="OFF", lamp="OFF"):

	path = r'../atual.xml'
	tree = ET.parse(path)
	root = tree.getroot()


	for i in root.iter():
		if i.tag == 'data':
			i.text = data
		if i.tag == 'hora':
			i.text = hora
		if i.tag == 'temp':
			i.text = temp
		if i.tag == 'umd':
			i.text = umd	
		if i.tag == 'aspr':
			i.text = aspr
		if i.tag == 'vent':
			i.text = vent
		if i.tag == 'lamp':
			i.text = lamp


	tree.write(r'../atual.xml')			
	
			
		
