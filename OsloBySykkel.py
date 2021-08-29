# Dependent library
import requests


# Function to reformat json data from API to dictionary

def return_json(api):
    response = requests.get(api)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # if it wasn't a 200
        return "Error: " + str(e)

    # Must have been a 200 status code
    json_obj = response.json()
    return json_obj


# Function to parse reformatted JSON data and print required fields

def printsykkelstatus(x, y):
    for bystation in x['data']['stations']:
        print("At station", bystation['name'], "there are", end=" ")
        i = bystation['station_id']
        for available_bikes_docks in y['data']['stations']:
            if i == available_bikes_docks['station_id']:
                print(available_bikes_docks['num_bikes_available'], "bikes available", end=" ")
                print("and with", available_bikes_docks['num_docks_available'], "docks available")


stations = "https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json"
station_status = "https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json"

stations_dict = return_json(stations)
stations_status_dict = return_json(station_status)
printsykkelstatus(stations_dict, stations_status_dict)
