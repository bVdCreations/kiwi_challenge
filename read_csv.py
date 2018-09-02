import pandas as pd

'''
read the csv files into pandas
'''

input_data = pd.read_csv('data_example.csv')

input_data_dict = input_data.to_dict('records')

input_data_sorted = sorted(input_data_dict, key=lambda k: k['departure'])
