import pandas as pd
import numpy as np
import googlemaps


my_file = 'wip.csv'

google_api_key = '<key>'

# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key=google_api_key)

# Geocoding and address
def geocode(address):
    print address
    try:
        result =  gmaps.geocode(address)
        x =  result[0]['geometry']['location']['lng']
        y =  result[0]['geometry']['location']['lat'] 
        print (x,y)
        return (x,y)
    except:
        return ()


my_frame = pd.read_csv(my_file)

my_frame = my_frame[my_frame['Q60ST. Street Name'].isnull() != True]

my_frame =  my_frame.fillna('')

my_frame['address'] = my_frame[column_list[1]] + ' ' + my_frame[column_list[2]] + ' ' + my_frame[column_list[3]] + ' ' + my_frame[column_list[4]]+ ' ' + my_frame[column_list[5]]


my_frame['result'] = my_frame['address'].apply(geocode)




