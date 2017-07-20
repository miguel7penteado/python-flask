@echo off

python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" flask
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" flask-login
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" flask-openid
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" flask-mail
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" flask-sqlalchemy
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" sqlalchemy-migrate
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" flask-whooshalchemy
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" flask-wtf
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" flask-babel
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" guess_language
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" flipflop
python -m pip install --upgrade --user --proxy="http://172.16.3.35:3128/" coverage

