from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página principal
@app.route('/')
def hello():
    return '¡Hola Mundo!'

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

