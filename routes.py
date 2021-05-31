#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIDADÃO DF
O aplicativo “Cidadão DF”, possibilita o registro de um problema em sua exata localização, dimensão e horário; e deixa o cidadão no anonimato. Registra qualquer tipo de problema com uma foto, que inclui automaticamente sua localização e momento em que foi tirada, comprovando e expondo os problemas. Desde um buraco na rua até a presença de grupos suspeitos, o aplicativo tem por objetivo otimizar o trabalho dos órgãos competentes, na identificação dos problemas de infraestrutura e segurança que assolam um número considerável de cidadãos, possibilitando uma rápida solução na atuação dos problemas.

Objetivos:
Não necessitando realizar um cadastro, o App permite categorizar a denúncia:

- LIXO: referente a informações de entulhos clandestinos, acúmulo de detritos em “bocas de lobo”, nascentes contaminadas e outros problemas relacionados ao lixo,
- ESGOTO E ÁGUA: referente a situações de esgotos expostos, vazamento de água, tubulações danificadas e outros problemas relacionados a Esgoto e Água,
- VIAS PÚBLICAS: referente à situação das calçadas, pistas, canteiros e outros problemas relacionados as Vias Públicas,
- ESTRUTURAS PÚBLICAS: referente à situação de passarelas, estacionamentos, placas, pontos de ônibus, iluminação e outros problemas relacionados as Estruturas Públicas,
- SEGURANÇA: referente a suspeitas de tráfico, vadiagem, venda ilegal de armas, lavagem de dinheiro, contrabando, pontos de distribuição de drogas e outros problemas relacionados à Segurança,
- TRANSPORTE: referente a lotações, falta de ônibus, precariedades no transporte público e outros problemas relacionados ao Transporte Público;
- VIOLÊNCIA: referente a denúncias de violência doméstica, e outras.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField # Os validadores são usados para garantir que as entradas sejam o que a gente espera.
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask import render_template, Blueprint, redirect, url_for, flash, request
from flask import Flask, render_template, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'minhasenha'

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/lixo')
def lixo(): 
    return render_template('lixo.html')

@app.route('/esgotoAgua')
def esgotoAgua(): 
    return render_template('esgotoAgua.html')

@app.route('/estruturasPublicas')
def estruturasPublicas(): 
    return render_template('estruturasPublicas.html')

@app.route('/seguranca')
def seguranca(): 
    return render_template('seguranca.html')

@app.route('/transporte')
def transporte(): 
    return render_template('transporte.html')

@app.route('/viasPublicas')
def viasPublicas(): 
    return render_template('viasPublicas.html')

@app.route('/violencia')
def violencia(): 
    return render_template('violencia.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
