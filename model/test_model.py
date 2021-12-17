import pickle
import numpy as np

model = pickle.load(open("./model.pkl", 'rb'))
scale_x = pickle.load(open('scaler_x.pkl', 'rb'))
scale_y = pickle.load(open('scaler_y.pkl', 'rb'))

harga = 100000000

y_pred = model.predict(scale_x.transform(np.array([[harga]])))
y_pred2 = scale_y.inverse_transform([y_pred])
harga_jual = int(y_pred2[0][0])
print(harga_jual)
