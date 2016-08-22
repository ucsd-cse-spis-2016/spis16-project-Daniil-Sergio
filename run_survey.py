import os
from flask import Flask, url_for, render_template, request
import time




app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('main.html')

@app.route('/survey')
def render_survey():
     return render_template('survey.html')

@app.route('/result')


def render_result():
    results = request.args
    print(results)
    print check(results)[0]
    if check(results)[0]:
        save_res(results)     
        return render_template('success.html', name = results['first_name'])
    else:
        return render_template('error.html', error = check(results)[1])

def check(arr):
    for elem in arr:
        if elem != 'age' and elem != 'nickname':
            if not(arr[elem].isalpha()):
                return False, 'numbers in a text form'
        if arr[elem] == 'required' or arr[elem] == 'optional':
            return False, 'required or optional should be deleted'
        
    return True, 'none'

def save_res(results):
    name = results['nickname'] + time.strftime("%d_%m_%Y") + '.txt'
    f = open(name, 'w')
    for elem in results:
        f.write(str(elem) + ' ' + str(results[elem]) + '\n')


@app.route('/gettop5')
def render_gettop5():
    return render_template('gettop5.html')



    
#@app.route('/forgot')

if __name__=="__main__":
    app.run(debug=False,host="128.54.69.248", port=54321)
