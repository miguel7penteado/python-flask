from flask     import render_template
from aplicacao import variavel_aplicacao

@variavel_aplicacao.route('/')
@variavel_aplicacao.route('/indice')
def indice():
    usuario_sessao = {'primeiro_nome': 'Miguel'}  # usuario teste
    return render_template('indice.html', title='Pagina Inicial',  user=usuario_sessao)


