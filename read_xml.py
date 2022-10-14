import xml.etree.ElementTree as ET
tree = ET.parse('xml_test.xml')
root = tree.getroot()

for h in root:
    print(h.tag)
    