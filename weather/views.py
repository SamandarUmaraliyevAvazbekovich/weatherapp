from django.shortcuts import render
import requests 
# Create your views here.

def index(request):
	if request.method == 'POST':
		city = request.POST['city']
		print(city)
		natija = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+
			'&units=metric&units=statndart&appid=af9d9d6511061dfbb970a02827bd0346').json()
		
		natija_info = {
			'city': city,
			'temp' : natija['main']["temp"],
			'temp_max' : natija['main']['temp_max'],
			'time' : natija['timezone'],
			'icon' : natija['weather'][0]["icon"]
		}
		context = {
			'info' : natija_info
		} 
		return render(request,'home.html',context=context)
	return render(request,'home.html')
