import re  # Manejo de expresiones regulares
from datetime import datetime  # Manejo de fechas y horas
import matplotlib.pyplot as plt  # Librería para generar gráficos
import seaborn as sns  # Librería para mejorar la visualización de gráficos
from flask import Flask, render_template, request, send_file  # Flask y funciones para manejar plantillas y solicitudes
from LinealRe import predecir_nota  # Importamos la función de predicción

# Crea la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return "Hello Flask"

# Ruta para saludar con nombre validado
@app.route("/Hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y, %H:%M:%S")

    match_object = re.match(r"^[a-zA-Z ]+$", name)
    clean_name = match_object.group(0) if match_object else "friend"

    content = f"Hello there, {clean_name}! Today is: {formatted_now}"
    return content

# Ruta para mostrar la página de cálculo de notas
@app.route("/hello2", methods=["GET", "POST"])
def helloHTML():
    return render_template("CalculoNota.html")

# Ruta para calcular la nota en base a las horas de estudio
@app.route("/CalculoNota", methods=["GET", "POST"])
def calcular_nota():
    nota_predicha = None
    if request.method == "POST":
        try:
            horas = float(request.form["horas"])  # Convertimos la entrada a número
            nota_predicha = predecir_nota(horas)  # Llamamos a la función de predicción
        except ValueError:
            nota_predicha = "Entrada inválida"  # Si hay error, mostramos mensaje

    return render_template("CalculoNota.html", nota_predicha=nota_predicha)

# Nueva ruta para generar y mostrar el gráfico de predicción
@app.route("/grafico")
def mostrar_grafico():
    # Datos de ejemplo para la gráfica (simulación de predicción)
    horas_estudio = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    notas_predichas = [predecir_nota(h) for h in horas_estudio]  # Calculamos notas para diferentes horas

    # Crear gráfico
    plt.figure(figsize=(8, 5))
    sns.regplot(x=horas_estudio, y=notas_predichas, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
    plt.xlabel("Horas de estudio")
    plt.ylabel("Nota predicha")
    plt.title("Relación entre horas de estudio y nota obtenida")
    plt.grid(True)

    # Guardar el gráfico como imagen
    grafico_path = "static/grafico_prediccion.png"
    plt.savefig(grafico_path)
    plt.close()

    # Mostrar la imagen generada
    return send_file(grafico_path, mimetype="image/png")

# Ruta para la página "caso de uso"
@app.route("/caso_uso")
def caso_uso():
    return render_template("caso_uso.html")

# Ejecutar la aplicación si se ejecuta directamente el script
if __name__ == "__main__":
    app.run(debug=True)