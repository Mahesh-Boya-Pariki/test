from flask import Flask

app=Flask(__name__)
#
@app.route('/')
def hello():
    return "Hello!"

@app.route('/profile')
def profile():
    return "New"

@app.route('/user/<username>')
def user(username):
    return "Hi %s"%username

@app.route('/post/<int:id>')
def post(id):
    return "Id is %s"%id

app.run(debug=True)
