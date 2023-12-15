from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

def formataReal(valor):
    valorStr = str("%.2f" % valor)
    return valorStr.replace(".", ",")

def calcular_troco(valorCompra, valorRecebido):
        if valorCompra<valorRecebido:
                troco = valorRecebido - valorCompra
                resultado = "Total da compra: R${}<br>Valor recebido: R${}<br>[Valor do troco: R${}]".format(formataReal(valorCompra), formataReal(valorRecebido), formataReal(troco))
                return resultado
        elif valorCompra>valorRecebido:
                falta = valorCompra - valorRecebido
                return "Dinheiro insuficiente. Parte faltante: {}".format(formataReal(falta))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_troco', methods=['POST'])
def calcular_troco_route():
        valorCompra = float(request.form['valorCompra'])
        valorRecebido = float(request.form['valorRecebido'])

        resultado = calcular_troco(valorCompra, valorRecebido)
        return render_template('index.html', resultado=resultado)

app.run(debug=True)
