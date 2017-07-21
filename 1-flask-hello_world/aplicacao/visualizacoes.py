from aplicacao import variavel_aplicacao

@variavel_aplicacao.route('/')
@variavel_aplicacao.route('/indice')
def indice():
    return "Ola Mundo!"
	