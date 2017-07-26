# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Flask

variavel_aplicacao = Flask(__name__)
variavel_aplicacao.config.from_object('config')
# importar o pacote views do pacote app.
from aplicacao import visualizacoes
