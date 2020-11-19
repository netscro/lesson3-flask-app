from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)


@app.route('/encrypt')
def encrypt():
    param = request.args.get('param', '')
    string = f.encrypt(param.encode())
    return render_template('index.html', string=string)


@app.route('/decrypt')
def decrypt():
    param = request.args.get('param', '')
    print(param.encode())
    string = f.decrypt(param.encode())
    return render_template('index.html', string=string)


app.run(debug=True)
