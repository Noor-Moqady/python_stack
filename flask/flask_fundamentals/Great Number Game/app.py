from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secret key of your choice

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    return render_template('index.html', message='Guess a number between 1 and 100.')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    session['attempts'] += 1

    if guess < session['number']:
        message = 'Too low, try again!'
    elif guess > session['number']:
        message = 'Too high, try again!'
    else:
        message = f'Congratulations! You guessed the number {session["number"]} in {session["attempts"]} attempts.'
        session.pop('number')
    
    return render_template('index.html', message=message)

@app.route('/reset')
def reset():
    session.pop('number')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
