import argparse 
import pandas as pd
from os import listdir
import xml.etree.ElementTree as ET
from os.path import isfile, isdir, join

'''

OBTENER LA ENTRADA Y SALIDA DEL USUARIO

'''

parser = argparse.ArgumentParser(description='***** XML TO EXCEL *****')

parser.add_argument('--user', type=str,
                    help='carpeta de usuario')

parser.add_argument('--output', type=str,
                    help='nombre de tabla de salida (sin extensión)')

args = parser.parse_args()

#col = ['uuid', 'ID_Region', 'ID_Departamento', 'Municipio', 'Decada', 'Usuario', 'NumeroBoleta', 'TipoFuente',
# 'CodigoFuente', 'NombreFuente', 'Direccion', 'Zona', 'Telefono', 'Correo', 'NombreInformante', 
#'CargoInformante', 'Observacion', 'NumerodeArticulos', 'AgregarFoto', 'Foto', 'GPS', 'FechaRecopilacion', 'instanceID']


# Obtener el directorio donde están almacenadas las carpetas "INSTITUTO NACIONAL ..."
path = args.user
outname = join('fuentes_recuperadas',args.output) + '.xlsx'

# Definir los campos a extraer y escribir
cols = {'start':[],'end':[],'username':[],'uuid':[] ,'ID_Region':[], 'ID_Departamento':[], 'Municipio':[] , 'Decada':[] , 'Usuario':[] , 'NumeroBoleta':[] ,
 'TipoFuente':[] , 'CodigoFuente':[] , 'NombreFuente':[] , 'Direccion':[] , 'Zona':[] , 'Telefono':[] ,
  'Correo':[] , 'NombreInformante':[] , 'CargoInformante':[] , 'Observacion':[] ,'Especifique':[], 'NumerodeArticulos':[] ,
   'AgregarFoto':[] , 'Foto':[] , 'GPS':[] , 'FechaRecopilacion':[], 'instanceID':[] }

dataframe = pd.DataFrame(cols)

dirs = [f for f in listdir(path) if isdir(join(path, f))]
#print (dirs)
#dataframe = pd.DataFrame()
#dataframe = dataframe.reindex(columns=cols)  

# Lectura y extracción de datos en cada uno de los archivos xml
for dir in dirs:
    path = join(args.user,dir)
    for filename in listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = join(path, filename)
        tree = ET.parse(fullname)
        root = tree.getroot()
        for child in root:
            if child.tag in cols:
                cols[child.tag].append(child.text)
            print(child.tag, child.text)
            for grandchild in child:
                if grandchild.tag in cols:
                    cols[grandchild.tag].append(grandchild.text)
#print(cols)
dataframe = pd.DataFrame.from_dict(cols,orient='index').T
print(dataframe.info)
dataframe.to_excel(outname, columns=cols, index=False)