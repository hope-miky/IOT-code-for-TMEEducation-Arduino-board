from flask import Flask
from flask import render_template
import firebaseClass
firebdata = 0.0
from datetime import time
from time import sleep
fc = firebaseClass.FireB()
btnstate = ""

app = Flask(__name__)
@app.route('/')
def hello():
    firebdata = fc.getTemprature()
    print(firebdata)
    firebdata = float(firebdata)

    #print('esfat')
    return render_template('home.html', value = firebdata)

@app.route("/btnled/", methods=['POST'])
def move_forward():
    #Moving forward code
    firebdata = fc.getTemprature()
    if fc.getLight() == '1':
        fc.setLight(0)
        btnstate = "OFF"
    elif fc.getLight() == '0':
        fc.setLight(1)
        btnstate = "ON"
    return render_template('home.html', btnst = btnstate, value = firebdata);

@app.route("/temp/", methods=['POST'])
def move_fd():
    firebdata = fc.getTemprature()
    if fc.getLight() == '1':
        btnstate = "ON"
    elif fc.getLight() == '0':
        btnstate = "OFF"
    return render_template('home.html', value = firebdata, btnst = btnstate)



@app.route("/time_chart")
def time_chart():
    legend = 'Temperatures'
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = [time(hour=11, minute=14, second=15),
             time(hour=11, minute=14, second=30),
             time(hour=11, minute=14, second=45),
             time(hour=11, minute=15, second=00),
             time(hour=11, minute=15, second=15),
             time(hour=11, minute=15, second=30),
             time(hour=11, minute=15, second=45),
             time(hour=11, minute=16, second=00),
             time(hour=11, minute=16, second=15),
             time(hour=11, minute=16, second=30),
             time(hour=11, minute=16, second=45),
             time(hour=11, minute=17, second=00),
             time(hour=11, minute=17, second=15),
             time(hour=11, minute=17, second=30),
             time(hour=11, minute=17, second=45),
             time(hour=11, minute=18, second=00),
             time(hour=11, minute=18, second=15),
             time(hour=11, minute=18, second=30)]
    return render_template('time_chart.html', values=temperatures, labels=times, legend=legend)

# run the application
if __name__ == "__main__":
    app.run(debug=True)


