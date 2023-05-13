from django.http import HttpResponse
from django.shortcuts import render
import phonenumbers
from folium import Map
from phonenumbers import geocoder,carrier,timezone
import folium
from geopy.geocoders import Nominatim
from django.template import loader
import opencage
from opencage.geocoder import OpenCageGeocode


def index(request):
    return render(request,'index.html')



def fu(request):
    geolocator = Nominatim(user_agent="geoapiExercises")
    numc = {
            'num' : request.GET.get('number','return please')
            }
    
   
    
    details = {
        'parsed_number':phonenumbers.parse(numc['num']),
        'country_name'  : phonenumbers.region_code_for_number(phonenumbers.parse(numc['num'])),
        'timeZone' : timezone.time_zones_for_number(phonenumbers.parse(numc['num'])),
        'company_name' : geocoder.description_for_number(phonenumbers.parse(numc['num'], "RO"), "en"),
        'company_phone'        :   carrier.name_for_number(phonenumbers.parse(numc['num'], "RO"),'en'),
    }
    location = geolocator.geocode(details['country_name'])


    map = Map(location=[location.latitude, location.longitude], zoom_start=15)
    folium.Marker(location=[location.latitude, location.longitude]).add_to(map)

    map.save('Templates/mylocation.html')

     
    	
       
    return render(request,'information.html',details)

def loc(request):
    return render(request,'mylocation.html')


