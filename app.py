from flask import Flask, request, render_template

app = Flask(__name__)

href = "{{ url_for('static', filename='modern-business.css')}}"


@app.route('/user/<name>')
def index1(name):
    return render_template('Hello {{ name }}', name=name)


@app.route('/')
def index2():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s </p>' % user_agent


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/portfolio_1')
def portfolio1():
    return render_template('stats.html')


@app.route('/item')
def item():
    return render_template('item.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/about')
def user():
    return render_template('about.html')


@app.route('/signuplogin')
def signuplogin():
    return render_template('signuplogin.html')


if __name__ == '__main__':
    app.run()
