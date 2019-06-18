from flask import Flask, request, redirect, url_for, flash, jsonify,Response, render_template
from flask_cors import CORS
from googletrans import Translator  # Import Translator module from googletrans package



app = Flask(__name__)
#CORS(app)


@app.route('/')
def index():
    return render_template('mysvr.html')

@app.route('/callapi', methods=['POST'])
def callmyapi():
    content = request.form['ct']
    translator = Translator()  # Create object of Translator.
    translated = translator.translate(content,src="en",dest="vi")
    return translated.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


