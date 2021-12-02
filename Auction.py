import datetime
from time import time, localtime


class Auction(object):
    def __init__(self, auction_id, nft, price, duration):
        self.auction_id = auction_id
        self.nft = nft
        self.price = price
        self.duration = duration
        epoch = time()
        start_date = localtime(epoch)
        end_date = localtime(epoch+duration)
        bids_dict = {None, price}
        best_bid = price


def make_a_bid(id, price_bid):
    if price_bid > best_bid:
        bids_dict[id] = price_bid
        best_bid = price_bid
        best_bidder = id

#da modificare, andrebbe nella pagina dell'asta
def countdown():
    while duration:
        time.sleep(1)
        duration -= 1
        cd = datetime.timedelta(duration)



