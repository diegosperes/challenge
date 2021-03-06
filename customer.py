from data_model import DataModel
from order import Order


class Customer(DataModel):
    @property
    def address(self):
        return dict(zip_code=self._data.get('zip_code'), address=self._data['address'])

    def __init__(self, _id):
        ''' Get all informations (data) from database. '''
        self._data = data

    def get_order(self, products=None):
        ''' Get the opened order in database if doesn't exist create a new one. '''
        if not order:
            order = Order.create({'customer': self, 'products': products})
        elif products:
            order.update({'products': products})
        return order

    def enable_service(self, service_id):
        ''' Enable service for a user, check if the customer paid for it and activate the account. '''
        pass
