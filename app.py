
import flask
import numpy as np
import pickle
import numpy as np

model = pickle.load(open("model/model.pkl", 'rb'))
scale_x = pickle.load(open('model/scaler_x.pkl', 'rb'))
scale_y = pickle.load(open('model/scaler_y.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='view')


@app.route('/')
def main():
    return(flask.render_template('index.html'))


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    int_features = int(flask.request.form.get('harga'))
    y_pred = model.predict(scale_x.transform(np.array([[harga]])))
    y_pred2 = scale_y.inverse_transform([y_pred])
    harga_jual = int(y_pred2[0][0])

    return flask.render_template('result.html', prediction_text='{}'.format(harga_jual))


if __name__ == '__main__':
    app.run(debug=True)
