# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask        import render_template, flash, redirect
from aplicacao    import variavel_aplicacao
from .formularios import FormularioAutenticacao

@variavel_aplicacao.route('/')
@variavel_aplicacao.route('/indice')
def indice():
    usuario_sessao = {'primeiro_nome': 'Miguel'}  # usuario teste
    return render_template('indice.html', titulo='Pagina Inicial',  parametro_usuario=usuario_sessao)

@variavel_aplicacao.route('/indice0')
def indice0():
    usuario_sessao = {'primeiro_nome': 'Miguel'}  # usuario teste
    return render_template('indice0.html', titulo='Pagina Inicial',  parametro_usuario=usuario_sessao)

@variavel_aplicacao.route('/indice2')
def indice2():
    usuario_sessao = {'nome_usuario': 'Miguel'}  # usuario_teste
    matriz_postagem = [  # Simulacao de matriz de postagem (vulgo post do html)
        { 
            'autor': {'primeiro_nome': 'Miguel'}, 
            'corpo': 'Belo dia em Sao Paulo!' 
        },
        { 
            'autor': {'primeiro_nome': 'Marcia'}, 
            'corpo': u'O filme do Lion me é muito bom!' 
        }
    ]
    return render_template("indice2.html", title='Pagina Principal 2', parametro_usuario=usuario_sessao, parametro_matriz_postagem=matriz_postagem)

@variavel_aplicacao.route('/autenticacao', methods=['GET', 'POST'])
def autenticar():
    conseguiu_autenticar=None	 
    formulario = FormularioAutenticacao()
    if ( formulario.validate_on_submit() ):
        flash('Requisicao para campo_identificacao="%s", campo_lembre_me=%s' % (formulario.campo_identificacao.data, str(formulario.campo_lembre_me.data)))
        conseguiu_autenticar=True
    else:
        conseguiu_autenticar=False
    if (conseguiu_autenticar):
        return redirect('/indice')
    else:
        return render_template('autenticar.html', title='Autentique-se',parametro_formulario=formulario)


