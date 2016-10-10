#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json
import urllib.request


class KaraokeLocal():

    def init(self, fich):
        parser = make_parser()
        self.KHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(self.KHandler)
        parser.parse(open(fich))
        self.misdatos = self.KHandler.get_tags()

    def do_local(self):
        for datos in self.misdatos:
            for dato in datos:
                if datos[dato][:7] == 'http://':
                    file_name = datos[dato].split('/')[-1]
                    web = urllib.request.urlretrieve(datos[dato], file_name)
                    print(web)

    def __str__(self):
        for datos in self.misdatos:  # datos es cada diccionario por separado
            tag = datos['etiqueta']
            linea = tag + '\t'
            for dato in datos:   # dato es cada atributo del diccionario
                if datos[dato] != tag:
                    valor = datos[dato]
                    linea = linea + '\t' + dato + '=' + '"' + valor + '"'
            print(linea)
            linea = ''

    def to_json(self, smilfile):
        jsonfile = open(smilfile.split('.')[0] + '.json', 'w')
        jsoncontent = json.dumps(self.misdatos)
        jsonfile.write(jsoncontent)


if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil')   
    KLocal = KaraokeLocal()
    KLocal.init(fichero)
    KLocal.__str__()
    KLocal.to_json(fichero)
    KLocal.do_local()
    KLocal.to_json('local')
    KLocal.__str__()
