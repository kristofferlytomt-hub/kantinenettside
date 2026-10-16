from flask import Flask, render_template
from data import varer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meny')
def meny():
    return render_template('meny.html')

@app.route('/varer')
def vareside():
    return render_template('varer.html', vareliste=varer)

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')

if __name__ == "__main__":
    app.run()