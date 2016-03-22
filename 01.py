from helpers import *


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


class Repo:

    def __init__(self, locator='yglukhov/nimx'):
        self.locator = locator

    def is_valid(self):
        return True

    def get_repo_info(self):
        url = 'https://api.github.com/repos/'\
              + self.locator + '/commits'
        # https://api.github.com/yglukhov/nimx as example
        # curl -i "https://api.github.com/repos/show/nimx"
        data=dict_from_rest(url)
        print(data)
        # for key in data:
        #     print(key, data[key])

r=Repo()
r.get_repo_info()

class Organisation:
    def __init__(self,locator):
        self.locator=locator


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
