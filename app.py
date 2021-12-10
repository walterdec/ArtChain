from flask import Flask, request, render_template

app = Flask(__name__)


# href = "{{ url_for('static', filename='modern-business.css')}}"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/item')
def item():
    return render_template('item.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/explore-nfts')
def explore_nfts():
    return render_template('explore-nfts.html')


@app.route('/explore-crypto')
def explore_crypto():
    return render_template('explore-crypto.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/myaccount-mywallet')
def my_wallet():
    return render_template('myaccount-mywallet.html')


@app.route('/myaccount-settings')
def my_settings():
    return render_template('myaccount-settings.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signupartist')
def signupartist():
    return render_template('signupartist.html')


@app.route('/signupcustomer')
def signupcustomer():
    return render_template('signupcustomer.html')


@app.route('/404')
def pagenotfound():
    return render_template('404.html')


if __name__ == '__main__':
    app.run()