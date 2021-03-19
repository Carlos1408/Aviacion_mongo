from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/hangar')
def hangares():
    return render_template('hangar.html')

@app.route('/persona')
def personas():
    return render_template('persona.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)