import observer
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
cliente = observer.Cliente()
funcionario = observer.Cliente()
pedido = observer.Pedido()

@app.route('/')
def index():
   return render_template('pizza.html')

@app.route('/pizza', methods = ["GET", "POST"])
def pizza():
   if request.method == "POST":
      form = request.form
      pedido.adicionarPedido(form['pizza'])
      return redirect(url_for('formulario'))
   else:
      return render_template('pizza.html')

@app.route('/formulario', methods = ["GET", "POST"])
def formulario():
   if request.method == "POST":
      form = request.form
      cliente.adicionarDados(form["nome"], form["telefone"], form["email"], form["rua"], form["numero"])
      pedido.attach(cliente)
      pedido.atualizarStatus("registrando")
      return redirect(url_for('acompanha'))
   else:
      return render_template('formulario.html')


@app.route('/acompanha', methods = ["GET"])
def acompanha():
   return render_template("acompanha.html", pedido_html = pedido._historico_state)


@app.route('/atualizador', methods = ["GET", "POST"])
def atualizador():
   if request.method=="POST":
      pedido.atualizarStatus(request.form["status"])
      return render_template("atualizador.html")
   else:
      return render_template("atualizador.html")


if __name__ == '__main__':
   app.run(debug = True)