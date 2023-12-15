from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

def formataReal(valor):
    valorStr = str("%.2f" % valor)
    return valorStr.replace(".", ",")

def calcular_troco(valorCompra, valorRecebido):
        if valorCompra<valorRecebido:
                troco = valorRecebido - valorCompra
                return "Valor do troco: R${}".format(formataReal(troco))
        elif valorCompra>valorRecebido:
                falta = valorCompra - valorRecebido
                return "Dinheiro insuficiente. Parte faltante: {}".format(formataReal(falta))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_troco', methods=['POST'])
def calcular_troco_route():
    if request.method == 'POST':
        try:
            valorCompra = float(request.form['valorCompra'])
            valorRecebido = float(request.form['valorRecebido'])

            resultado = calcular_troco(valorCompra, valorRecebido)
            return render_template('index.html', resultado=resultado)
        except Exception as e:
            return f"Erro ao processar a solicitação: {str(e)}"

app.run(debug=True)