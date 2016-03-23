from helpers import *
import datetime

class Github_user:
    def __init__(self, login='yglukhov'):
        self.login = login

    def get_user_info_by_rest(self):
        url = 'https://api.github.com/users/' + self.login
        data = dict_from_rest(url)
        # for key in data:
        #     print(key, data[key])


g = Github_user()
g.get_user_info_by_rest()


def commit_stat(data):
    assert len(data) > 0
    # days=["Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday","Sunday"]
    days=["Mon","Tue","Wed","Thu", "Fri", "Sat","Sun"]
    print(type(data[0]['commit']['committer']['date']))
    start_date = date_from_string(data[len(data) - 1]['commit']['committer']['date'])
    end_date = date_from_string(data[0]['commit']['committer']['date'])
    assert start_date<=end_date
    date=start_date
    commits={}
    while date<=end_date:
        commits[date]=0
        # print(days[datetime.date.weekday(date)])
        date+=datetime.timedelta(days=1)

    for i in range(len(data)):
        date=date_from_string(data[i]['commit']['committer']['date'])
        commits[date]+=1
    # for i in commits.values():
    #     print(i)
    # print(commits)
    points=[]
    graf_keys=[]
    while date<=end_date:
        graf_keys.append(days[datetime.date.weekday(date)])
        points.append(commits[date])
        # print(days[datetime.date.weekday(date)], commits[date])
        date+=datetime.timedelta(days=1)

    return graf_keys,points


class Repo:
    def __init__(self, locator='yglukhov/nimx'):
        self.locator = locator

    def is_valid(self):
        return True

    def get_repo_info(self):
        url = 'https://api.github.com/repos/' \
              + self.locator + '/commits'
        # https://api.github.com/yglukhov/nimx as example
        # curl -i "https://api.github.com/repos/show/nimx"
        data = dict_from_rest(url)
        # print (date_from_string(data[0]['commit']['committer']['date']))
        # 2016-03-22T09:38:26Z

        # for i in range(len(data)):
        #     print (date_from_string(data[i]['commit']['committer']['date']))
        print(commit_stat(data))


r = Repo()
r.get_repo_info()


# string='2016-03-22T09:38:26Z'
# d=time.strptime(string)

class Weather:
    pass


class Organisation:
    def __init__(self, locator):
        self.locator = locator

# 1.1. Для обраного проекту формувати графік:
# 1) за кількістю нових зірочок за період (тиждень\місяць);
# 2) за кількістю унікальних контрибюторів за період;
# 3) за кількістю комітів за період.
# 1.2. Сортувати проекти (знаходити топ кількість) за вищевказаними критеріями.
# 1.3. Сортувати організації (знаходити топ кількість) за:
# 1) абсолютною кількістю комітів за період;
# 2) середньою кількістю комітів (враховуючи кількість співробітників
#  організації).
# 1.4. Дані необхідно агрегувати та тримати у підготовленому стані
# на стільки, на скільки це
# можливо, аби час відповіді був мінімальним.
