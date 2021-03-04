from abc import ABC, abstractmethod


class Order:
    def __init__(self, name , phone, cart, prom=None):
        self.name  = name
        self.phone = phone
        self.cart = cart
        self.prom = prom

    def total(self):
        total_pay = 0
        for item in self.cart:
            total_pay += item.get_total_price
        return total_pay

    def due(self):
        return self.total() - self.prom.discount(self.cart)


class Item:
    def __init__(self, title, price, qty):
        self.title = title
        self.price = price
        self.qty = qty

    @property
    def get_total_price(self):
        return self.price * self.qty



class Promotion(ABC):

    @abstractmethod
    def discount(self, cart):
        pass


class MoshtarianSetare(Promotion):
    '''moshtariane setare man 10 darsad takhfif'''

    def discount(self, cart):
        takhfif = 0
        for item in cart:
            takhfif += item.get_total_price
        return takhfif * 0.1


class LargeOrder(Promotion):
    '''moshtariane zuad bekhar man 7 darsad takhfif'''
    
    def discount(self, cart):
        takhfif = 0
        if sum(item.qty for item in cart) >=50:
            for item in cart:
                takhfif += item.get_total_price
            return takhfif * 0.07
        return takhfif


class MoshtarianMotadJens(Promotion):
    '''moshtariane eshghe ye jens(vaghti 20ta va bishtar) 5 darsad takhfif ru un jense'''
    
    def discount(self, cart):
        takhfif = 0
        for item in cart:
            if item.qty >=20:
                takhfif += (item.get_total_price * 0.05)
        return takhfif



sib = Item('sib', 1000, 10)
port = Item('port', 2500, 10)
mowz = Item('mowz', 150, 21)

order = Order('ashkan', 912222222, [sib, port, mowz], prom=MoshtarianMotadJens())


print(f"ghabl takhfif {order.total()} bad takhfif {order.due()}")