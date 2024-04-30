from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página principal
@app.route('/')
def hello():
    return '¡Hola Mundo lo logre MAXIMO!'

# Ejecutar la aplicación en el puerto 443 (requiere permisos de administrador)
if __name__ == '__main__':
    app.run(debug=True, port=443, host='0.0.0.0', ssl_context='adhoc')

