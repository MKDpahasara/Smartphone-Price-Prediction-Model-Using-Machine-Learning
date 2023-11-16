from flask import Flask
from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__,template_folder='template')
def prediction(lst):
    filename = 'model/prediction_model_1.pickle'
    with open(filename,'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value



@app.route('/',methods=['POST','GET'])
def index():
    pred = 0
    if request.method == 'POST':
        ram_gb = request.form['ram']
        brand = request.form['Brand']
        storage_gb= request.form['Storage']
        screen_size_inch = request.form['Screen Size']
        main_camera_mp = request.form['main_camera(MP)']
        camera_count = request.form['rear cameras count']
        battery_capacity_mah = request.form['Battery Capacity']

        feature_list =[]
        feature_list.append(int(ram_gb))
        feature_list.append(float(screen_size_inch))
        feature_list.append(int(storage_gb))
        feature_list.append(int(main_camera_mp))
        feature_list.append(int(camera_count))
        feature_list.append(int(battery_capacity_mah))

        brand_list = ['Samsung','Xiaomi','Oppo','Realme','Vivo','Apple','Nokia','Motorola','OnePlus','Huawei','Google','other']
        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse_list(brand_list, brand)

        pred = prediction(feature_list)
        pred = pred*-1
        pred = np.round(pred[0])
        print(pred)

        
              
    return render_template('index.html',pred = pred)

if __name__ == '__main__':
    app.run(debug=True)
