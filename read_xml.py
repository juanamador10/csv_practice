import xml.etree.ElementTree as ET
tree = ET.parse('xml_csv.xml')
root = tree.getroot()


'''for i in range(len(root)):
    print(root[i][0].text, root[i][1].text, root[i][2].text)'''

vivienda = []
for i in range(len(root)):
    print(root[i][0].text)

    if root[i][0] in vivienda:
        pass
    else:
        vivienda.append()
