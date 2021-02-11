from flask import Flask, render_template, request, redirect

app = Flask(__name__)#instancia

productos = [] #lista vacía

@app.route("/")#creamos la ruta principal
def principal():
	return render_template("index.html", productos=productos)#dirige al html principal y le asignamos una variable llamda variable en los argumentos

@app.route("/añadir", methods=["GET", "POST"])#creamos otro html con /agregar y ponemos com argumentos los métodos post y get
def añadir():
	if request.method == "GET":#si el metodo es get que enviamos a través de la página
		return render_template("añadir.html")#devolvemos al html /agregar
	else:
		carrito = request.form.get("carrito")
		productos.append(carrito)#añadimos a la lista productos
		return redirect("/")#volvemos al index o página principal


if __name__ == "__main__":
	app.run(debug=True)