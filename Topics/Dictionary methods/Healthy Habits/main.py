
total_meters = 0
for i in walks:
    total_meters += i["distance"]

print (total_meters // len(walks))