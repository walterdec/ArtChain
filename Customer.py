from Wallet import Wallet


username = ""
password = ""
email = ""
id = ""
my_nft_list = []

class Customer(object):
    def __init__(self, username, password, email,id):
        self.username = username
        self.password = password
        self.email = email
        self.id = id
        wallet = Wallet(id)


