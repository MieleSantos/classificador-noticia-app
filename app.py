from flask import Flask, jsonify, request, render_template
from joblib import load

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():

    predictin =''
    
    if request.method == 'POST':
        query = request.form['query']    
        predictin = process_model(query)

    return render_template('index.html',predictin=predictin)


def process_model(query):

    model_class= ['carros', 'economia', 'educacao', 'esporte', 'musica', 'politica']
    #carregando modelo
    model = load("./modelo/classificador_model.joblib")

    #enviado dados para modelo
    predict = model.predict([query])

    #pegando a classificador identificada pelo modelo
    predictin = model_class[predict[0]]

    return predictin


if __name__ == "__main__":
    app.run(debug=True)