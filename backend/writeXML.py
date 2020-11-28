import xml.etree.ElementTree as ET

path = '../data.xml'
tree = ET.parse(path)
root = tree.getroot()


info = ET.SubElement(root, 'Info')

data = ET.SubElement(info, 'data')
data.text = '22/11/2020'

hora = ET.SubElement(info, 'hora')
hora.text = '23:03'

temp = ET.SubElement(info, 'temp')
temp.text = '25'

umid = ET.SubElement(info, 'umd')
umid.text = '50'

aspr = ET.SubElement(info, 'aspr')
data.text = 'OFF'

vent = ET.SubElement(info, 'vent')
vent.text = 'OFF'

lamp = ET.SubElement(info, 'lamp')
lamp.text = 'OFF'

tree.write('..	/data.xml')




