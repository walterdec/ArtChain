from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    category = db.Column(db.String(64), default=False)

    profile_pic_src = db.Column(db.String(64))

    insta = db.Column(db.Integer)
    instaname = db.Column(db.String(64))
    face = db.Column(db.Integer)
    facename = db.Column(db.String(64))
    twitter = db.Column(db.Integer)
    twittername = db.Column(db.String(64))
    yt = db.Column(db.Integer)
    ytname = db.Column(db.String(64))
    tiktok = db.Column(db.Integer)
    tiktokname = db.Column(db.String(64))
    twitch = db.Column(db.Integer)
    twitchname = db.Column(db.String(64))
    applemusic = db.Column(db.Integer)
    applemusicname = db.Column(db.String(64))
    spotify = db.Column(db.Integer)
    spotifyname = db.Column(db.String(64))
    soundcloud = db.Column(db.Integer)
    soundcloudname = db.Column(db.String(64))
    sales = db.Column(db.Integer)

    value = db.Column(db.Integer)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(100), nullable=False)
    users = db.relationship('User', backref='role_name')


class NFT(db.Model):
    __tablename__ = 'nfts'
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.String(64), index=True)
    owner_id = db.Column(db.String(64))
    name = db.Column(db.String(64))
    category = db.Column(db.String(64))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    img_src = db.Column(db.String(64))


class Crypto(db.Model):
    __tablename__ = 'cryptos'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(64), unique=True)
    value = db.Column(db.Float)


class Wallet(db.Model):
    __tablename__ = 'wallets'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer)
    crypto_id = db.Column(db.Integer)
    amount = db.Column(db.Float)








