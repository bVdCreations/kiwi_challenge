import pytest
from ..flight import Flight


@pytest.fixture
def data_input():
    '''data example 1 row'''
    return {
        'source': 'USM', 'destination': 'HKT',
        'departure': '2017-02-12T12:15:00',
        'arrival': '2017-02-12T13:15:00', 'flight_number': 'PV755',
        'price': 23, 'bags_allowed': 2, 'bag_price': 9}


@pytest.fixture
def setup_flight(data_input):
    '''setup object of flight for test'''
    fly = Flight(**data_input)
    return fly


def test_allowed_bages(setup_flight, data_input):
    '''test the ammount of allowed bags is correct'''

    assert setup_flight.allowed_bags(0)
    assert setup_flight.allowed_bags(data_input['bags_allowed'])
    assert not setup_flight.allowed_bags(data_input['bags_allowed']+1)

    with pytest.raises(ValueError):
        setup_flight.allowed_bags(-1)


def test_total_price(setup_flight, data_input):
    '''test the method total price'''

    assert setup_flight.total_price() > 0
    assert setup_flight.total_price(total_bags=data_input['bags_allowed']) > 0
    assert setup_flight.total_price() <= setup_flight.total_price(
        total_bags=data_input['bags_allowed'])
    assert setup_flight.total_price() == data_input['price']
    assert setup_flight.total_price(
        total_bags=data_input['bags_allowed']) == (
            data_input['bags_allowed'] * data_input['bag_price'] + data_input['price'])

    with pytest.raises(ValueError):
        setup_flight.total_price(total_bags=(data_input['bags_allowed'] + 1))

    with pytest.raises(ValueError):
        setup_flight.total_price(total_bags=-1)
