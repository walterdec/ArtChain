import os
import string
import random
import model
from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_mail import Message, Mail
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from form import LoginForm, CustomerRegistrationForm, ArtistRegistrationForm, ForgotPasswordForm, EditArtistForm, \
    EditCustomerForm, NewNFTForm, ContactForm, BuyCryptoForm
from PIL import Image

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

app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+"/static/uploads"
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

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
    users_dictionary = {}
    nfts_list = db.session.query(model.NFT).all()
    cryptos_list = db.session.query(model.Crypto).all()
    for cryptocurrency in cryptos_list:
        users_dictionary[cryptocurrency.user_id] = (db.session.query(model.User).
                                                    filter_by(id=cryptocurrency.user_id).first())
    random.shuffle(nfts_list)
    random.shuffle(cryptos_list)
    return render_template('home.html', cryptos=cryptos_list[0:4], nfts=nfts_list[0:4], users=users_dictionary)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    contact_request = 0
    if form.validate_on_submit():
        contact_request = 1
        send_mail(app.config['MAIL_USERNAME'], "Contact Request | "+form.name.data, "mail", name=form.name.data,
                  email=form.email.data,  message=form.message.data, contact_request=contact_request)
    return render_template('contact.html', form=form, contact_request=contact_request)


@app.route('/explore-nfts', methods=['GET', 'POST'])
def explore_nfts():
    nfts_list = db.session.query(model.NFT).all()
    return render_template('explore-nfts.html', nfts_list=nfts_list)


@app.route('/explore-crypto', methods=['GET', 'POST'])
def explore_crypto():
    users_dictionary = {}
    cryptos_list = db.session.query(model.Crypto).all()
    for cryptocurrency in cryptos_list:
        users_dictionary[cryptocurrency.user_id] = (db.session.query(model.User).filter_by
                                                    (id=cryptocurrency.user_id).first())
    return render_template('explore-crypto.html', users_dictionary=users_dictionary, cryptos_list=cryptos_list)


@app.route('/stats')
def stats():
    return render_template('stats.html')


@app.route('/myaccount-mywallet')
def my_wallet():
    try:
        if session['username']:
            user = session['username']
            for row in db.session.query(model.User).filter_by(username=user):
                user_logged_in = row
    except KeyError:
        return forbidden(KeyError)
    users_dictionary = {}
    crypto_dictionary = {}
    wallet_dictionary = {}
    wallet_list = db.session.query(model.Wallet).filter_by(user_id=user_logged_in.id).all()
    cryptos_list = db.session.query(model.Crypto).all()
    for cryptocurrency in cryptos_list:
        users_dictionary[cryptocurrency.user_id] = (db.session.query(model.User).filter_by
                                                    (id=cryptocurrency.user_id).first())
    for row in wallet_list:
        crypto_dictionary[row.crypto_id] = (db.session.query(model.Crypto).filter_by
                                            (id=row.crypto_id).first())
        wallet_dictionary[row.crypto_id] = row

    nfts_list = db.session.query(model.NFT).filter_by(owner_id=user_logged_in.id).all()

    return render_template('myaccount-mywallet.html', user=user_logged_in,
                           users_dictionary=users_dictionary, crypto_dictionary=crypto_dictionary,
                           wallet_dictionary=wallet_dictionary, nfts_list=nfts_list)


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
        return forbidden(KeyError)

    return render_template('myaccount-profile.html', form=form, user_logged_in=user_logged_in)


@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    form = LoginForm()
    login_error = 0
    if form.validate_on_submit():
        for row in db.session.query(model.User).filter_by(username=request.form['username'].lower()):
            user = row
            if check_password_hash(user.password, request.form['password']):
                username = form.username.data.lower()
                session['username'] = username
                return redirect(url_for('home'))
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
        if model.Crypto.query.filter(model.Crypto.name == request.form['crypto'].upper()).first():
            return render_template('artist-registration.html', form=form, crypto_already_existing=1)
        if len(request.form['crypto']) is not 3:
            return render_template('artist-registration.html', form=form, crypto_not_valid=1)

        if (model.User.query.filter(model.User.username == request.form['username'].lower()).first() or
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
                           (applemusic * 0.4 + spotify * 0.4 + soundcloud * 0.2) * 0.3 + sales * 0.2)/1000
                value_c = round(value_c, 3)
            else:
                value_c = ((insta * 0.3 + face * 0.2 + twitter * 0.2 + yt * 0.1 + tiktok * 0.1 + twitch * 0.1) * 0.8 +
                           + sales * 0.2)/1000
                value_c = round(value_c, 3)

            encrypted_password = generate_password_hash(form.password.data)

            img_src = upload_profile_pic(form.profile_pic.data, form.username.data.lower())

            artist_reg = model.User(username=form.username.data.lower(), email=form.email.data,
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
                                    value=value_c, profile_pic_src=img_src)

            db.session.add(artist_reg)
            db.session.commit()
            registration_success = 1

            crypto_creation = model.Crypto(name=form.crypto.data.upper(), user_id=model.User.query.filter_by
                                           (username=form.username.data.lower()).first().id, value=value_c)
            db.session.add(crypto_creation)
            db.session.commit()

            wallet_row = model.Wallet(user_id=model.User.query.filter_by
                                      (username=form.username.data.lower()).first().id,
                                      crypto_id=model.Crypto.query.filter_by(name=form.crypto.data.upper()).first().id,
                                      amount=100)
            db.session.add(wallet_row)
            db.session.commit()

            send_mail(form.email.data, "ArtChain | Registration success", "mail", username=form.username.data,
                      password=form.password.data, name=form.name.data, surname=form.surname.data,
                      category=form.category.data, artist=1, restore_account=0)

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
        if (model.User.query.filter(model.User.username == request.form['username'].lower()).first() or
                model.User.query.filter(model.User.email == request.form['email']).first()):
            unique_db_error = 1
        else:
            encrypted_password = generate_password_hash(form.password.data)
            customer_reg = model.User(username=form.username.data.lower(), email=form.email.data,
                                      password=encrypted_password, role_id=2)
            db.session.add(customer_reg)
            db.session.commit()
            registration_success = 1
            send_mail(form.email.data, "ArtChain | Registration success", "mail", username=form.username.data,
                      password=form.password.data, artist=0, restore_account=0)

    return render_template('customer-registration.html', form=form, name=username, unique_db_error=unique_db_error,
                           registration_success=registration_success)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = NewNFTForm()
    duplicated_nft = 0
    try:
        for row in db.session.query(model.User).filter_by(username=session['username']):
            user_logged_in = row
    except KeyError:
        return forbidden(KeyError)

    if form.validate_on_submit():
        if not db.session.query(model.NFT).filter_by(name=form.nft_name.data).first():
            img_src = upload_nft(form.nft_file.data, form.nft_name.data)
            if img_src is not None:
                nft = model.NFT(name=form.nft_name.data, description=form.description.data, category=form.category.data,
                                price=form.price.data, creator_id=user_logged_in.id, owner_id=user_logged_in.id,
                                img_src=img_src)
                db.session.add(nft)
                db.session.commit()
                return render_template('create.html', user_logged_in=user_logged_in, form=form, nft_created=1)
            else:
                return render_template('create.html', user_logged_in=user_logged_in, form=form, img_size_error=1)
        else:
            duplicated_nft = 1

    return render_template('create.html', user_logged_in=user_logged_in, form=form, duplicated_nft=duplicated_nft)


@app.route('/item/nft/<name>', methods=['GET', 'POST'])
def item_nft(name):
    nft = None
    for row in db.session.query(model.NFT).filter_by(name=name):
        nft = row
    if nft is None:
        return page_not_found(TypeError)
    nft_creator = db.session.query(model.User).filter_by(id=nft.creator_id).first()
    return render_template('item-nft.html', nft=nft, nft_creator=nft_creator)


@app.route('/item/crypto/<name>', methods=['GET', 'POST'])
def item_crypto(name):
    form = BuyCryptoForm()
    cryptocurrency = None
    for row in db.session.query(model.Crypto).filter_by(name=name):
        cryptocurrency = row
    if cryptocurrency is None:
        return page_not_found(TypeError)
    crypto_artist = db.session.query(model.User).filter_by(id=cryptocurrency.user_id).first()
    if form.validate_on_submit():
        return render_template('item-crypto.html', form=form, crypto=cryptocurrency, crypto_artist=crypto_artist)
    return render_template('item-crypto.html', form=form, crypto=cryptocurrency, crypto_artist=crypto_artist)


@app.route('/profile/<username>', endpoint="profile_by_user")
def artist_profile(username):
    user = None
    nft_list = []
    for row in db.session.query(model.User).filter_by(username=username):
        user = row
    if user is None or user.role_id is not 3:
        return page_not_found(TypeError)
    for row in db.session.query(model.NFT).filter_by(creator_id=user.id):
        nft_list.append(row)
    cryptocurrency = db.session.query(model.Crypto).filter_by(user_id=user.id).first()
    return render_template('profile-page.html', user=user, nft_list=nft_list, crypto=cryptocurrency)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    form = ForgotPasswordForm()
    wrong_email = 0
    email_sent = 0
    restoring_user = None
    if form.validate_on_submit():
        if model.User.query.filter(model.User.email == request.form['email']).first():
            for row in db.session.query(model.User).filter_by(email=form.email.data):
                restoring_user = row
            new_password = password_generator(12)
            restoring_user.password = generate_password_hash(new_password)
            db.session.commit()
            send_mail(form.email.data, "ArtChain | Password Reset", "mail", username=restoring_user.username,
                      password=new_password, artist=0, restore_account=1)
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
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


def calculate_artist_value(user_artist):
    value = 0
    if user_artist.category == 'Musician':
        value = ((user_artist.insta * 0.3 + user_artist.face * 0.2 + user_artist.twitter * 0.2 + user_artist.yt * 0.1 +
                  user_artist.tiktok * 0.1 + user_artist.twitch * 0.1) * 0.5 +
                 (user_artist.applemusic * 0.4 + user_artist.spotify * 0.4 + user_artist.soundcloud * 0.2) * 0.3 +
                 user_artist.sales * 0.2)/1000
    else:
        value = ((user_artist.insta * 0.3 + user_artist.face * 0.2 + user_artist.twitter * 0.2 + user_artist.yt * 0.1 +
                  user_artist.tiktok * 0.1 + user_artist.twitch * 0.1) * 0.8 + user_artist.sales * 0.2)/1000

    user_artist.value = round(value, 3)
    db.session.commit()


def upload_nft(nft_file, name):
    img_name = name.replace(" ", "_")
    img_name = img_name+'.jpg'
    if not os.path.exists('static/uploads/nfts'):
        os.makedirs('static/uploads/nfts')
    folder = 'nfts'
    photos.save(nft_file, name=img_name, folder=folder)
    img_src = 'static/uploads/nfts/'+img_name
    if check_size(img_src):
        return img_name
    else:
        os.remove(img_src)
        return None


def check_size(image):
    img = Image.open(image)
    width, height = img.size
    if width in range(height-10, height+10):
        return True
    else:
        return False


def upload_profile_pic(pic_file, username):
    img_src = username.replace(" ", "_")
    img_src = img_src+'.jpg'
    if not os.path.exists('static/uploads/profilepics'):
        os.makedirs('static/uploads/profilepics')
    folder = 'profilepics'
    photos.save(pic_file, name=img_src, folder=folder)
    return img_src


def password_generator(length):
    uppercase_loc = random.randint(1, 4)
    symbol_loc = random.randint(5, 6)
    lowercase_loc = random.randint(7, 12)

    password = ''
    pool = string.ascii_letters + string.punctuation

    for i in range(length):
        if i == uppercase_loc:
            password += random.choice(string.ascii_uppercase)
        elif i == lowercase_loc:
            password += random.choice(string.ascii_lowercase)
        elif i == symbol_loc:
            password += random.choice(string.punctuation)
        else:
            password += random.choice(pool)
    return password


if __name__ == '__main__':
    app.run()
