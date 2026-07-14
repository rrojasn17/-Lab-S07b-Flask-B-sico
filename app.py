from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return '<h1>Tecnología para la agricultura familiar</h1><p>Laboratorio S07b - Programación IV</p>'


@app.route('/acerca')
def acerca():
    return '<h1>Acerca del estudiante</h1><p>Nombre: Reymond E. Rojas Núñez.</p><p>Espero aprender Flask para crear aplicaciones web sencillas relacionadas con tecnología y agricultura.</p>'


@app.route('/contacto')
def contacto():
    return '<h1>Contacto</h1><p>Correo: reymond.rojas@ejemplo.com</p>'


if __name__ == '__main__':
    app.run(debug=True)
