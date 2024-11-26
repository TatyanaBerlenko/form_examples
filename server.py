from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template('bootstrap_example.html')


@app.route('/save', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')

    print(f"Received: Name - {name}, Email - {email}")

    return render_template('result.html', name=name, email=email)


@app.route('/submit_bootstrap', methods=['POST'])
def submit_bootstrap_form():
    email = request.form.get('email')
    password = request.form.get('password')
    checked = request.form.get('checked')
    print(f"Received: Email - {email}")
    print(f"Received: Password - {password}")
    print(f"Received: is checked - {checked}")

    return f"Received: Email: {email}, Checkbox: {'Yes' if checked else 'No'}"




if __name__ == '__main__':
    app.run(port=5001)
