from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_mail import Message, Mail

from form import LoginForm, CustomerRegistrationForm, ArtistRegistrationForm, ForgotPasswordForm, EditArtistForm, \
    EditCustomerForm, NewNFTForm
import model

# from model import User, Auction, NFT, CryptoOnSale, Wallet da errore, uso import model per aggirare

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardtoguess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artchain.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'service.artchain@gmail.com'
app.config['MAIL_PASSWORD'] = 'ISPolitecnicoGroup6'
app.config['MAIL_USE_TLS'] = True

db = SQLAlchemy(app)

mail = Mail(app)

CSRFProtect(app)


def send_mail(to, subject, template, **kwargs):
    msg = Message(subject, recipients=[to], sender=app.config['MAIL_USERNAME'])
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


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
    email_already_existing = 0
    settings_edited = 0
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
                settings_edited = 1

            password = form.password.data
            if password != '' and form.password.data == form.confpassword.data:
                encrypted_password = generate_password_hash(form.password.data)
                user_logged_in.password = encrypted_password
                db.session.commit()
                settings_edited = 1

            if user_logged_in.role_id == 3:
                if form.instafollowers.data is not None:
                    user_logged_in.insta = request.form['instafollowers']
                    db.session.commit()
                    settings_edited = 1
                if form.facefollowers.data is not None:
                    user_logged_in.face = request.form['facefollowers']
                    db.session.commit()
                    settings_edited = 1
                if form.twitterfollowers.data is not None:
                    user_logged_in.twitter = request.form['twitterfollowers']
                    db.session.commit()
                    settings_edited = 1
                if form.ytfollowers.data is not None:
                    user_logged_in.yt = request.form['ytfollowers']
                    db.session.commit()
                    settings_edited = 1
                if form.tiktokfollowers.data is not None:
                    user_logged_in.tiktok = request.form['tiktokfollowers']
                    db.session.commit()
                    settings_edited = 1
                if form.twitchfollowers.data is not None:
                    user_logged_in.twitch = request.form['twitchfollowers']
                    db.session.commit()
                    settings_edited = 1

                if user_logged_in.category == 'Musician':
                    if form.applemusicfollowers.data is not None:
                        user_logged_in.applemusic = request.form['applemusicfollowers']
                        db.session.commit()
                        settings_edited = 1
                    if form.spotifyfollowers.data is not None:
                        user_logged_in.spotify = request.form['spotifyfollowers']
                        db.session.commit()
                        settings_edited = 1
                    if form.soundcloudfollowers.data is not None:
                        user_logged_in.soundcloud = request.form['soundcloudfollowers']
                        db.session.commit()
                        settings_edited = 1

                if form.sales.data is not None:
                    user_logged_in.sales = request.form['sales']
                    db.session.commit()
                    settings_edited = 1

                calculate_artist_value(user_logged_in)

            return render_template('myaccount-profile.html', form=form, user_logged_in=user_logged_in,
                                   email_already_existing=email_already_existing,
                                   settings_edited=settings_edited)

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
            if check_password_hash(user.password, request.form['password']):
                username = form.username.data
                session['username'] = username
                return redirect(url_for('index'))
        else:
            login_error = 1
    return render_template('login.html', form=form, login_error=login_error)


@app.route('/artist-registration', methods=['GET', 'POST'])
def artist_registration():
    session.clear()
    form = ArtistRegistrationForm()
    unique_db_error = 0
    registration_success = 0
    if form.validate_on_submit() and form.password.data == form.confpassword.data:
        if (model.User.query.filter(model.User.username == request.form['username']).first() or
                model.User.query.filter(model.User.email == request.form['email']).first()):
            unique_db_error = 1
            return render_template('artist-registration.html', form=form, registration_success=registration_success,
                                   unique_db_error=unique_db_error)
        else:
            insta = int(form.instafollowers.data or 0)
            face = int(form.facefollowers.data or 0)
            twitter = int(form.twitterfollowers.data or 0)
            yt = int(form.ytfollowers.data or 0)
            tiktok = int(form.tiktokfollowers.data or 0)
            twitch = int(form.twitchfollowers.data or 0)
            applemusic = int(form.applemusicfollowers.data or 0)
            spotify = int(form.spotifyfollowers.data or 0)
            soundcloud = int(form.soundcloudfollowers.data or 0)
            sales = int(form.sales.data or 0)

            if form.category.data == 'Musician':
                value_c = ((insta * 0.3 + face * 0.2 + twitter * 0.2 + yt * 0.1 + tiktok * 0.1 + twitch * 0.1) * 0.5 +
                           (applemusic * 0.4 + spotify * 0.4 + soundcloud * 0.2) * 0.3 + sales * 0.2)
            else:
                value_c = ((insta * 0.3 + face * 0.2 + twitter * 0.2 + yt * 0.1 + tiktok * 0.1 + twitch * 0.1) * 0.8 +
                           + sales * 0.2)

            encrypted_password = generate_password_hash(form.password.data)

            artist_reg = model.User(username=form.username.data, email=form.email.data,
                                    password=encrypted_password, role_id=3, name=form.name.data,
                                    surname=form.surname.data, category=form.category.data,
                                    insta=insta, instaname=form.instauser.data,
                                    face=face, facename=form.faceuser.data,
                                    twitter=twitter,
                                    twittername=form.twitteruser.data,
                                    yt=yt, ytname=form.ytuser.data,
                                    tiktok=tiktok,
                                    tiktokname=form.tiktokuser.data,
                                    twitch=twitch,
                                    twitchname=form.twitchuser.data,
                                    applemusic=applemusic,
                                    applemusicname=form.applemusicuser.data,
                                    spotify=spotify,
                                    spotifyname=form.spotifyuser.data,
                                    soundcloud=soundcloud,
                                    soundcloudname=form.soundclouduser.data, sales=sales,
                                    value=value_c)
        db.session.add(artist_reg)
        db.session.commit()
        registration_success = 1
        send_mail(form.email.data, "ArtChain | Registration success", "mail", username=form.username.data,
                  password=form.password.data, name=form.name.data, surname=form.surname.data,
                  category=form.category.data, artist=1)

    return render_template('artist-registration.html', form=form, registration_success=registration_success,
                           unique_db_error=unique_db_error)


@app.route('/customer-registration', methods=['GET', 'POST'])
def customer_registration():
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
            encrypted_password = generate_password_hash(form.password.data)
            customer_reg = model.User(username=form.username.data, email=form.email.data,
                                      password=encrypted_password, role_id=2)
            db.session.add(customer_reg)
            db.session.commit()
            registration_success = 1
            send_mail(form.email.data, "ArtChain | Registration success", "mail", username=form.username.data,
                      password=form.password.data, artist=0)

    return render_template('customer-registration.html', form=form, name=username, unique_db_error=unique_db_error,
                           registration_success=registration_success)


@app.route('/new-nft', methods=['GET', 'POST'])
def new_nft():
    form = NewNFTForm()
    for row in db.session.query(model.User).filter_by(username=session['username']):
        user_logged_in = row

    if form.validate_on_submit():
        nft = model.NFT(name=form.nft_name.data, description=form.description.data, category=form.category.data,
                        price=form.price.data, nft_file=form.nft_file.data, creator_id=user_logged_in.id)
        db.session.add(nft)
        db.session.commit()

        return redirect(url_for('my_wallet'))

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def calculate_artist_value(user_artist):
    value = 0
    if user_artist.category == 'Musician':
        value = ((user_artist.insta * 0.3 + user_artist.face * 0.2 + user_artist.twitter * 0.2 + user_artist.yt * 0.1 +
                  user_artist.tiktok * 0.1 + user_artist.twitch * 0.1) * 0.5 +
                 (user_artist.applemusic * 0.4 + user_artist.spotify * 0.4 + user_artist.soundcloud * 0.2) * 0.3 +
                 user_artist.sales * 0.2)
    else:
        value = ((user_artist.insta * 0.3 + user_artist.face * 0.2 + user_artist.twitter * 0.2 + user_artist.yt * 0.1 +
                  user_artist.tiktok * 0.1 + user_artist.twitch * 0.1) * 0.8 + user_artist.sales * 0.2)

    user_artist.value = value
    db.session.commit()


if __name__ == '__main__':
    app.run()
