import json
import hashlib

url = 'https://ru.wikipedia.org/wiki/'


class MyIter:

    def __init__(self, path):
        with open(path, encoding='utf-8') as f:
            self.countries_list = []
            file = json.load(f)
            for country in file:
                self.countries_list.append(country['name']['common'])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            country = self.countries_list.pop(0)
            print(f"{country} : {url + country.replace(' ', '_')}")
        except IndexError:
            raise StopIteration
        return country


with open('new_countries_list.txt', 'w') as f:
    for country in MyIter('countries.json'):
        try:
            f.write(f"{country} : {url + country.replace(' ', '_')}\n")
        except UnicodeEncodeError:
            pass

def get_hash():
    with open('new_countries_list.txt', encoding='utf-8') as f:
        for country in f:
            yield hashlib.md5(country.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    country = get_hash()
    for i in country:
        print(i)