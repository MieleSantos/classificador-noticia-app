from flask import Flask, jsonify, request
from joblib import load

app = Flask(__name__)

@app.route("/")
def index():

    if "query" not in request.args:
        return jsonify({"Prediction": None, "message":"Send me a text"})
    
    query= request.args.get("query")
    
    #pegando a classificador identificada pelo modelo
    predictin = process_model(query)

    return jsonify({"prediction": predictin})

def process_model(query):

    model_class= ['carros', 'economia', 'educacao', 'esporte', 'musica', 'politica']
    #carregando modelo
    model = load("./modelo/classificador_model.joblib")

    #enviado dados para modelo
    predict = model.predict([query])

    #pegando a classificador identificada pelo modelo
    predictin = model_class[predict[0]]

    return predictin
