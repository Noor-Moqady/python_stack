from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def playground():
    return render_template('Playground.html')
@app.route('/play/<num>')
def repeatrender(num):
    return render_template('Playground2.html',num=int(num))
@app.route('/play/<num>/<col>')
def color(num,col):
    return render_template('Playground2.html',num=int(num),col=col)
if __name__ == "__main__":
    app.run(debug=True)
