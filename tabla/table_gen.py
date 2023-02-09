# -*- coding: utf-
# Author: Alexander Alvarado
# Email: daalvarado@ine.gob.gt 
# Libraries used: argparse, pandas, openpyxl  
#
#############################################
#                                           #
#           TABLE GENERATOR                 #
#                                           #
#############################################

import argparse 
import pandas as pd

'''

OBTENER LA ENTRADA Y SALIDA DEL USUARIO

'''
parser = argparse.ArgumentParser(description='Generador de tablas')
parser.add_argument('--input', metavar='-i', type=str,
                    help='base de datos en excel (sin extensión)')
parser.add_argument('--output', metavar='-o', type=str,
                    help='nombre de tabla de salida (sin extensión)')

args = parser.parse_args()

# CHECKPOINT, MIGHT DELETE 
print("su primer arg: " ,args.input)
print("su primer arg: " ,args.output)

# Archivos de entrada y salida

inname = args.input + ".xlsx"
outname = args.output + ".xlsx"

'''
CREATING DATAFRAME
'''

dataframe = pd.read_excel(inname, sheet_name='INSTITUTO NACIONAL DE ESTADí...', dtype=str, usecols = ['Semana',
                                                                                                      'Usuario',
                                                                                                      'Nombre de la Fuente',
                                                                                                      'No. de Boleta',
                                                                                                      'Código de Fuente',
                                                                                                      'Teléfono',
                                                                                                      'Fecha de Recopilación',
                                                                                                      'Municipio',
                                                                                                      'Zona',
                                                                                                      'Dirección'])



dataframe.rename(columns = {'Fecha de Recopilación':'Fecha', 
                            'Nombre de la Fuente':'Fuente', 
                            'Dirección':'Direccion', 
                            'No. de Boleta':'Boleta',
                            'Usuario':'Cotizador' }, inplace = True)
# CHECKPOINT MIGHT DELETE
print(dataframe.Boleta)
dataframe.Fecha = dataframe['Fecha'].str.split().str[0]
dataframe.Cotizador = dataframe['Cotizador'].str.split('- ').str[1]

print(dataframe.Cotizador)


'''

ESCRIBIR NUEVO EXCEL 

'''
cols = ['Boleta','Semana','Cotizador','Fuente','Código de Fuente','Teléfono','Fecha','Municipio','Zona','Direccion']
dataframe.insert
dataframe.to_excel(outname,columns = cols, index = False)