

class FlightCombinations:

    def __init__(self, prem_flight, sec_flight):
        '''
        args : instance of the Flight class
            prem_flight : the first flight
            sec_flight : the second flight

        '''
        self._first_flight = prem_flight
        self._second_flight = sec_flight
        self._is_combination = self._check_combination()

    def is_combination(self):
        '''return if the combination of the flight are possible'''
        return self._is_combination

    def _check_combination(self):
        if self._possible_destinations() and self._acceptable_time():
            return True
        else:
            return False

    def _possible_destinations(self):
        '''
        return:
            true if possible destinations between 2 flights
            else false

        possible:
            a->b b->c
        '''
        if (self._first_flight.arrival_destination() == self._second_flight.departure_destination()) and (
         self._first_flight.departure_destination() != self._second_flight.arrival_destination()):
            return True
        else:
            return False

    def _acceptable_time(self):
        '''
        if the time difference between arrival of the first flight and departure of the second
        is between 1 and 4  hours
        return : bool
        '''
        time_delta = self._second_flight.departure_time() - self._first_flight.arrival_time()
        time_hours = time_delta.seconds/3600

        if time_hours >= 1 and time_hours <= 4:
            return True
        else:
            return False

    def max_allowed_bags(self):
        ''' return the maximum allowed bags for both flight'''
        return min(
            self._first_flight.max_allowed_bags(),
            self._second_flight.max_allowed_bags()
            )

    def total_price(self, total_bags=0)->int:
        '''return the sum of the total price of both flights'''
        return (
            self._first_flight.total_price(total_bags=total_bags) +
            self._second_flight.total_price(total_bags=total_bags)
            )
