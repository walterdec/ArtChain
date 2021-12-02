from Wallet import Wallet


class Artist(object):
    def __init__(self, username, password, email, name, surname, id, is_musician):
        self.username = username
        self.password = password
        self.email = email
        self.name = name  # optional
        self.surname = surname  # optional
        self.is_musician = is_musician
        wallet = Wallet(id)



    crypto_value = 0.0

    insta = 0
    face = 0
    twitter = 0
    yt = 0
    tiktok = 0
    twitch = 0

    applemusic = 0
    spotify = 0
    soundcloud = 0

    sales = 0.0


def evaluation(insta, face, twitter, yt, tiktok, twitch, applemusic, spotify, soundcloud, sales):
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
                        twitch * 0.1) * 0.5 + (applemusic * 0.4 + spotify * 0.5 + soundcloud * 0.1) * 0.3 + sales * 0.2
    else:
        crypto_value = (insta * 0.3 + face * 0.2 + twitter * 0.2 + yt * 0.1 + tiktok * 0.1 +
                        twitch * 0.1) * 0.8 + sales * 0.2
