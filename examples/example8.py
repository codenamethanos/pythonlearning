import random

offer1 = {
    "url": "www.offer1.com",
    "weight": 30 
}

offer2 = {
    "url": "www.offer2.com",
    "weight": 60
}

# Total Weight: 90
print(30/90*100)
print(60/90*100)

total_weight = offer1["weight"] + offer2["weight"]

offer1_count = 0
offer2_count = 0

for i in range(0, 100):
    random_number = random.random()
    if random_number <= (offer1["weight"] / total_weight):
        offer1_count += 1
    else:
        offer2_count += 1

print("Offer 1: " + str(100*offer1_count/(offer1_count + offer2_count)))
print("Offer 2: " + str(100*offer2_count/(offer1_count + offer2_count)))