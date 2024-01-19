from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def homes():
    msg = ''
    return render_template('login.html', msg = msg)

# @app.route('/signup')
# def homes():
#     msg = ''
#     return render_template('signup.html', msg = msg)

if __name__== "__main__" :
    app.run(debug = True)
