from app import db




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    is_artist = db.Column(db.Boolean)
    is_musician = db.Column(db.Boolean, default=False)

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

    value = db.Column(db.Float)
    growth = db.Column(db.Float)


class NFT(db.Model):
    __tablename__ = 'nfts'
    id = db.Column(db.Integer, primary_key=True)
    id_artist = db.Column(db.String(64), index=True)
    name = db.Column(db.String(64))
    id_owner = db.Column(db.String(64))
    type = db.Column(db.String(64))
    description = db.Column(db.Text)


class Auction(db.Model):
    __tablename__ = 'auctions'
    auction_id = db.Column(db.Integer)
    nft_id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float)
    duration = db.Column(db.Time)
    best_bidder_id = db.Column(db.Integer)
    start_date = db.Column(db.Date)


#class CryptoOnSale(db.Model):
#    __tablename__ = 'cryptos_on_sale'
#    crypto_id = db.Column(db.Integer)
#    artist_id = db.Column(db.Integer)
#    quantity = db.Column(db.Float)
#    duration = db.Column(db.Time)
#    best_bidder_id = db.Column(db.Integer)
#    start_date = db.Column(db.Date)


#class Wallet(db.Model):
#    __tablename__ = 'wallets'
#    owner_id = db.Column(db.Integer)
#    ac_crypto = db.Column(db.Float, default=0.0)








