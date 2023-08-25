import requests

re=requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=d742781a1b4c177b2351836c6436933e&user_id=196319389%40N04&format=json&nojsoncallback=1")
if re.status_code==200:
    print(re.json())
