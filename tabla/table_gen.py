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
import numpy as np
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
ty = {'Semana':np.intc, 'Usuario':str, 'Nombre de la Fuente': str,'No, de Boleta':str, 'Código de Fuente':str, 'Teléfono':str, 'Fecha de Recopilación':str, 'Municipio': str, 'Zona':str, 'Dirección':str}
dataframe = pd.read_excel(inname, sheet_name='INSTITUTO NACIONAL DE ESTADí...', dtype=str, usecols = ['Semana',
                                                                                                      'Usuario',
                                                                                                      'Nombre de la Fuente',
                                                                                                      'No. de Boleta',
                                                                                                      'Código de Fuente',
                                                                                                      'Teléfono',
                                                                                                      'Fecha de Recopilación',
                                                                                                      'Municipio',
                                                                                                      'Zona',
                                                                                                      'Dirección',
                                                                                                      ])



dataframe.rename(columns = {'Fecha de Recopilación':'Fecha', 
                            'Nombre de la Fuente':'Fuente', 
                            'Dirección':'Direccion', 
                            'No. de Boleta':'Boleta',
                            'Usuario':'Cotizador' }, inplace = True)
# CHECKPOINT MIGHT DELETE
print(dataframe.Boleta)
dataframe.Fecha = dataframe['Fecha'].str.split(' ').str[0]
dataframe.Fecha = pd.to_datetime(dataframe['Fecha'], dayfirst=True)#.dt.strftime('%d/%m/%Y')
#dataframe.Fecha = dataframe.Fecha.dt.strftime('%d/%m/%Y')
dataframe.Cotizador = dataframe['Cotizador'].str.split('- ').str[1]

print(dataframe.Fecha)


'''

ESCRIBIR NUEVO EXCEL 

'''
cols = ['Boleta','Semana','Cotizador','Fuente','Código de Fuente','Teléfono','Fecha','Municipio','Zona','Direccion']

writer = pd.ExcelWriter(outname,
                    engine='xlsxwriter',
                    date_format='dd/mm/yyyy',datetime_format='dd/mm/yyyy')

dataframe.to_excel(writer,columns = cols, index = False)
writer.close()