from flask import Flask, abort, jsonify, request, Response
import requests
import json
import re
from geocodio import GeocodioClient
from pprint import pprint
app = Flask(__name__)
#pip install pygeocodio
#pip install --force-reinstall requests==2.1.0
@app.route('/')
def hello():
  return 'Hello, World!', 202

@app.route('/restaurant', methods=['GET', 'POST'])
def accept():
  geo_api = 'cdd3d0fdfbecafbeaf75d8a0bb50d35b0b3bfec'
  z_key = "bde24dcdc622ec474c29feed7411a8cb"
  try:
    client = GeocodioClient(geo_api)
    addr = request.args.get('address')
    if addr == "" or addr is None:
      return "404 Error: Invalid Adress", 404
    param = "https://api.geocod.io/v1.3/geocode?q=" + addr + "&api_key="+geo_api 
    test = requests.get(param)
    if test.status_code != 200: 
      return "Geocod,io might be down, aborting", 500
    try:
      loc = client.geocode(addr).coords
    except Exception as e:
      return "Invalid Address Input, Returning 404\n",e, 404
    locationUrlFromLatLong = "https://developers.zomato.com/api/v2.1/geocode?lat=" + `loc[0]` + "&lon=" + `loc[1]`
    headers = header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": z_key}
    lst = {}
    lst['restaurant'] = {}
    res = requests.get(locationUrlFromLatLong, headers=header)
    if res.status_code != 200:
      "Wrong Usage or Zomato might be down, Aborting", 500
    data = res.json()
    i = 1 
    for item in data['nearby_restaurants']:
      token = item.get('restaurant')
      name = token.get("name")
      itm_loc = token.get("location")
      address = itm_loc.get("address")
      cuis = token.get("cuisines")
      user_rat = token.get("user_rating")
      rating = user_rat.get("aggregate_rating")
      vals = {"name": name, "address":address, "cuisines":cuis, "rating":rating}
      lst['restaurant'][i] = vals
      i = i+1
    return jsonify(lst), 200
  except Exception as e:
    return "404 Error not found",e , 404
   
   
'''

'''


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

