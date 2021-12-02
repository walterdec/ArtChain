class Wallet(object):
    def __init__(self, id):
        self.id = id
        self.crypto_dict = {ac_crypto: 0, id: 1500}

    #        self.ac_crypto_amount = 0

    def vendita_nft(self, prezzo): #vale anche per ricarica da cc
        crypto_dict[ac_crypto] += prezzo


    def compra_nft(self, prezzo):  #vale anche per ricariica a cc
        if crypto_dict[ac_crypto]>=prezzo:
            crypto_dict[ac_crypto] -= prezzo
        else:
            return None


    def compra_crypto(self, prezzo, id_crypto, crypto_ammount):
        if crypto_dict[ac_crypto] >= prezzo:
            crypto_dict[ac_crypto] -= prezzo
            crypto_dict[id_crypto] = crypto_ammount
        else:
            return None

    def vendi_crypto(self, prezzo, id_crypto, crypto_ammount):
        if crypto_dict[id_crypto] >= crypto_ammount:
            self.crypto_dict[ac_crypto]+= prezzo
            self.crypto_dict[id_crypto]-= crypto_ammount
        else:
            return None

