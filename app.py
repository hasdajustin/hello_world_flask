from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        name = request.form['name'] 
        return render_template('pages/welcome.html', name=name)
    return render_template('pages/page2.html')

if __name__ == '__main__':
    app.run(debug=True)