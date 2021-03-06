import pytest
from ..flight import Flight
from ..combinations import FlightCombinations

# 5 test flights
fly1 = Flight(**{
        'source': 'USM', 'destination': 'HKT',
        'departure': '2017-02-12T12:15:00',
        'arrival': '2017-02-12T13:15:00', 'flight_number': 'PV755',
        'price': 23, 'bags_allowed': 2, 'bag_price': 9})

fly2 = Flight(**{
        'source': 'DPS', 'destination': 'HKT',
        'departure': '2017-02-11T00:20:00',
        'arrival': '2017-02-11T04:00:00', 'flight_number': 'PV519',
        'price': 79, 'bags_allowed': 2, 'bag_price': 44})

fly3 = Flight(**{
        'source': 'HKT', 'destination': 'DPS',
        'departure': '2017-02-12T00:00:00',
        'arrival': '2017-02-12T03:40:00', 'flight_number': 'PV961',
        'price': 70, 'bags_allowed': 1, 'bag_price': 39})

fly4 = Flight(**{
        'source': 'DPS', 'destination': 'BWN',
        'departure': '2017-02-12T17:15:00',
        'arrival': '2017-02-12T19:40:00', 'flight_number': 'PV620',
        'price': 43, 'bags_allowed': 1, 'bag_price': 25})

fly5 = Flight(**{
        'source': 'HKT', 'destination': 'BWN',
        'departure': '2017-02-12T14:45:00',
        'arrival': '2017-02-12T16:15:00', 'flight_number': 'PV755',
        'price': 23, 'bags_allowed': 2, 'bag_price': 9})


@pytest.mark.parametrize("first_flight, second_flight, expect", [
    # first.arrival != second.departure
    (fly1, fly2, False),
    # first.arrival == second.departure & second.arrival == first.departure
    (fly2, fly3, False),
    # first.arrival == second.departure & second.arrival != first.departure
    (fly3, fly4, True),
    # second.arrival == first.departure & first.arrival != second.departure
    (fly4, fly3, False),
    ])
def test_possible_destinations(first_flight, second_flight, expect):
    '''test method possible destinations of the FlightCombinations'''

    errorstring = 'first flight departure: {} destination: {} \n \
                second flight departure: {} destination: {}'.format(
                        first_flight.departure_destination(),
                        first_flight.arrival_destination(),
                        second_flight.departure_destination(),
                        second_flight.arrival_destination(),
                    )
    assert FlightCombinations(
        first_flight, second_flight)._possible_destinations() == expect, errorstring


@pytest.mark.parametrize("first_flight, second_flight, expect", [
    # first.time arrival > second.time departure
    (fly1, fly2, False),
    # second.time departure- first.time arrival < 1:00
    (fly2, fly3, False),
    # 4:00 > second.time departure- first.time arrival < 1:00
    (fly1, fly4, True),
    # 4:00 > second.time departure- first.time arrival
    (fly3, fly4, False),
])
def test_acceptable_time(first_flight, second_flight, expect):
    '''test method possible destinations of the FlightCombinations'''

    errorstring = 'first flight departure time: {} arrival time: {} \n \
                second flight departure time: {} arrival time: {}'.format(
        first_flight.departure_time(),
        first_flight.arrival_time(),
        second_flight.departure_time(),
        second_flight.arrival_time(),
    )
    assert FlightCombinations(
        first_flight, second_flight)._acceptable_time() == expect, errorstring


@pytest.mark.parametrize("first_flight, second_flight, expect", [
    # first.time arrival > second.time departure and first.arrival != second.departure
    (fly1, fly2, False),
    # second.time departure- first.time arrival < 1:00
    # first.arrival == second.departure & second.arrival == first.departure
    (fly2, fly3, False),
    # first.arrival != second.departure
    (fly1, fly4, False),
    # 4:00 > second.time departure- first.time arrival
    (fly3, fly4, False),
    # second.arrival == first.departure & first.arrival != second.departure
    (fly4, fly3, False),
    # possible time and correct destinations
    (fly1, fly5, True),
])
def test_check_combination(first_flight, second_flight, expect):
        '''test the method that combines the previous two tested method'''

        errorstring = 'first flight departure: {} destination: {} \n \
                        second flight departure: {} destination: {} \n \
                        first flight departure time: {} arrival time: {} \n \
                        second flight departure time: {} arrival time: {}'.format(
                        first_flight.departure_destination(),
                        first_flight.arrival_destination(),
                        second_flight.departure_destination(),
                        second_flight.arrival_destination(),
                        first_flight.departure_time(),
                        first_flight.arrival_time(),
                        second_flight.departure_time(),
                        second_flight.arrival_time(),
                    )
        assert FlightCombinations(
            first_flight, second_flight)._check_combination() == expect, errorstring


@pytest.mark.parametrize("first_flight, second_flight, expect", [
        # flight 1 bags:2 flight2 bags:2
        (fly1, fly2, 2),
        # flight 1 bags:2 flight2 bags:1
        (fly2, fly3, 1),
        # flight 1 bags:1 flight2 bags:1
        (fly3, fly4, 1),
        # flight 1 bags:1 flight2 bags:2
        (fly4, fly5, 1),
])
def test_max_allowed_bags(first_flight, second_flight, expect):
        '''test the method of the max allowed bags the to plane flights'''

        errorstring = 'first flight max bags: {} second flight max bags: {}'.format(
                first_flight.max_allowed_bags(),
                second_flight.max_allowed_bags(),
        )

        assert FlightCombinations(
                first_flight, second_flight).max_allowed_bags() == expect, errorstring


@pytest.mark.parametrize("first_flight, second_flight, expect_no_bags, expect_all_bags", [
    # flight 1, flight2, Totalprice no bags, Totalprice max bags
    (fly1, fly2, 102, 208),
    (fly2, fly3, 149, 232),
    (fly3, fly4, 113, 177),
])
def test_total_price(first_flight, second_flight, expect_no_bags, expect_all_bags):
        '''test the method of the max allowed bags the to plane flights'''

        errorstring = 'first flight price: {}  bagprice: {} \n \
                        second flight price: {}  bagprice: {}'.format(
            first_flight._price,
            first_flight._bag_price,
            second_flight._price,
            second_flight._bag_price,
        )

        flight_combo = FlightCombinations(first_flight, second_flight)
        max_bags = flight_combo.max_allowed_bags()

        assert flight_combo.total_price() > 0, errorstring
        assert flight_combo.total_price() == expect_no_bags
        assert flight_combo.total_price(total_bags=max_bags) == expect_all_bags

        with pytest.raises(ValueError):
                flight_combo.total_price(total_bags=-1)

        with pytest.raises(ValueError):
                flight_combo.total_price(total_bags=1000)
