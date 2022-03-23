from Wallet import Wallet
from flask import flask
from NFT import NFT
from Auction import Auction


class Artist(object):
    def __init__(self, username, password, email, name, surname, id, is_musician):
        self.username = username
        self.password = password
        self.email = email
        self.name = name  # optional
        self.surname = surname  # optional
        self.id = id
        self.is_musician = is_musician
        self.my_auctions_list = []
        wallet = Wallet(id)

    def evaluation(self, insta, face, twitter, yt, tiktok, twitch, applemusic, spotify, soundcloud, sales, is_musician):
        insta = insta
        face = face
        twitter = twitter
        yt = yt
        tiktok = tiktok
        twitch = twitch
        applemusic = applemusic
        spotify = spotify
        soundcloud = soundcloud
        sales = sales
        if is_musician:
            crypto_value = (insta * 0.3 + face * 0.2 + twitter * 0.2 + yt * 0.1 + tiktok * 0.1 +
                            twitch * 0.1) * 0.5 + (
                                       applemusic * 0.4 + spotify * 0.5 + soundcloud * 0.1) * 0.3 + sales * 0.2
        else:
            crypto_value = (insta * 0.3 + face * 0.2 + twitter * 0.2 + yt * 0.1 + tiktok * 0.1 +
                            twitch * 0.1) * 0.8 + sales * 0.2

    def create_nft_and_auction(self, nft_id, type, description, auction_id, price, duration):
        nft = NFT(nft_id, id, type, description)
        # aggiungere collegamento a immagine tramite URI
        auction = Auction(auction_id, nft, price, duration)
        self.my_auctions_list.append(auction)
        auction.countdown()
