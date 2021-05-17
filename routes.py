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


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
        return 'Hello, World!'


if __name__ == '__main__':
    app.run()
