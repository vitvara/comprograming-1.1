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

# city_temp_tuple = []
# for i in cities_data:
#     city_temp_tuple.append((i["city"],i['temperature']))
   
# print(city_temp_tuple)

# list_1 = [[1,2,3],[4,5,6]]

# for i in list_1:
#     string = ""
#     for j in i:
#         string += str(j) + ","
#     print(string[:-1])

# for i, k in zip(list_1[0],list_1[1]):
#     print(str(i)+","+str(k))

def list_countries(data):
    list_return = []
    for i in data:
        if i["country"] not in list_return:
            list_return.append(i["country"])
    return(list_return)
# countries = list_countries(cities_data)
# print(len(countries))
# print(countries)
def compute_ave_country_temp(data):
    local_dict = {}
    for i in list_countries(data):
        sum_temp = 0
        count = 0
        for j in data:
            if i == j["country"]:
                sum_temp += float(j['temperature'])
                count += 1
        local_dict[i] = sum_temp/ count
    return local_dict
            
# country_temps = compute_ave_country_temp(cities_data)
# print(len(country_temps))
# print(country_temps)
import csv
import matplotlib.pyplot as plt

def read_file(file):
    cities_data = []
    with open('lecture8/afternoon/cities.csv') as f:
        rows = csv.DictReader(f)
        for r in rows:
            cities_data.append(r)
    return cities_data
    
def extract_to_list(data, type):
    return_list = []
    for i in data:
        return_list.append(float(i[type]))
    return return_list

# cities_data = read_file('cities.csv')
# lat = extract_to_list(cities_data,'latitude')
# long = extract_to_list(cities_data,'longitude')
# temps = extract_to_list(cities_data,'temperature')
# high = extract_to_list(cities_data,'highest')

# # Plot scatter plot using x = latitude,
# # y = temperature,
# # color=longitude
# plt.scatter(lat,temps,c=long)
# # Add x-axis label
# plt.xlabel('Latitude')
# # Add y-axis label
# plt.ylabel('Temperatures')
# # Add label for color bar
# plt.colorbar().ax.set_title('Longtitude')
# # Save plot as image file
# plt.savefig('lat_temps_long.png')
# # Show plot
# plt.show()

# plt.scatter(long,temps,c=lat)
# plt.xlabel('Longitude')
# plt.ylabel('Temperatures')
# plt.colorbar().ax.set_title('Latitude')
# # Set colormap to the selected one
# # See more colormap selection in the reference at the end of

# plt.set_cmap('RdBu')
# plt.savefig('long_temps_lat.png')
# plt.show()

def count_region_freq(data):
    count_dict = {}
    name = []
    for i in data:
        if i["region"] not in count_dict:
            count_dict[i["region"]] = 1
            name.append(i["region"])
        count_dict[i["region"]] = count_dict[i["region"]] + 1

    return name, list(count_dict.values())


import csv
import matplotlib.pyplot as plt
cities_data = read_file('cities.csv')
region_list, region_freq_list = count_region_freq(cities_data)
# Set up bar colors in bar graph
# See more color names in the reference at the end of Exercise 6
my_colors = ['red','blue','green','orange']
# Plot bar graph using x = unique region list
# y = region frequency
# Bar graph color is set to my_colors list
plt.bar(region_list, region_freq_list, color=my_colors)
plt.xlabel('Region')
plt.ylabel('Frequency')
plt.savefig('region_freq.png')
plt.show()


