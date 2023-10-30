from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/visits')
def counter():
    
    if  'count' not in session:
        session['count']=1
        session['people']= "noor"
    
    else:
        session['count']+=1

    return render_template('counter.html')

@app.route('/addcount')
def counter2():
    
    if  'count' not in session:
        session['count']=1
    else:
        session['count']+=2

    return render_template('counter.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/visits')

@app.route('/delete')
def delete():
    session.pop('count')
    
    print(session['people'])
    return redirect ('/visits')


if __name__ == "__main__":
    app.run(debug=True)