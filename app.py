from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return ('Hi')

@app.route('/name')
def hey():
    return ('How are you')


if __name__ =='__main__':
    app.run()