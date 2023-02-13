import argparse 
import pandas as pd
from os import listdir
from os.path import isfile, isdir, join
import pandas_read_xml as pdx

'''

OBTENER LA ENTRADA Y SALIDA DEL USUARIO

'''
parser = argparse.ArgumentParser(description='***** XML TO EXCEL *****')

parser.add_argument('--user', metavar='-usuario', type=str,
                    help='carpeta de usuario')

#parser.add_argument('--m', metavar='-mes', type=str,
                    #help='carpeta de mes')

parser.add_argument('--output', metavar='-o', type=str,
                    help='nombre de tabla de salida (sin extensión)')

args = parser.parse_args()
path = args.user
outname = args.output+'.xlsx'

cols = ['uuid', 'start', 'end', 'username', 'deviceid', 'ID_Region', 'ID_Departamento', 'Municipio', 'Decada', 'Usuario', 'NumeroBoleta', 'TipoFuente', 'CodigoFuente', 'NombreFuente', 'Direccion', 'Zona', 'Telefono', 'Correo', 'NombreInformante', 'CargoInformante', 'Observacion', 'NumerodeArticulos', 'AgregarFoto', 'Foto', 'GPS', 'FechaRecopilacion', '__version__', '_version_', '_version__001', '_version__002', '_version__003', '_version__004', '_version__005', 'instanceID']

dataframe = pd.DataFrame()

dataframe = dataframe.reindex(columns=cols)  

print(dataframe.info())

temp = pd.DataFrame()

dirs = [f for f in listdir(path) if isdir(join(path, f))]
#print(dirs)
for dir in dirs:
    path = args.user+'\\' + dir
    for filename in listdir(path):
        if not filename.endswith('.xml'): continue
        fullname = join(path, filename)
        print(fullname)
        #temp = pdx.read_xml(fullname,cols,root_is_rows=False)
    temp = pd.read_xml(fullname)
    temp = flatten(temp)
dataframe = pd.concat([temp,dataframe],join='inner')
#dataframe = pd.merge(temp,dataframe, how='left')  
#cols = list(temp.columns.values)
#print(cols)      
print(dataframe.info())
dataframe.to_excel(outname, columns=cols, index=False)

    