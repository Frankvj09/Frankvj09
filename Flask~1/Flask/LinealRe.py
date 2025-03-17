import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from flask import Flask, request, render_template

# Datos de entrenamiento
data = {
    "Study_hours": [10, 20, 30, 40, 50],
    "Final_grade": [38, 40, 44, 45, 50]
}

df = pd.DataFrame(data)

# Definir variables de entrada y salida
x = df[["Study_hours"]]
y = df["Final_grade"]

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(x, y)

# Función para predecir la calificación
def calculate_grade(hours):
    result = model.predict([[hours]])[0]
    return round(result, 2)

# Configurar Flask
app = Flask(__name__)

@app.route("/CalculoNota", methods=["GET", "POST"])
def CalculateGradeExample():
    result = None
    if request.method == "POST":
        hours = float(request.form["hours"])  # Obtener horas del formulario
        result = calculate_grade(hours)  # Llamar a la función de predicción
    return render_template("CalculateGrades.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
