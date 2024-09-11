from flask import Flask, request, jsonify, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def Dashboard():
    return render_template("Dashboard.html")
@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/Solarcalc')
def Solarcalc():
    return render_template("Solarcalc.html")
@app.route('/procument')
def procument():
    return render_template("procument.html")
@app.route('/solardatas')
def solardatas():
    return render_template("solardatas.html")
@app.route('/sundatas')
def sundatas():
    return render_template("sundatas.html")
@app.route('/Graph')
def Graph():
    return render_template("Graph.html")
@app.route('/Contact')
def Contact():
    return render_template("Contact.html")









@app.route('/success/<int:score>')
def success(score):
    return "Pass : " + str(score)

@app.route('/check/<int:mark>')
def check(mark):
    if(mark>50):
        return redirect(url_for('success', score=mark))
    return render_template("index.html")

@app.route('/submit-data', methods=['POST'])
def submit_data():
    # data = request.get_json()
    # name = data.get('name')
    # age = data.get('age')
    # return "Received ${age} and ${name}"
    return render_template("index.html")
    #return jsonify({'message': f'Received data for {name}, age {age}'})


if __name__ == '__main__':
   app.run(debug=True)

# $env:FLASK_APP = "Backend"
# set FLASK_APP=Backend
# cd 'c:\Users\user\OneDrive\Desktop\SIH-GIT'
#& 'c:\Users\user\OneDrive\Desktop\SIH-GIT\.venv\Scripts\python.exe' -m flask run --no-debugger --no-reload





# {
#     // Use IntelliSense to learn about possible attributes.
#     // Hover to view descriptions of existing attributes.
#     // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
#     "version": "0.2.0",
#     "configurations": [
#         {
#             "name": "Python Debugger: Flask",
#             "type": "debugpy",
#             "request": "launch",
#             "module": "flask",
#             "env": {
#                 "FLASK_APP": "Backend.py",
#                 "FLASK_DEBUG": "1"
#             },
#             "args": [
#                 "run",
#                 "--no-debugger",
#                 "--no-reload"
#             ],
#             "jinja": true,
#             "autoStartBrowser": false
#         }
#     ]
# }