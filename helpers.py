import json
import urllib.request as ur
import urllib.parse as par
import datetime


def date_from_string(s='2016-03-22T09:38:26Z'):
    d = datetime.date(int(s[0:4]),
                      int(s[5:7]),
                      int(s[8:10]))
    return d

d=date_from_string()

print(d+datetime.timedelta(days=2))
a={date_from_string():1}
print(a.keys(),a.values())

def dict_from_rest(url=' https://api.github.com/yglukhov'):
    html = ur.urlopen(url).read()
    data = json.loads(html.decode('utf-8'))
    return data
