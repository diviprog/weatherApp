from flask import Flask, render_template, request
app = Flask(__name__)

import urllib.request
import json

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        city = request.form['city']
    else :
        city = "Bangalore" #default city is Bangalore

    api = "997ea79e1c9575bd4f087cf90e68205d"
    #api = "3516a72eb69f779a9c0e683d651fc1c2"
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api
    source = urllib.request.urlopen(url).read()
    print (source)

    list_of_data = json.loads(source)

    data = {
        "country_code":"IN",
        "temp":str(round((list_of_data['main']['temp'] - float(273)), 2)),
        "humidity":str(list_of_data['main']['humidity']),
        "city_name":str(list_of_data['name']),
        "lon":str(list_of_data['coord']['lon']),
        "lat":str(list_of_data['coord']['lat']),
    }

    return render_template('index.html', data=data)

@app.route('/user')
def user ():
    return '<h6> Hello there! </h6>'

if __name__ == '__main__':
    app.run(debug=True)

#api = "997ea79e1c9575bd4f087cf90e68205d"