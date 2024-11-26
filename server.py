from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template('simple.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')

    print(f"Received: Name - {name}, Email - {email}")

    return render_template('result.html', name=name, email=email)



if __name__ == '__main__':
    app.run(port=5001)
