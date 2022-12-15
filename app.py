import json

from models.business import Business
from models.spot import Spot

businesses: list[Business] = []
spots: list[Spot] = []


def fetchBusinesses():
    with open('data/calgary_business_licences.json', 'r') as file:
        data = json.load(file)
        for item in data:
            latitude: str = item.get('latitude')
            longitude: str = item.get('longitude')
            licenseType: str = item['licencetypes']
            if 'FOOD SERVICE' in licenseType and latitude != None and longitude != None:
                businesses.append(
                    Business(
                        tradeName=item['tradename'],
                        address=item['address'],
                        licenceTypes=item['licencetypes'],
                        latitude=float(latitude),
                        longitude=float(longitude)
                    )
                )


def fetchSpots():
    with open('data/on_street_parking_rates.json', 'r') as file:
        data = json.load(file)
        for item in data:
            spots.append(
                Spot(
                    name=item['name'],
                    hourlyPrice=item['hourly_price'],
                    latitude=float(item['latitude']),
                    longitude=float(item['longitude']),
                    permitZone=item['permit_zone']
                )
            )


def findNearParkingLots(restaurantName: str) -> list[Spot]:
    # Improve business logic here lol
    return [spots[2]]


def findCheapParkingLots(restaurantName: str) -> list[Spot]:
    # Improve business logic here lol
    return [spots[0], spots[1]]


def main():
    print('-------------------- Park Me Here --------------------')
    print('The best restaurant parking spot just in your hand.')
    restaurantName = input('What\'s your destination today: ')
    fetchBusinesses()
    fetchSpots()
    nearParkingLots: list[Spot] = findNearParkingLots(restaurantName)
    cheapParkingLots: list[Spot] = findCheapParkingLots(restaurantName)

    while True:
        print('\n')
        option = input('''Select your option
                   1. Near Parking spots
                   2. Cheap parking spots
                   0. Exit
                   ''')

        match option:
            case '0':
                print('Exit')
                break
            case '1':
                print('\n')
                print('-------------------- Here you go --------------------')
                print('The near parking spots will be')
                for i in range(len(nearParkingLots)):
                    spot = nearParkingLots[i]
                    print(
                        f'Permit Zone: {spot.permitZone} | Name: {spot.name} | Hourly price: {spot.hourlyPrice} | how long you can park here: 2 hours | [Press here to navigate]'
                    )
            case '2':
                print('\n')
                print('-------------------- Here you go --------------------')
                print('The cheap parking spots will be')
                for i in range(len(cheapParkingLots)):
                    spot = cheapParkingLots[i]
                    print(
                        f'Permit Zone: {spot.permitZone} | Name: {spot.name} | Hourly price: {spot.hourlyPrice} | how long you can park here: 2.45 hours |[Press here to navigate]'
                    )


main()
