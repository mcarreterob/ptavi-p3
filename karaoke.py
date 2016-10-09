#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import json

parser = make_parser()
SSHandler = SmallSMILHandler()
parser.setContentHandler(SSHandler)
misdatos = SSHandler.get_tags()

def salida_datos(misdatos):
    for datos in misdatos:    # datos es cada diccionario por separado
        linea = datos['etiqueta']    # inicializo la salida a la etiqueta
        del datos['etiqueta']
        for dato in datos:    #dato es cada atributo del diccionario
            valor = datos[dato]
            linea = linea + '\t' + dato + '=' + '"' + valor + '"' 
        print(linea)
        linea = ''

def smil_to_json(misdatos):
    smilfile = sys.argv[1]
    jsonfile = open(smilfile.split('.')[0] + '.json', 'w')
    jsoncontent = json.dump(misdatos)
    jsonfile.write(jsoncontent)



        
if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil')

    parser.parse(open(fichero))


