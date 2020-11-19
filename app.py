from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)


@app.route('/encrypt')
def encrypt():
    string = request.args.get('string', '')
    token = f.encrypt(string.encode())
    original_token = token.decode()
    d = f.decrypt(token).decode()
    return render_template('index.html', original_token=original_token, string=d)


app.run(debug=True)
