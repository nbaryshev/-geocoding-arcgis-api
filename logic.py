import arcgis
from haversine import haversine, Unit


def geocoding(latitude, longitude):
    """
    Geocodes the address basing on latitude and longitude
    """
    gis = arcgis.gis.GIS("https://www.arcgis.com/", "Niktia", "polo8Ret")

    results = arcgis.geocoding.reverse_geocode([latitude, longitude])

    return results


#
# lyon = (45.7597, 4.8422) # (lat, lon)
# paris = (48.8567, 2.3508)
#
# print(haversine(lyon, paris))
#
#
def destination(city1, city2):

    cities_dest = haversine(city1, city2, Unit.METERS)

    return cities_dest
#
#
# def convertTuple(tup):
#     str =  ''.join(tup)
#     return str
#
# list=[]
# for i in combinations([a['name'],b['name'],c['name']], 2):
#     cities = convertTuple(i)
#     # print(cities)
#     list.append({"name": cities, "destination":haversine((a['latitude'], a['longitude']), (b['latitude'], b['longitude']))})
# print(list)
#
#
# # a = {'name': "A",
# #     'latitude': 50.412,
# #     'longitude': 30.124
# #     }
# #
# # b = {'name': "B",
# #     'latitude': 50.346,
# #     'longitude': 30.437,
# #     }
# #
# # c = {'name': "C",
# #     'latitude': 70.346,
# #     'longitude': 14.437
# #     }
