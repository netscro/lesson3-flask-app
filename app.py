from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)


@app.route('/encrypt')
def encrypt():
    string = request.args.get('string', '')
    param = f.encrypt(string.encode()).decode()
    return render_template('index.html', string=param)


@app.route('/decrypt')
def decrypt():
    string = request.args.get('string', '')
    print(string.encode())
    param = f.decrypt(string.encode()).decode()
    return render_template('index.html', string=param)


app.run(debug=True)
