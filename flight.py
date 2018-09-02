import arrow


class Flight:

    '''
    this class represents a flight

    args:
        none

    kwargs:
        example
        {
            'source': 'DPS',
            'destination': 'BWN',
            'departure': '2017-02-11T22:10:00',
            'arrival': '2017-02-12T00:35:00',
            'flight_number': 'PV197',
            'price': 50,
            'bags_allowed': 1,
            'bag_price': 30
        }

    '''

    def __init__(self, **kwargs):
        self._source = kwargs['source']
        self._destination = kwargs['destination']
        self._departure = arrow.get(kwargs['departure'])
        self._arrival = arrow.get(kwargs['arrival'])
        self._flight_number = kwargs['flight_number']
        self._price = kwargs['price']
        self._bags_allowed = kwargs['bags_allowed']
        self._bag_price = kwargs['bag_price']

    def allowed_bags(self, amount_bags: int)->bool:
        '''
        arg:
            amount_bags: amount of bags that a passager want to bring
        return:
            true or false if possible
        '''

        if amount_bags < 0:
            raise ValueError('You can not bring a negatief amount of bags {}'.format(amount_bags))
        else:
            if amount_bags <= self._bags_allowed:
                return True
            else:
                return False

    def total_price(self, total_bags=0)->int:
        '''
        calculates the total price of the fligt by the given bags taken on the flight

        arg:
            total_bages : the total amount of bags taken on the flight
        return:
            the total price of the flight
        '''
        if not self.allowed_bags(total_bags):
            raise ValueError('the total bags {} are more than allowed {}'.format(total_bags, self._bags_allowed))
        return self._price + total_bags * self._bag_price

    def departure_destination(self):
        return self._source

    def arrival_destination(self):
        return self._destination

    def departure_time(self):
        return self._departure

    def arrival_time(self):
        return self._arrival

    def max_allowed_bags(self):
        return self._bags_allowed
