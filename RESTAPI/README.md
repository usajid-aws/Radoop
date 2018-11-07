est-API Assignment
---
## Credits
- **Usama Sajid - us71** 
- **Ammaar Muhammad Iqbal - ami76**
---
## Accomplishments
We used python flask to create a RESTful service that returned
list of nearby restaurants given an address.
Project makes use of Geocod.io and Zomato APIs, right now only
availible in US / Canada. Address have to bound to these regions.
---

## Issues
No real issues faced during this project

---
## Requirements
Python Installed
#### Some Packeges used
- `pip install pygeocodio`
- `pip install flask`

_If Running on Ilabs:
issues may arrise with Requests. Was able to fix with
**`pip install --force-reinstall requests==2.1.0`**_
---
## Usage
flask will run on server and will use local IP/restaurant as DNS on Port 5000.
Application takes `address` as query parameters. 

E.g.
### On Server running flask
**`python service.py`**
### Testing on Linux/Unix
**`curl ls.cs.rutgers.edu:5000/restaurant?address=84JoyceKilmerAve#117D,PiscatawayTownship,NJ,08854`**
### Testing on Windows
**`wget ls.cs.rutgers.edu:5000/restaurant?address=84JoyceKilmerAve#117D,PiscatawayTownship,NJ,08854`**

### Results
```
{
    "restaurant": {
        "1": {
            "address": "809 W Court St, Winnfield 71483",
            "cuisines": "Mexican",
            "name": "El Patio Mexican Restaurant",
            "rating": "3.6"
        },
        "2": {
            "address": "1601 E Lafayette St, Winnfield 71483",
            "cuisines": "American",
            "name": "Grantadams Dairy Maid",
            "rating": "3.8"
        },
        "3": {
            "address": "1004 E Lafayette St, Winnfield 71483",
            "cuisines": "",
            "name": "Brenda's Chicken Inn",
            "rating": "3.7"
        },
        "4": {
            "address": "700 W Ct St, Winnfield 71483",
            "cuisines": "American, Diner, Southern",
            "name": "Embers Restaurant of La Incorporated",
            "rating": "3.5"
        },
        "5": {
            "address": "908 W Ct St, Winnfield 71483",
            "cuisines": "Fast Food, Pizza",
            "name": "Pizza Hut",
            "rating": "2.7"
        },
        "6": {
            "address": "1409 W Ct St, Winnfield 71483",
            "cuisines": "Donuts",
            "name": "Donut Palace",
            "rating": "3.3"
        },
        "7": {
            "address": "703 West Court Street, Winnfield 71483",
            "cuisines": "Fast Food",
            "name": "Sonic Drive-in",
            "rating": "3.1"
        },
        "8": {
            "address": "109 South Abel Street, Downtown Winnfield, Louisiana 71483",
            "cuisines": "American",
            "name": "Pea Patch Gallery & Cafe",
            "rating": "3.3"
        },
        "9": {
            "address": "103 Hwy 84 West 71483",
            "cuisines": "Fast Food",
            "name": "McDonald's",
            "rating": "2.8"
        }
    }
}
```
### API Keys
API Keys are located on lines 16 & 17
**geo_api: api key from geocod.io**
**z_key: api key from zomato**

---
### Extra docs
full_call.txt - a text file with full api call returned from Zomato
data.txt - a text file with parsed data about each resteraunt from Zomat
