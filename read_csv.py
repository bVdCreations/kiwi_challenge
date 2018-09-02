import pandas as pd


def read_in_csv(data):
    '''
    read the csv files into pandas
    return rows as dict (header : value) in a sorted list (sorted by departure time)
    '''

    input_data = pd.read_csv('data_example.csv')

    input_data_dict = input_data.to_dict('records')

    return sorted(input_data_dict, key=lambda k: k['departure'])
