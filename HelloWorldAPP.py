from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página principal
@app.route('/')
def hello():
    return '¡Hola Mundo lo logre EN CONTAINER FINAL!'

# Ejecutar la aplicación en el puerto 443 (requiere permisos de administrador)
if __name__ == '__main__':
    app.run(debug=False, port=443, host='0.0.0.0', ssl_context='adhoc')

