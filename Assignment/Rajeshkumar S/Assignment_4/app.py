from flask import Flask,redirect, render_template, request
 
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

#Index page
@app.route('/',)
def index():
    return render_template('index.html',)

if __name__=='__main__':
    app.run(debug = True)