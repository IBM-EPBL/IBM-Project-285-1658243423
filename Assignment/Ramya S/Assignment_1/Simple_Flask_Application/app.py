from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

data={}
 
@app.route('/SignUp', methods=['POST'])
def SignUp():
    if request.method == 'POST':
        name = request.form['user_name']
        phone = request.form['user_phone']
        email = request.form['user_email']
        data['name'] = name
        data['phone'] = phone
        data['email'] = email
        return redirect(url_for('Success'))
    else:
        return "<script>alert('error')</script>"

@app.route('/Success')
def Success():
    return render_template('Success.html' ,formdata=data)

if __name__ == '__main__':
	app.run(debug=True)