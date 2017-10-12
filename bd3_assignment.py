import json
from collections import Counter


def load_data(filename):
    with open(filename, encoding='utf-8-sig') as json_file:
        data = json.load(json_file)
        return data


def q_3a():
    result = []
    data = load_data('Assgcars.json')
    for item in data:
        make = item['Manufacturer']
        model = item['Model']
        if make == 'Skoda' and model == 'Octavia':
            result.append(item['Price'])
    return result


def q_3b():
    count = 0
    total = 0.0
    data = load_data('Assgcars.json')
    for item in data:
        make = item['Manufacturer']
        if make == 'Skoda':
            total += item['Price']
            count += 1
    return total / count


def q_3c():
    cnt = Counter()
    tot = Counter()
    avg = []
    data = load_data('Assgcars.json')
    for item in data:
        make = item['Manufacturer']
        if make == 'Skoda':
            cnt[item['Model']] += 1
            tot[item['Model']] += item['Price']
            print(item)
    print(cnt)
    while len(cnt) > 0:
        count = float(cnt.popitem()[1])
        total = float(tot.popitem()[1])
        avg.append(total / count)
    return avg


def main():
    result = q_3a()
    print(result)

    result = q_3b()
    print(result)

    result = q_3c()
    print(result)


if __name__ == "__main__":
    main()


# todo implement all queries in Python functions which return a list of values
# todo replicate as MongoDB queries using PyMongo
# todo write unit tests to verify equality
