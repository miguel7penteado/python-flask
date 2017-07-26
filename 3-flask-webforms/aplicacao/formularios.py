from flask_wtf          import Form
from wtforms            import StringField, BooleanField
from wtforms.validators import DataRequired

class FormularioAutenticacao(Form):
    campo_identificacao = StringField('campo_identificacao', validators=[DataRequired()])
    campo_lembre_me     = BooleanField('campo_lembre_me', default=False)