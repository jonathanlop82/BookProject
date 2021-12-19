from flask import Flask, render_template, request #Importando la libreria Flask

app = Flask(__name__) #Creando una variable para crear nuestra aplicacion utilizando la instancia de Flask


@app.before_request
def before_request():
    print('Antes de la peticion...')


@app.after_request
def after_request(response):
    print('Despues de la peticion...')

    return response

# @app.route('/') #Respuesta que se obtenga cuando accedemos a ruta raiz
# def index():
#     return "CodigoFacilito"

# @app.route('/contact')
# def contact():
#     return "Pagina de Contactos"

##Otra forma de indexar una pagina
def index():
    print('Estamos realizando la peticion....')
    #return "Pagina de Index"
    data = {
        'titulo':'index',
        'encabezado':'Bienvenido'
    }
    return render_template('index.html',data=data)

@app.route('/contacto')
def contact():
    #return "Pagina de Index"
    data = {
        'titulo':'contacto',
        'encabezado':'Contacto'
    }
    return render_template('contact.html',data=data)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    #return (f'Hola, {nombre}!')
    return 'Hola, {0}!'.format(nombre)

@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1,valor2):
    return 'La suma de los valores es: {0}'.format(valor1 + valor2)

@app.route('/lenguajes')
def lenguajes():
    data = {
        'hay_lenguajes': True,
        'lenguajes':['PHP','Python','Kotlin','Java','C#','JavaScript']
    }
    return render_template('lenguajes.html',data=data)

@app.route('/HolaMundo')
def hola_mundo():
    return "Hola Mundo!"

# HTTP: HyperText Transfer Protocol
# GET, POST, PUT, DELETE

@app.route('/datos')
def datos():
    print(request.args)
    valor1=request.args.get('valor1') #Se guarda en la variable valor1 , el dato que contenga el argumento con llave valor1 ?valor1=Python
    b = int(request.args.get('valor2'))
    return 'Estos son los datos: {0} {1}'.format(valor1,b+1)


if __name__ == '__main__': #Lanzar la aplicacion como principal para iniciar el servidor mediante el medoto run
    app.add_url_rule('/',view_func=index)
    #app.add_url_rule('/contacto',view_func=contact)
    app.run(debug=True, port=5005)