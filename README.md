## Here, I practice working with the flask framework.

**Aim:** To Learn `flask` from basic concepts to advanced techniques.

**1. install flask**
```bash
pip install flask
```
**2. code**
```bash
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
```
**3. run server**
```bash
python flaskapp.py
```
**4. running on**
```bash
[python app.py](http://127.0.0.1:5000)
```
