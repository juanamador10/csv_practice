#Juan Fernando Amador Miranda - 9° A BIS - ISW

import xml.etree.cElementTree as ET
import mariadb

#XML Initialization
root = ET.Element("codigos_postales")
tree = ET.ElementTree(root)


#Database Connection
miConexion = mariadb.connect(host='localhost',
                                     user= 'root', 
                                     passwd='', 
                                     db='csvdatabase' )
cur = miConexion.cursor()
cur.execute( "SELECT d_tipo_asenta, id_asenta_cpcons, c_oficina FROM codigos_postales" )

for d_tipo_asentamiento, id_asenta_cpcons, c_oficina, in cur.fetchall():
    doc = ET.SubElement(root, "codigo_postal")
    ET.SubElement(doc, "d_tipo_asentamiento").text = d_tipo_asentamiento
    ET.SubElement(doc, "id_asenta_cpcons").text = str(id_asenta_cpcons)
    ET.SubElement(doc, "c_oficina").text = str(c_oficina)

    #Selected PATH where XML file is saved      #Create or Update XML    
    tree.write("xml_csv.xml")


miConexion.close()




