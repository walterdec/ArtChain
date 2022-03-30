from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from sqlalchemy.orm import Session

from form import LoginForm, CustomerRegistrationForm, ArtistRegistrationForm, ForgotPasswordForm, EditArtistForm, \
    EditCustomerForm, NewNFTForm
import model

# from model import User, Auction, NFT, CryptoOnSale, Wallet da errore, uso import model per aggirare

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardtoguess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artchain.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CSRFProtect(app)


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


@app.route('/myaccount-profile', methods=['GET', 'POST'])
def my_settings():
    form = None
    email_edit_successful = 0
    email_already_existing = 0
    password_edit_successful = 0
    try:
        if session['username']:
            user = session['username']
            for row in db.session.query(model.User).filter_by(username=user):
                user_logged_in = row
            if user_logged_in.role_id == 3:
                form = EditArtistForm()
            else:
                form = EditCustomerForm()

        if form.validate_on_submit():
            user = db.session.query(model.User).filter_by(email=request.form['email']).first()
            if user:
                if user != user_logged_in:
                    email_already_existing = 1

            elif email_already_existing == 0:
                user_logged_in.email = request.form['email']
                db.session.commit()
                email_edit_successful = 1

            if form.password.data is not None and form.password.data == form.confpassword.data:
                user_logged_in.password = form.password.data
                db.session.commit()
                password_edit_successful = 1

            return render_template('myaccount-profile.html', form=form, user_logged_in=user_logged_in,
                                   email_edit_successful=email_edit_successful,
                                   email_already_existing=email_already_existing,
                                   password_edit_successful=password_edit_successful)

    except KeyError:
        return redirect(url_for('index'))

    return render_template('myaccount-profile.html', form=form, user_logged_in=user_logged_in)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    login_error = 0
    if form.validate_on_submit():
        for row in db.session.query(model.User).filter_by(username=request.form['username']):
            user = row
            if user.password == request.form['password']:
                username = form.username.data
                session['username'] = username
                return redirect(url_for('index'))
        else:
            login_error = 1
    return render_template('login.html', form=form, login_error=login_error)


@app.route('/signupartist', methods=['GET', 'POST'])
def signupartist():
    session.clear()
    form = ArtistRegistrationForm()
    artist_categories = ['Musician', 'Sketcher', 'Other']
    unique_db_error = 0
    registration_success = 0
    is_musician = 0
    if form.validate_on_submit() and form.password.data == form.confpassword.data:
        if (model.User.query.filter(model.User.username == request.form['username']).first() or
                model.User.query.filter(model.User.email == request.form['email']).first()):
            unique_db_error = 1
            return render_template('signupartist.html', form=form, artist_categories=artist_categories,
                                   registration_success=registration_success, unique_db_error=unique_db_error)
        else:
            if form.category.data == 'Musician':
                is_musician = 1

            artist_registration = model.User(username=form.username.data, email=form.email.data,
                                             password=form.password.data, role_id=3, name=form.name.data,
                                             surname=form.surname.data, is_musician=is_musician,
                                             insta=int(form.instafollowers.data or 0), instaname=form.instauser.data,
                                             face=int(form.facefollowers.data or 0), facename=form.faceuser.data,
                                             twitter=int(form.twitterfollowers.data or 0),
                                             twittername=form.twitteruser.data,
                                             yt=int(form.ytfollowers.data or 0), ytname=form.ytuser.data,
                                             tiktok=int(form.tiktokfollowers.data or 0),
                                             tiktokname=form.tiktokuser.data,
                                             twitch=int(form.twitchfollowers.data or 0),
                                             twitchname=form.twitchuser.data,
                                             applemusic=int(form.applemusicfollowers.data or 0),
                                             applemusicname=form.applemusicuser.data,
                                             spotify=int(form.spotifyfollowers.data or 0),
                                             spotifyname=form.spotifyuser.data,
                                             soundcloud=int(form.soundcloudfollowers.data or 0),
                                             soundcloudname=form.soundclouduser.data, sales=int(form.sales.data or 0))
            db.session.add(artist_registration)
            db.session.commit()
            registration_success = 1

    return render_template('signupartist.html', form=form, artist_categories=artist_categories,
                           registration_success=registration_success, unique_db_error=unique_db_error)


@app.route('/signupcustomer', methods=['GET', 'POST'])
def signupcustomer():
    session.clear()
    form = CustomerRegistrationForm()
    username = None
    unique_db_error = 0
    registration_success = 0
    if form.validate_on_submit() and form.password.data == form.confpassword.data:
        username = form.username.data
        if (model.User.query.filter(model.User.username == request.form['username']).first() or
                model.User.query.filter(model.User.email == request.form['email']).first()):
            unique_db_error = 1
        else:
            customer_registration = model.User(username=form.username.data, email=form.email.data,
                                               password=form.password.data, role_id=2)
            db.session.add(customer_registration)
            db.session.commit()
            registration_success = 1

    return render_template('signupcustomer.html', form=form, name=username, unique_db_error=unique_db_error,
                           registration_success=registration_success)


@app.route('/new-nft')
def new_nft():
    form = NewNFTForm()
    for row in db.session.query(model.User).filter_by(username=session['username']):
        user_logged_in = row
    return render_template('new-nft.html', user_logged_in=user_logged_in, form=form)


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


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = ForgotPasswordForm()
    wrong_email = 0
    email_sent = 0
    if form.validate_on_submit():
        if model.User.query.filter(model.User.email == request.form['email']).first():
            email_sent = 1
        else:
            wrong_email = 1

    return render_template('forgot.html', form=form, email_sent=email_sent, wrong_email=wrong_email)


@app.route('/delete')
def delete():
    if session['username']:
        for row in db.session.query(model.User).filter_by(username=session['username']):
            user_to_delete = row
        db.session.delete(user_to_delete)
        db.session.commit()
    session.clear()
    return redirect('/index')


if __name__ == '__main__':
    app.run()
