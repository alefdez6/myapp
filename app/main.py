from flask import jsonify
from flask import Flask
from . import catalog

app = Flask(__name__)

@app.route('/product'
def list_all_products():
    '''This view retrieves all the products in the catalog'''
    response = get_products()
    return jsonify(response)

@app.route('/hello')
def hello_world():
    message = "Hola mundo, soy Python! Ahora con CloudBuild y hablando JSON"
    response = {
            "message": message,
            "length": len(message)
    }
    return jsonify(response)

@app.route('/bye')
def bye_world():
    return ("Adios perro")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



