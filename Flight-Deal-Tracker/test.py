data = [{'city': 'Berlin', 'iataCode': 'BML', 'lowestPrice': 200, 'id': 2}, {'city': 'New Delhi', 'iataCode': 'DEL', 'lowestPrice': 1500, 'id': 3}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 500, 'id': 4}, {'city': 'Munich',
                                                                                                                                                                                                                           'iataCode': 'MUC', 'lowestPrice': 300, 'id': 5}, {'city': 'Krakow', 'iataCode': 'KRK', 'lowestPrice': 50, 'id': 6}, {'city': 'Gdansk', 'iataCode': 'GDN', 'lowestPrice': 60, 'id': 7}, {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 350, 'id': 8}]

for item in data:
    print(item["iataCode"])
