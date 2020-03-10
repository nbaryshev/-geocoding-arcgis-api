import arcgis
from haversine import haversine, Unit


def geocoding(latitude, longitude):
    """
    Geocodes the address basing on latitude and longitude
    """
    # accessing the data and the source
    gis = arcgis.gis.GIS("https://www.arcgis.com/", "Niktia", "polo8Ret")

    # reverse_geocode returns the address details
    results = arcgis.geocoding.reverse_geocode([latitude, longitude])

    return results


def destination(city1, city2):
    """
    :param city1:
    :param city2:
    :return: Meters
    """

    # haversine function calculates the destination basing on longitude and latitude
    cities_dest = haversine(city1, city2, Unit.METERS) # meters

    return cities_dest
