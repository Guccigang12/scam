from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Salatik.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        age = request.form.get('RICE')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')

        if age == 'notscam':
            return f"Вам меньше 18 поэтому мы не можем вам помочь"
        else:
            return render_template("scam.html")


if __name__ == '__main__':
    app.run(debug=True)
