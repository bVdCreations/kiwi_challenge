from ..read_csv import input_data


def test_read_in():
    '''check is the data_example is correctly read in'''
    assert list(input_data.columns.values) == [
                                            'source',
                                            'destination',
                                            'departure',
                                            'arrival',
                                            'flight_number',
                                            'price',
                                            'bags_allowed',
                                            'bag_price'
                                            ]
