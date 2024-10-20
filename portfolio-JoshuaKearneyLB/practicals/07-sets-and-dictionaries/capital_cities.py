#!/usr/bin/env python3



def chomp(s):
    return s[:-1]


def read_city_file(filename = 'capital_cities.txt'):

    cities = {}

    with open(filename, 'r') as cityfile:
        for line in cityfile:
            country, capital = line.split(',')
            cities[country] = chomp(capital)
    cityfile.close()
    return cities


def write_city_file(cities, filename = 'capital_cities.txt'):
    with open(filename, 'w') as cityfile:
        for country in cities:
            cityfile.write(f"{country},{cities[country]}\n")
    cityfile.close()


if __name__ == '__main__':

    cities = read_city_file()
    print("If you wish the exit the program at anytime type 'exit' ")

    while True:
        country_input = input("Enter a country: ")
        country_input = country_input.lower()

        if country_input == "exit":
            break
        elif country_input in cities:
            print(f"The capital of {country_input} is {cities[country_input]}")
        else:
            capital = input(f"Enter the capital of {country_input}: ")
            cities[country_input] = capital

        print(cities)
        write_city_file(cities)
