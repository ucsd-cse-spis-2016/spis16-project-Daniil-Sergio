import os
from flask import Flask, url_for, render_template, request
import glob, os




app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('main.html')

@app.route('/survey')
def render_survey():
     return render_template('survey.html')

@app.route('/result')


def render_result():
    req = request.args
    results = {}
    for elem in req:
        results[elem] = req[elem].lower()
    
    print(results)
    print check(results)[0]
    if check(results)[0]:
        save_res(results)     
        return render_template('success.html', name = req['first_name'])
    else:
        return render_template('error.html', error = check(results)[1])

def check(arr):
    #print(os.getcwd())
    if in_base(arr['nickname']):
        print('here')
        return False, 'username already exists'

    if arr['nickname'] == '':
            return False, 'required fields should be filled'
    for elem in arr:
        if elem != 'age' and elem != 'nickname':
            if not(arr[elem].isalpha()) and arr[elem] != '':
                return False, 'numbers in a text form'
        if elem == 'age' and not(arr[elem].isdigit()):
            return False, 'letters in a digit form'
                
    return True, 'none'

def save_res(results):
    name = results['nickname'] + '.txt'
    f = open('users/' + name, 'w')
    for elem in results:
       f.write(str(elem) + ' ' + str(results[elem]) + '\n')
    return True

def in_base(name):
    for file in glob.glob("users/*.txt"):
        if str(file.split('.')[0].split('/')[1]) == name:
            print('here')
            return True
    return False

    

@app.route('/gettop5')
def render_gettop5():
    return render_template('gettop5.html')



    
@app.route('/forgot')
def forgot_nickname():
    return render_template('forgot.html')
    

if __name__=="__main__":
    app.run(debug=False,host="128.54.69.248", port=54321)
