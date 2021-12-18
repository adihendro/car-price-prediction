
import flask
from flask.helpers import send_from_directory
import numpy as np
import pickle
from flask import request


model = pickle.load(open("model/model.pkl", 'rb'))
scale_x = pickle.load(open('model/scaler_x.pkl', 'rb'))
scale_y = pickle.load(open('model/scaler_y.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='view',
                  static_url_path="", static_folder="view")


@app.route('/')
def main():
    return(flask.render_template('index.html'))


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    data = request.form
    # print(data["harga"])

    int_features = int(flask.request.form.get('harga'))
    y_pred = model.predict(scale_x.transform(np.array([[data["harga"]]])))
    y_pred2 = scale_y.inverse_transform([y_pred])
    harga_jual = int(y_pred2[0][0])

    return flask.render_template('result.html', profit='{}'.format(harga_jual), sell='{}'.format(harga_jual+int_features))


@app.route("/view/css/<path:path>")
def send_css(path):
    return send_from_directory('view/css', path)


@app.route("/view/js/<path:path>")
def send_js(path):
    return send_from_directory('view/js', path)


if __name__ == '__main__':
    app.run(debug=True)
