import json
import urllib.request as ur
import urllib.parse as par


class Github_user:
    def __init__(self, login='yglukhov'):
        self.login = login

    def get_info_by_rest(self):
        url = 'https://api.github.com/users/' + self.login
        html = ur.urlopen(url).read()
        data = json.loads(html.decode('utf-8'))
        if (data):
            print(data['name'])

            # print("The response contains {0} properties".format(len(data)))
            # print("\n")
            # for key in data:
            #     print
            #     key + " : " + data[key]


g = Github_user()
g.get_info_by_rest()


class Repo:
    prefix = 'https://github.com/'

    def __init__(self, locator='nim-lang/Nim'):
        self.locator = locator
        self.stars = None
        self.contributors = None
        self.commits = None
        self.date = None

    def is_valid(self):
        return True

    def get_full_path(self):
        return Repo.prefix + self.locator

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
