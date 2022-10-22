from flask import Flask,redirect, render_template, request
from Connection import Connect 
import Const
 
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

conn = Connect.Connection()

#SignUp page
@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        email = str(request.form.get("Email"))
        name = str(request.form.get("Name"))
        phone = str(request.form.get("Phone"))
        password = str(request.form.get("Password"))
        flag = Connect.Create(email,name,phone,password,conn)
        if(flag == 1):
            print("Success")
            return redirect('/Signin')
        else:
            print("Error while insert")

    return render_template('Signup.html')

#SignIn Page
@app.route('/Signin' , methods =["GET", "POST"])
def Signin():
    error = None
    if request.method == "POST":
        email = str(request.form.get("UEmail"))
        password = str(request.form.get("UPassword"))
        flag = Connect.Signin(email,password,conn)
        if(flag != 0):
            print("Login Success")
            Const.User_Name=flag[0]
            Const.User_Email=flag[1]
            Const.User_Phone=flag[2]
            return redirect('/Dashboard')
        else:
            error = "Invalid Email or Password"  
            print("Email or Password Incorrect !")
    return render_template('Signin.html',error=error)

#Dashboard Page
@app.route('/Dashboard')
def Dashboard():
    return render_template('Home.html',user = Const)
 
if __name__=='__main__':
    # print(conn = Connect.Connection())
    # print(Connect.Create(email,name,phone,password,conn))
    # print(Connect.Signin(conn,"rk9166771@gmail.com","123456789"))
    app.run(debug = True)