# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask     import render_template, flash, redirect, jsonify, abort, make_response, request
from aplicacao import variavel_aplicacao


tabela_produtos = [
    {
        'id': 1,
        'titulo': u'Padaria',
        'descricao': u'Pão, Coppa, Azeite, Frutas, Suco', 
        'disponivel': False
    },
    {
        'id': 2,
        'titulo': u'Limpeza',
        'descricao': u'Sabao, Água Sanitária', 
        'disponivel': False
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

@variavel_aplicacao.errorhandler(404)
def nao_encontrado(erro):
    return make_response(jsonify({'erro': 'Produto nao encontrado'}), 404)

@variavel_aplicacao.route('/todo/api/v1.0/produtos', methods=['POST'])
def inserir_produto():
    if ( (not request.json) or (not 'titulo') in request.json ):
        abort(400)
    produto = {
        'id': tabela_produtos[-1]['id'] + 1,
        'titulo': request.json['titulo'],
        'descricao': request.json.get('descricao', ""),
        'disponivel': False
    }
    tabela_produtos.append(produto)
    return jsonify({'produto': produto}), 201

    '''
    curl -i -H "Content-Type: application/json" -X POST -d '{"titulo":"Livros"}' http://localhost:5000/todo/api/v1.0/produtos
    '''
@variavel_aplicacao.route('/todo/api/v1.0/produtos/<int:codigo_produto>', methods=['PUT'])
def atualiza_produto(codigo_produto):
    produto = [produto for produto in tabela_produtos if produto['id'] == codigo_produto]
    if len(produto) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'titulo' in request.json and type(request.json['titulo']) != unicode:
        abort(400)
    if 'descricao' in request.json and type(request.json['descricao']) is not unicode:
        abort(400)
    if 'disponivel' in request.json and type(request.json['disponivel']) is not bool:
        abort(400)
    produto[0]['titulo'] = request.json.get('titulo', produto[0]['titulo'])
    produto[0]['descricao'] = request.json.get('descricao', produto[0]['descricao'])
    produto[0]['disponivel'] = request.json.get('disponivel', produto[0]['disponivel'])
    return jsonify({'produto': produto[0]})
'''
curl -i -H "Content-Type: application/json" -X PUT -d '{"disponivel":true}' http://localhost:5000/todo/api/v1.0/produtos/2
'''

@variavel_aplicacao.route('/todo/api/v1.0/produtos/<int:codigo_produto>', methods=['DELETE'])
def apaga_produto(codigo_produto):
    produto = [produto for produto in tabela_produtos if produto['id'] == codigo_produto]
    if len(produto) == 0:
        abort(404)
    tabela_produtos.remove(produto[0])
    return jsonify({'result': True})
'''
curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/todo/api/v1.0/produtos/2
'''
