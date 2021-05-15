
################## Imports
#Flask Server Impt
from flask import Flask, render_template, request
import datetime
import sys

import RPi.GPIO as GPIO
import time

in1 = 12
in2 = 16
in3 = 18
in4 = 22
in5 = 32
in6 = 36
in7 = 38
in8 = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(in5, GPIO.OUT)
GPIO.setup(in6, GPIO.OUT)
GPIO.setup(in7, GPIO.OUT)
GPIO.setup(in8, GPIO.OUT)

GPIO.output(in1, False)
GPIO.output(in2, False)
GPIO.output(in3, False)
GPIO.output(in4, False)
GPIO.output(in5, False)
GPIO.output(in6, False)
GPIO.output(in7, False)
GPIO.output(in8, False)


################## Flask Server 
sys.path = ['./lib'] + sys.path

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%d-%m-%Y %H:%M")
    templateData = {
      'title' : 'Basic Pi Smart Switch / Relay Control',
      'time': timeString
      }
    return render_template('index.html', **templateData);


@app.route('/ajax', methods=['POST'])
def ajax():
    
    if(request.form['data'] == 'OneOn'):
        GPIO.output(in1, True)
        return 'do something'

    elif(request.form['data'] == 'OneOff'):
        GPIO.output(in1, False)
        return 'do something else'

    elif(request.form['data'] == 'TwoOn'):
        GPIO.output(in2, True)
        return 'do something else'

    elif(request.form['data'] == 'TwoOff'):
        GPIO.output(in2, False)
        return 'do something else'

    elif(request.form['data'] == 'ThreeOn'):
        
        print('Sending Command /"takeoff/" to the tello')
        return 'do something else'

    elif(request.form['data'] == 'FourOn'):
        
        print('land')
        return 'do something else'

    elif(request.form['data'] == 'FiveOn'):
        
        print('land')
        return 'do something else'


    return 'invalid command'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
#    app.run(debug=True, host='0.0.0.0')  #Debug Mode
