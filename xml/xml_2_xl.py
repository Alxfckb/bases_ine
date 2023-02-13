import argparse 
import pandas as pd
import numpy as np
from os import listdir
import xml.etree.ElementTree as ET
from os.path import isfile, isdir, join

#R1_49_CECILIOBORRAYO/FUENTES_FEB_RECUPERADAS_49
'''

OBTENER LA ENTRADA Y SALIDA DEL USUARIO

'''
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
''' 

path = "example.xml"

tree = ET.parse(path)
root = tree.getroot()
for child in root:
    for grandchild in child:
        print (grandchild.tag,grandchild[0])