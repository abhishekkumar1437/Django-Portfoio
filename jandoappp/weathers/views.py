from django.shortcuts import render
import urllib.request
import json
import datetime

x = datetime.datetime.now()


def weathers(request):
    
    if request.method == 'POST': 
        city = request.POST['city'] 
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=fc55b08658db9fa4424173680994f3cb').read() 

        list_of_data = json.loads(source) 
        data = {
            
            'city':city,
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + ' °C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
            
          
        } 
        print(data)
       
    else: 
        data ={} 
    return render(request, "weather.html", data) 

    