from flask import Flask, request, jsonify, make_response
from helper import Datahelper
import json

app = Flask("__init__")

# Domyślnie w roocie dostajemy wszystkie dane
@app.route('/')
def index():
    data = Datahelper("data.json").get_data()
    response = make_response(jsonify(data),200,)
    response.headers["Content-Type"] = "application/json"
    return response

# Endpoint /users/ z query i metodą GET
@app.route('/users/', methods=["GET"])
def api():
    # Wyciągamy "name" z requesta
    name = request.args.get("name")
    # Jeżeli rzeczywiście został podany parametr "name" to przetwarzamy dane
    if name != None:
        # Bierzemy dane z jsona
        data = Datahelper("data.json").get_data()
        for obj in data:
            # Jeżeli istnieje obiekt z pasujacym "name" to zwracamy
            if obj["name"] == name:
                response = make_response(jsonify([obj]),200,)
                response.headers["Content-Type"] = "application/json"
                return response

    # Jeżeli NIE został podany parametr name (literowka/inny parametr) to zwracamy pusty json array
    response = make_response(jsonify([]),200,)
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == "__main__":
    app.run(debug=True)