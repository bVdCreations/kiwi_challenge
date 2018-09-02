import sys
import json

from read_csv import read_in_csv
from flight import Flight
from combinations import FlightCombinations

input_data_sorted = read_in_csv(sys.stdin)
valid_flight_combinations = list()
second_data = input_data_sorted.copy()

for first_flight_info in input_data_sorted:
    second_data.pop(0)
    for second_flight_info in second_data:
        flight_combi = FlightCombinations(
            Flight(**first_flight_info),
            Flight(**second_flight_info)
        )
        if flight_combi.is_valid():
            valid_flight_combinations.append(flight_combi)

max_bags = 2
combinations = list()
for bags in range(max_bags+1):
    # combinations['combinationsset'] = {'combinations by bag': list(), 'bags': bags}
    for valid_combination in valid_flight_combinations:
        if valid_combination.max_allowed_bags() >= bags:
            price = valid_combination.total_price(total_bags=bags)
            combinations.append({**valid_combination.info_flights(), 'total price': price, 'bags': bags})

# write out the combinations list in json
sys.stdout.write(json.dumps(combinations))
