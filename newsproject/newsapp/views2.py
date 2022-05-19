from django.shortcuts import render

import requests
# Create your views here.
def suicidios(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=dc3a210ad053ab105a0848cf9b24ba1c&countries=mx&keywords=suicidios')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        if i['image'] is not None:
            imagen = i['image']
        else:
            imagen = 'https://acortar.link/GM02v8'
        title. append (i['title'])
        description . append (i['description'])
        image. append ( 
            imagen
        )
        url.append (i['url'])
    news = zip(title, description, image, url)
    return render(request,'newsapp/suicidios.html', {'news':news})
