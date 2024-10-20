from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['userid']
        password = request.form['password']
        # Implement your registration logic here
        # For now, we will just redirect to a success page
        return redirect(url_for('success', userid=user_id))
    return render_template('login.html')

@app.route('/success/<userid>')
def success(userid):
    return f"Welcome, {userid}! You have successfully registered."

if __name__ == '__main__':
    app.run(debug=True)

