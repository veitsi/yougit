from enum import Enum


class Indicators(Enum):
    stars = 1
    contributors = 2
    commits = 3


class Resources(Enum):
    github = 1


class Period(Enum):
    week = 1
    sprint = 2
    month = 3


if __name__ == "__main__":
    for i in Period:
        print(i)
