from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/soma')
def soma():
    n1= int(request.args.get('valor1',0))
    n2= int(request.args.get('valor2',0))
   
    conta = n1 + n2

    return{
       'Resultado': conta
    }

@app.route('/subtracao')
def subtracao():
    n1= int(request.args.get('valor1',0))
    n2= int(request.args.get('valor2',0))

    conta = n1 - n2

    return{
        'Resultado': conta
    }


@app.route('/multiplicacao')
def multiplicacao():
    n1= int(request.args.get('valor1'),0)
    n2 = int(request.args.get('valor2'),0)

    conta = n1 * n2

    return{
        'Resultado': conta
    } 


@app.route('/divisao')
def divisao():
    n1= int(request.args.get('valor1',0))
    n2= int(request.args.get('valor2',0))

    conta = n1 / n2 

    return{
        'Resultado': conta
    }

if __name__ == '__main__':
    app.run(debug=True)