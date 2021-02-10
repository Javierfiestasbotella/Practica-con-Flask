from flask import Flask, render_template, request #importamos el render_template para el index html y Flask

app=Flask(__name__) # creamos la instancia de Flask donde va a estar toda nuestra aplicacion
@app.route("/")#con esto creamos nuestra ruta y ponemos / porque se supone que esta es nuestra página principal
def principal():
    return render_template("index.html")#aquí ingresamos el archivo html que tenemos dentro del directorio Templates. en este caso la ruta es: http://127.0.0.1:5000/

@app.route("/segunda")#con un nombre despues de / podemos ir a una subpágina. http://127.0.0.1:5000/segunda
def frase():
    return " hola a todos"#enviamos un mensaje u otro html

@app.route("/rellenar")# en esta simplemente presentamos un html donde vamos a enviar por metodo post 
def relleno():
    return render_template("rellenar.html")


@app.route("/registro", methods=["POST"])#incluimos el metodo post porque por defecto pone el GET que no nos interesa ahora
def registro():
    nombre=request.form.get("nombre")#damos nombre al request que ha sido importado arriba
    return render_template("registro.html",nombre=nombre)#damos valor a la variable nombre a otro nombre del hatml

@app.route("/ejemplo") #ejecutamos otra ruta con ejemplo detras de slash / "http://127.0.0.1:5000/ejemplo"
def ejemplo_variable_for(): # función
    variable=[9,8,7,6,5,4,3] #una lista con nombre de variables
    return render_template("ejemplo.html",variable=variable) # junto al templates de la pagina html como argumento la variable con comas

if __name__ == '__main__':
    app.run(debug=True)