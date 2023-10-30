from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'


@app.route('/form')
def form():
    return render_template('Dojo_Survey.html')
@app.route('/result',methods=['POST'])
def result():
    session['x'] =request.form['name']
    session['y'] =request.form['Dojo Location']
    session['z'] =request.form['favorite language']
    session['w'] =request.form['comment']
    session['f'] =request.form.get('gender')
    session['n'] = "Yes" if 'email_updates' in request.form else "No"
    return redirect('/result2')
@app.route('/result2')
def result2():
    return render_template('submit_info.html')
if __name__ == "__main__":
    app.run(debug=True)
