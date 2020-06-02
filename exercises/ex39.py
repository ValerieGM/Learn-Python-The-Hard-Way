# creating a mapping of provinces to abbreviation
provinces = {
    'Gauteng': 'GP',
    'Mpumalanga': 'MP',
    'Limpopo': 'LP',
    'Free State': 'FS',
    'Western Cape': 'WC'
}

# creating a basic set of provinces and some cities in them
cities = {
    'GP': 'Pretoria',
    'FS': 'Bloomfontein',
    'WC': 'Cape Town'
}

# add some more cities
cities['MP'] = 'Nelspruit'
cities['LP'] = 'Polokwane'

# print out some cities
print('-' * 10)
print("MP Provine has: ", cities['MP'])
print("LP Province has: ", cities['LP'])

# print some provinces
print('-' * 10)
print("Gauteng's abbreviation is: ", provinces['Gauteng'])
print("Free State's abbreviation is: ", provinces['Free State'])

# do it by using the province then the cities dict
print('-' * 10)
print("Gauteng has: ", cities[provinces['Gauteng']])
print("Free State has: ", cities[provinces['Free State']])

# print every province abbreviation
print('-' * 10)
for province, abbrev in list(provinces.items()):
    print(f"{province} is abbreviated {abbrev}")
    
# print every city in province
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
    
# both at the same time
print('-' * 10)
for province, abbrev in list(provinces.items()):
    print(f"{province} province is abbrevited {abbrev}")
    print(f"And has city {cities[abbrev]}")
    
print('-' * 10)
# safely get an abbreviation by province that might not be there
province = provinces.get('Eastern Cape')

if not province:
    print("Apologies, no Eastern Cape")
    
# get a city by default value
city = cities.get('EC', 'Does Not Exist')
print(f"The city for the province 'EC' is: {city}")