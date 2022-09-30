from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1> Holaaaaa mundo </h1>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('n','no puso nombre')
    return 'Hola {}'.format(nombre)

@app.route('/suma')
def sumando():
    n1=request.args.get('n1','no hay valor para n1')
    n2=request.args.get('n2','no hay valor para n1')
    suma=int(n1)+int(n2)
    return 'la suma de {} + {} es {}'.format(n1,n2,suma)

@app.route('/operacion')
@app.route('/operacion/<tipo>/<n1>/<n2>')
def operacion(tipo="indicar tipo",n1="valor n1",n2="valor n2"):
    if tipo=="suma":
        suma=int(n1)+int(n2)
        resultado="<b> suma de 2 numeros </b><br>La suma de {} + {} es {}".format(n1,n2,suma)
    elif tipo=="resta":
        resta=int(n1)-int(n2)
        resultado="<b> suma de 2 numeros </b><br>La resta de {} - {} es {}".format(n1,n2,resta)
    else:
        resultado=tipo
         
    return '{}'.format(resultado)

@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method=='POST':
        n1=request.form['n1']
        n2=request.form['n2']
        resultado=int(n1)+int(n2)
        return 'la suma de {} + {} es {}'.format(n1,n2,resultado)        

@app.route('/calculadora',methods=['GET','POST'])
def calculadora ():
    form="<form action='calcular' method='POST'>"
    form+="<input type='text' name='n1' size='5' /> + "
    form+="<input type='text' name='n2' size='5'/> "
    form+="<input type='submit' value='calcular' /></br>"
    if request.method=='POST':
        n1=request.form['n1']
        n2=request.form['n2']
        resultado=int(n1)+int(n2)
        form +='<b>{}</b>'.format(resultado)
    return form
        
#debug mode on
if __name__=='__main__':
    app.run(debug = True, port=5000)