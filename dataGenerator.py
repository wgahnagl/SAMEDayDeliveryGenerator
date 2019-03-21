import names
import csv
import random
from random import randrange
import time
from faker import Faker

fake = Faker()


def email_generator():
    email_list = ["gmail.com", "yahoo.com", "aol.com", "comcast.net", "outlook.com", "gearsgearsgears.com",
                  "csh.rit.edu"]
    random_dot = [".", ""]
    return names.get_first_name(None) + random.choice(random_dot) + names.get_last_name() + "@" + random.choice(
        email_list)


def vehicle_generator():
    vehicles = ["car", "plane", "truck"]
    return random.choice(vehicles)


def origin_customer():
    # TODO: add real customers
    return "customer"


def destination_customer():
    # TODO: add real customers
    return "customer"


def package_size():
    return randrange(0, 100)


def package_type():
    types = ['letter', 'package', 'cool']
    return random.choice(types)


def package_weight():
    return randrange(1, 1000)


def package_info():
    # TODO: info should have real info
    return "info"


def package_price():
    return "$" + str(randrange(1, 100))


def package_signature_id():
    # TODO: signature should have an actual signature
    return "signature"


def time_interval_generator():
    ship_timestamp = randrange(1546300800, 1550534400)
    if randrange(0, 2) == 1:
        delivery_timestamp = randrange(1550620800, int(time.time()))
    else:
        delivery_timestamp = None

    expected_delivery_date = randrange(1550620800, int(time.time()) + 14 * (24 * 60 * 60))
    return {
        "ship_timestamp": ship_timestamp,
        "delivery_timestamp": delivery_timestamp,
        "expected_delivery_date": expected_delivery_date
    }


def generate_data(amount, people, carriers, packages):
    created_data = []
    i = 0
    for x in range(0, amount):
        i += 1
        person = []
        carrier = []
        package = []
        if people:
            person.append(email_generator())
            created_data.append(person)

        if carriers:
            carrier.append(i)
            carrier.append(vehicle_generator())
            created_data.append(carrier)

        if packages:
            package.append(i)
            package.append(origin_customer())
            package.append(destination_customer())
            time_interval = time_interval_generator()
            package.append(time_interval["ship_timestamp"])
            package.append(time_interval["delivery_timestamp"])
            package.append(package_size())
            package.append(package_type())
            package.append(package_weight())
            package.append(package_info())
            package.append(package_price())
            package.append(time_interval["expected_delivery_date"])
            package.append(package_signature_id())
            created_data.append(package)

    return created_data


def generate_carriers(number):
    return generate_data(number, False, True, False)


def generate_packages(number):
    return generate_data(number, False, False, True)


def generate_people(number):
    return generate_data(number, True, False, False)


def write_csv(name, elements):
    with open(name + ".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for entry in elements:
            writer.writerow(entry)


write_csv("packagesData", generate_packages(10))
write_csv("carriersData", generate_carriers(10))
write_csv("peopleData", generate_people(10))
