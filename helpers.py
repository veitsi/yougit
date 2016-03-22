import json
import urllib.request as ur
import urllib.parse as par

def dict_from_rest(url=' https://api.github.com/yglukhov'):
        html = ur.urlopen(url).read()
        data = json.loads(html.decode('utf-8'))
        return data