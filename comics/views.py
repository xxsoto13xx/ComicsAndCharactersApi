import json
from django.http import HttpResponse
import requests

# Create your views here.


def comics(request):
    urlcomics = "https://gateway.marvel.com:443/v1/public/comics?ts=1&apikey=7fc9910ea80c6222e9053658f3d21f54&hash=4aeb4b73dc0c3b8b387dba00dce092c5"

    # GETTING COMICS INFO
    comicinformation = requests.get(urlcomics)
    comicinformation = comicinformation.json()
    comicdata = comicinformation['data']
    comicresults = comicdata['results']
    comics = []
    # GETTING NEEDED INFO FROM API
    for result in comicresults:
        dict1 = {}
        dict1['id'] = result['id']
        dict1['title'] = result['title']
        comicimages = result['thumbnail']
        dict1['image'] = comicimages['path'] + '.' + comicimages['extension']
        comicdates = result['dates']
        for comicdat in comicdates:
            if comicdat['type'] == 'onsaleDate':
                dict1['onsaledate'] = comicdat['date']
        comics.append(dict1)

    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        title = request.GET.get('title')
        if keyword != None:
            bykeyword = []
            for comic in comics:
                if keyword in comic['title']:
                    bykeyword.append(comic)
            bykeyword = {'data': bykeyword}
            return_list = list(bykeyword.items())
        elif title != None:
            print(title)
            bytitle = []
            for comic in comics:
                if title == comic['title']:
                    bytitle.append(comic)
            bytitle = {'data': bytitle}
            return_list = list(bytitle.items())
        else:
            byalphabet = []
            orderedbyalphabet = []
            for comic in comics:
                byalphabet.append(comic['title'])
            byalphabet = sorted(byalphabet)
            for item in byalphabet:
                for comic in comics:
                    if item == comic['title']:
                        orderedbyalphabet.append(comic)
            orderedbyalphabet = {'data': orderedbyalphabet}
            return_list = list(orderedbyalphabet.items())
    return HttpResponse(json.dumps(return_list))
