import datetime
from time import time, localtime


class Auction(object):
    def __init__(self, auction_id,  nft , price, duration):
        self.best_bidder = ""
        self.auction_id = auction_id
        self.nft = nft
        self.price = price
        self.duration = duration
        epoch = time()
        self.start_date = localtime(epoch)
        self.end_date = localtime(epoch + duration)
        self.bids_dict = {}
        self.best_bid = price

    def make_a_bid(self, id, price_bid):
        if price_bid > self.best_bid:
            self.bids_dict[id] = price_bid
            self.best_bid = price_bid
            self.best_bidder = id
            # da modificare, andrebbe nella pagina dell'asta

    def countdown(self):
        while self.duration:
            time.sleep(1)
            self.duration -= 1
            cd = datetime.timedelta(self.duration)
            self.nft.owner = self.best_bidder
