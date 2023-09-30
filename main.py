import csv
#import matplotlib

distinct_values = set() # for the cities
city_count = {}
rec_count = 0
countrecs= 0
with open("weeplace_checkins.csv", "r", newline='', encoding='utf-8') as file:
    csvreader = csv.reader(file)

    for i in csvreader:
        rec_count+=1
        if len(i) >= 5:
            distinct_values.add(i[5])
            city = i[5]
            if city in city_count:
                city_count[city] += 1
            else:
                city_count[city] = 1


distinct_values = sorted(distinct_values)
count = 0
for i in distinct_values:
    #print(i)
    count +=1
print(f'The distinct number of cities are {count}')
print(f"The number of records in the dataset are {rec_count}")

# for city in distinct_values:
#    count = city_count.get(city, 0)
#    print(f"City: {city}, Records: {count}")
# Sort the cities by record count in descending order
sorted_cities = sorted(city_count.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 cities with the most records
for city, count in sorted_cities[:10]:
    print(f"City: {city}, Records: {count}")

