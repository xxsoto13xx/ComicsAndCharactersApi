import json
from django.http import HttpResponse
import requests

# Create your views here.


def characters(request):

    # API URL
    url = "https://gateway.marvel.com:443/v1/public/characters?ts=1&apikey=7fc9910ea80c6222e9053658f3d21f54&hash=4aeb4b73dc0c3b8b387dba00dce092c5"

    # GETTING CHARACTERS INFO
    characterinformation = requests.get(url)
    characterinformation = characterinformation.json()
    characterdata = characterinformation['data']
    characterresults = characterdata['results']
    characters = []

    # GETTING NEEDED INFO FROM API
    for result in characterresults:
        dict2 = {}
        dict2['id'] = result['id']
        dict2['name'] = result['name']
        characterimages = result['thumbnail']
        dict2['image'] = characterimages['path'] + \
            '.' + characterimages['extension']
        comicappearances = result['comics']
        dict2['appearances'] = comicappearances['available']
        characters.append(dict2)

    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        title = request.GET.get('name')
        if keyword != None:
            bykeyword = []
            for character in characters:
                if keyword in character['name']:
                    bykeyword.append(character)
            bykeyword = {'data': bykeyword}
            return_list = list(bykeyword.items())
        elif title != None:
            print(title)
            bytitle = []
            for character in characters:
                if title == character['name']:
                    bytitle.append(character)
            bytitle = {'data': bytitle}
            return_list = list(bytitle.items())
        else:
            byalphabet = []
            orderedbyalphabet = []
            for character in characters:
                byalphabet.append(character['name'])
            byalphabet = sorted(byalphabet)
            for item in byalphabet:
                for character in characters:
                    if item == character['name']:
                        orderedbyalphabet.append(character)
            orderedbyalphabet = {'data': orderedbyalphabet}
            return_list = list(orderedbyalphabet.items())
    return HttpResponse(json.dumps(return_list))
