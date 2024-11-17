# Importamos Flask y las funciones necesarias para manejar rutas y plantillas
from flask import Flask, render_template, request

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta principal (Menú principal)
@app.route('/')
def index():
    # Renderizamos la página de inicio (menú principal)
    return render_template('index.html')

# Ruta para el Ejercicio 1 (Formulario de Notas)
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':  # Si el formulario fue enviado
        # Capturamos los datos ingresados en el formulario
        nota1 = float(request.form['nota1'])  # Convertimos a float porque las notas son numéricas
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Calculamos el promedio de las notas
        promedio = round((nota1 + nota2 + nota3) / 3, 2)

        # Determinamos si el estudiante aprueba o reprueba
        # Para aprobar, debe tener un promedio >= 55 y asistencia >= 75%
        estado = "APROBADO" if promedio >= 55 and asistencia >= 75 else "REPROBADO"

        # Renderizamos el formulario de notas con los resultados
        return render_template('form1.html', promedio=promedio, estado=estado)

    # Si no se ha enviado el formulario, mostramos el formulario vacío
    return render_template('form1.html')

# Ruta para el Ejercicio 2 (Formulario de Nombres)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':  # Si el formulario fue enviado
        # Capturamos los datos ingresados en el formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Creamos una lista con los nombres ingresados
        nombres = [nombre1, nombre2, nombre3]

        # Encontramos el nombre más largo
        nombre_mayor = max(nombres, key=len)  # Usamos la función max() para encontrar el más largo
        longitud = len(nombre_mayor)  # Calculamos la cantidad de caracteres del nombre más largo

        # Renderizamos el formulario de nombres con los resultados
        return render_template('form2.html', nombre_mayor=nombre_mayor, longitud=longitud)

    # Si no se ha enviado el formulario, mostramos el formulario vacío
    return render_template('form2.html')

# Ejecutamos la aplicación Flask
if __name__ == '__main__':
    # Activamos el modo de depuración para ver errores y cambios en tiempo real
    app.run(debug=True)



