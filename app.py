from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)


@app.route('/encrypt')
def encrypt():
    """
    encrypts the string entered in the url parameter --> /encrypt?string=<string_to_encrypt>
    :return: encrypting string
    """
    string = request.args.get('string', '')
    param = f.encrypt(string.encode()).decode()
    return render_template('index.html', string=param)


@app.route('/decrypt')
def decrypt():
    """
    decrypts the string entered in the url parameter --> /decrypt?string=<string_to_decrypt>
    :return: decrypting string
    """
    string = request.args.get('string', '')
    param = f.decrypt(string.encode()).decode()
    return render_template('index.html', string=param)


app.run(debug=True)
