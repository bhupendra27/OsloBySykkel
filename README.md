
# OsloBySykkel assignment

This python script will provide real time data about different stations and availability of bikes and docks of OsloBySykkel using below mentioned APIs.



## API Reference

#### Get all Stations

Endpoint:https://gbfs.urbansharing.com/oslobysykkel.no/station_information.jso

Response:
{
  "last_updated": 1553592653,
  "data": {
    "stations": [
      {  
        "station_id":"627",
        "name":"Skøyen Stasjon",
        "address":"Skøyen Stasjon",
        "lat":59.9226729,
        "lon":10.6788129,
        "capacity":20
      },
      {  
        "station_id":"623",
        "name":"7 Juni Plassen",
        "address":"7 Juni Plassen",
        "lat":59.9150596,
        "lon":10.7312715,
        "capacity":15
      },
      {  
        "station_id":"610",
        "name":"Sotahjørnet",
        "address":"Sotahjørnet",
        "lat":59.9099822,
        "lon":10.7914482,
        "capacity":20
      }
    ]
  }
}


#### Get all availability

Endpoint:https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json

Response:
{
  "last_updated": 1540219230,
  "data": {
    "stations": [
      {
        "is_installed": 1,
        "is_renting": 1,
        "num_bikes_available": 7,
        "num_docks_available": 5,
        "last_reported": 1540219230,
        "is_returning": 1,
        "station_id": "175"
      },
      {
        "is_installed": 1,
        "is_renting": 1,
        "num_bikes_available": 4,
        "num_docks_available": 8,
        "last_reported": 1540219230,
        "is_returning": 1,
        "station_id": "47"
      },
      {
        "is_installed": 1,
        "is_renting": 1,
        "num_bikes_available": 4,
        "num_docks_available": 9,
        "last_reported": 1540219230,
        "is_returning": 1,
        "station_id": "10"
      }
    ]
  }
}
Historical data



  
## Authors

- [@bhupendra27](https://github.com/bhupendra27)

## Installation on Mac OS 10.15.8 with pre-installed homebrew for standalone execution.

Ensure that you have python runtime 3.0 and requests module preinstalled using following commands.

brew install python3

pip3 install requests

Clone the repository from github

git clone https://github.com/bhupendra27/OsloBySykkel.git

  
## Usage example for executing standalone script after cloning repo


$cd OsloBySykkel

$python3 OsloBySykkel.py

## Result

At station Rostockgata there are 18 bikes available and with 0 docks available

At station Ulven Torg there are 1 bikes available and with 29 docks available

At station Domus Athletica there are 2 bikes available and with 28 docks available


## Appendix

Documentation of real time data for Oslo City Bike

https://oslobysykkel.no/en/open-data/realtime

Page for installation of homebrew

https://docs.brew.sh/Installation
  