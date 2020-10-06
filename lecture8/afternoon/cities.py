import csv
# cities_data = []
# with open('lecture8/afternoon/cities.csv', 'r', encoding='UTF-8') as f:
#     rows = csv.reader(f)
#     for r in rows:
#         cities_data.append(r)

# print(cities_data[0:10])
# print(cities_data[8:10])

cities_data = []
with open('lecture8/afternoon/cities.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)

city_temp_tuple = []
for i in cities_data:
    city_temp_tuple.append((i["city"],i['temperature']))
   
print(city_temp_tuple)

# list_1 = [[1,2,3],[4,5,6]]

# for i in list_1:
#     string = ""
#     for j in i:
#         string += str(j) + ","
#     print(string[:-1])

# for i, k in zip(list_1[0],list_1[1]):
#     print(str(i)+","+str(k))
