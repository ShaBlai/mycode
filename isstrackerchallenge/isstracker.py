#!/usr/bin/env python3



"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg


URL= "http://api.open-notify.org/iss-now.json"
def main():
    #getting the jSON data from the ISS api and setting it to resp
    resp= requests.get(URL).json()
    
    
    #combing through the JSON and setting it
    longitude = resp['iss_position']['longitude']
    latitude = resp['iss_position']['latitude']
    epochtimestamp = resp['timestamp']
    
    #inputting the coords into the tuple
    coords_tuple = (latitude, longitude)
    
    georesults = rg.search(coords_tuple, verbose=False)
    
    current_city = georesults[0]['name']
    current_country = georesults[0]['cc']
             
    
    #setting the datetime from the epoch time
    date_time = datetime.datetime.fromtimestamp(epochtimestamp)
        
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Timestamp: {date_time}")
    print(f"Long: {longitude}")    
    print(f"Lat: {latitude}")
    print(f"City/Country: {current_city}, {current_country}")

if __name__ == "__main__":
    main()
