import pandas as pd
import numpy as np
import googlemaps
import requests


my_file = 'wip.csv'

google_api_key = 'AIzaSyAs6XXypq9GGQ11P6bWcP3d0Pl1xtf7VOg'

broadband_map_api_key = 'ea8f76637af2064f7292'

# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key=google_api_key)


def geocode(address):
    # Geocoding an address using Google client library
    print address
    try:
        result =  gmaps.geocode(address)
        x =  result[0]['geometry']['location']['lng']
        y =  result[0]['geometry']['location']['lat'] 
        print (x,y)
        return (x,y)
    except:
        return ()
        
        
def get_technologies(co_tup):
    # Query BBmap API and return only available technologies
    my_list = []
    try:
        my_url  = "https://api.broadbandmap.nz/api/1.0/availability/yx/%s/%s?api_key=%s" % (co_tup[1], co_tup[0], broadband_map_api_key)
        response = requests.get(my_url)
        if response.status_code == 200:
            dic = json.loads(response.text)
            for result in dic['results']:
                if result['availability'] == 'Available':
                    my_list.append(result['technology'])
    except:
        my_list = []

        
    print my_list
    return my_list


# load and clean data
my_frame = pd.read_csv(my_file)

my_frame = my_frame[my_frame['Q60ST. Street Name'].isnull() != True]

my_frame =  my_frame.fillna('')

my_frame['address'] = my_frame[column_list[1]] + ' ' + my_frame[column_list[2]] + ' ' + my_frame[column_list[3]] + ' ' + my_frame[column_list[4]]+ ' ' + my_frame[column_list[5]]





# geocode addresses
my_frame['result'] = my_frame['address'].apply(geocode)


# identify technologies from bbmap
my_frame['available_tech'] = my_frame['result'].apply(get_technologies)

# Export csv
my_frame.to_csv('output.csv')
