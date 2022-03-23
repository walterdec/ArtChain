from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from form import LoginForm, CustomerRegistrationForm, ArtistRegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardtoguess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artchain.db'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#from model import User, Auction, NFT, CryptoOnSale, Wallet da errore, uso import model per aggirare

import model


@app.before_first_request
def setup_db():
    session.clear()
    db.drop_all()
    db.create_all()


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


@app.route('/myaccount-profile')
def my_settings():
    return render_template('myaccount-profile.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/signupartist', methods=['GET', 'POST'])
def signupartist():
    form = ArtistRegistrationForm()
    artist_categories = ['Musician', 'Sketcher', 'Other']
    if form.validate_on_submit() and form.password.data == form.confpassword.data:
        print("gin")
        return redirect(url_for('index'))
    return render_template('signupartist.html', form=form, artist_categories=artist_categories)


@app.route('/signupcustomer', methods=['GET', 'POST'])
def signupcustomer():
    form = CustomerRegistrationForm()
    username = None
    if form.validate_on_submit() and form.password.data == form.confpassword.data:
        username = form.username.data
        session['username'] = username
        return redirect(url_for('index'))

    return render_template('signupcustomer.html', form=form, name=username)


@app.route('/new-nft')
def new_nft():
    return render_template('new-nft.html')


@app.route('/profile-page')
def artist_profile():
    return render_template('profile-page.html')


@app.route('/crypto')
def crypto():
    return render_template('crypto.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/index')


@app.route('/404')
def pagenotfound():
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
