class Wallet(object):
    def __init__(self, id):
        self.id = id
        self.ac_crypto = ""
        if id[0] == 'a':
            self.crypto_dict = {self.ac_crypto: 0, id: 100}
        else:
            self.crypto_dict = {self.ac_crypto: 0}

    #        self.ac_crypto_amount = 0

    def vendita_nft(self, prezzo):  # vale anche per ricarica da cc
        self.crypto_dict[self.ac_crypto] += prezzo

    def compra_nft(self, prezzo):  # vale anche per ricariica a cc
        if self.crypto_dict[self.ac_crypto] >= prezzo:
            self.crypto_dict[self.ac_crypto] -= prezzo
        else:
            return None

    def compra_crypto(self, prezzo, id_crypto, crypto_ammount):
        if self.crypto_dict[self.ac_crypto] >= prezzo:
            self.crypto_dict[self.ac_crypto] -= prezzo
            self.crypto_dict[id_crypto] = crypto_ammount
        else:
            return None

    def vendi_crypto(self, prezzo, id_crypto, crypto_ammount):
        if self.crypto_dict[id_crypto] >= crypto_ammount:
            self.crypto_dict[self.ac_crypto] += prezzo
            self.crypto_dict[id_crypto] -= crypto_ammount
        else:
            return None
