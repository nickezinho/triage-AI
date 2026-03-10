import googlemaps

MAPS_API_KEY = 'AIzaSyAWJBDjW-mOYDGFNm4p1RhxN7csM_TPVRs'


class MapsService:

    def __init__(self):
        self.client = googlemaps.Client(MAPS_API_KEY)

    def search_hospital(self, lat, lng, speciality):
        
        #location = (-23.3169879, -46.7303273)
        response = self.client.places_nearby(
            location = (lat,lng),
            radius=10000,
            keyword = f'hospital especializado em {speciality}',
        )

        hospital = []

        for places in response['results']:

            place_id = places["place_id"]

            hospital.append({
                "name": places['name'],
                "address":places.get("vicinity"),
                "maps_link":f"https://www.google.com/maps/place/?q=place_id:{place_id}"
            })
        
        print(hospital)
        return hospital