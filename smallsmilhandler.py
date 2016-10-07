#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        """Inicializador de varibles. dicc_atributos es un diccionario con
           claves 'etiqueta' y los nombres de los atributos y como valores
           el nombre de la etiqueta ppal y los atributos"""
        self.dicc_atributos = {}
        self.misdatos = []

    def startElement(self, name, attrs):
        # Método que se llama cuando se abre una etiqueta
        if name == 'root-layout':
            self.dicc_atributos['etiqueta'] = name
            self.dicc_atributos['width'] = attrs.get('width', '0')
            self.dicc_atributos['height'] = attrs.get('height', '0')
            self.dicc_atributos['background_color'] = \
                attrs.get('background-color', '-')
            self.misdatos.append(self.dicc_atributos)
            self.dicc_atributos = {}
        elif name == 'region':
            self.dicc_atributos['etiqueta'] = name
            self.dicc_atributos['id'] = attrs.get('id', '-')
            self.dicc_atributos['top'] = attrs.get('top', '0')
            self.dicc_atributos['bottom'] = attrs.get('bottom', '0')
            self.dicc_atributos['left'] = attrs.get('left', '0')
            self.dicc_atributos['right'] = attrs.get('right', '0')
            self.misdatos.append(self.dicc_atributos)
            self.dicc_atributos = {}
        elif name == 'img':
            self.dicc_atributos['etiqueta'] = name
            self.dicc_atributos['src'] = attrs.get('src', '-')
            self.dicc_atributos['region'] = attrs.get('region', '-')
            self.dicc_atributos['begin'] = attrs.get('begin', '-')
            self.dicc_atributos['dur'] = attrs.get('dur', '-')
            self.misdatos.append(self.dicc_atributos)
            self.dicc_atributos = {}
        elif name == 'audio':
            self.dicc_atributos['etiqueta'] = name
            self.dicc_atributos['src'] = attrs.get('src', '-')
            self.dicc_atributos['begin'] = attrs.get('begin', '-')
            self.dicc_atributos['dur'] = attrs.get('dur', '-')
            self.misdatos.append(self.dicc_atributos)
            self.dicc_atributos = {}
        elif name == 'textstream':
            self.dicc_atributos['etiqueta'] = name
            self.dicc_atributos['src'] = attrs.get('src', '-')
            self.dicc_atributos['region'] = attrs.get('region', '-')
            self.misdatos.append(self.dicc_atributos)
            self.dicc_atributos = {}

    def get_tags(self):
        return self.misdatos

        

if __name__ == "__main__":

    parser = make_parser()
    SSHandler = SmallSMILHandler()
    parser.setContentHandler(SSHandler)
    parser.parse(open('karaoke.smil'))
    misdatos = SSHandler.get_tags()
    print(misdatos)
