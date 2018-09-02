from read_csv import input_data_sorted
from flight import Flight
from combinations import FlightCombinations

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
# read the csv files

# process into easy manageable objects

# find combinations objects

#    combinations source destination

#    check time diference 1-4 hours

#    maximun allowed bags

#    call price flight plus bags

# ouput data in a readable form -> json

# figure out what stdio stdout and stderr are
