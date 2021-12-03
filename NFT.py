global id
global artist_id
global type
global description

class NFT(object):

    def __init__(self, id, artist_id, type, description):
        self.id = id
        self.artist = artist_id
        self.type = type
        self.description = description
        self.owner = artist_id
                                                    #aggiungere colelgamento a immagine tramite URI


