from xml.etree import ElementTree as ET

def serializeImports(importsXML):
    data = {
        "consumerGoods" : [],
        "intermediateGoods" : [],
        "capitalGoods" : [],
        "total" : [],
        "month" : [],
        "year" : [],
    }
    root = ET.fromstring(importsXML)
    for import_item in root.findall('codigo_postal'):
        data['d_tipo_asentamiento'].append(float(import_item.find('d_tipo_asentamiento').text))  
        data['intermediateGoods'].append(float(import_item.find('intermediateGoods').text))  
        data['capitalGoods'].append(float(import_item.find('capitalGoods').text))  
        data['total'].append(int(import_item.find('total').text))  
        data['month'].append(import_item.find('month').text)  
        data['year'].append(import_item.find('year').text) 

    return data


    <d_tipo_asentamiento>Colonia</d_tipo_asentamiento>
<id_asenta_cpcons>1</id_asenta_cpcons>
<c_oficina>72091</c_