# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask     import render_template, flash, redirect, jsonify, abort
from aplicacao import variavel_aplicacao


tabela_produtos = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@variavel_aplicacao.route('/')
@variavel_aplicacao.route('/todo/api/v1.0/produtos', methods=['GET'])
def lista_produtos():
    return jsonify({'produtos': tabela_produtos})


@variavel_aplicacao.route('/todo/api/v1.0/produtos/<int:codigo_produto>', methods=['GET'])
def lista_produto_por_codigo(codigo_produto):
    produto = [produto for produto in tabela_produtos if produto['id'] == codigo_produto]
    if len(produto) == 0:
        abort(404)
    return jsonify({'produto': produto[0]})
