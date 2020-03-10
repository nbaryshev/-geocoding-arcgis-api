import flask
import requests
import csv
from io import StringIO
import logic

# initiating the app
app = flask.Flask(__name__)

# creating the route /getAddress
@app.route('/getAddresses', methods=('GET','POST'))
def get_addresses():
    # loading the file and reading it
    csv_file_url = flask.request.form.get("file")
    csv_file_content = requests.get(csv_file_url).text

    # simulating csv file as csv_file_content is a simple text now
    f = StringIO(csv_file_content)
    reader = csv.reader(f, delimiter=',') # "," set up as a delimiter now
    csv_data = list(reader)
    csv_data.pop(0) # excluding heading as we don't need it for the further processing

    points = [] # store all points
    links = [] # store links

    # iterating through the data in csv
    for row in csv_data:
        name = row[0]
        latitude = float(row[1])
        longitude = float(row[2])

        # logic file consist all manipulations with arcgis API and calculating the destination between the links
        points.append({'name': name, 'address': logic.geocoding(latitude, longitude), 'coordinates': (latitude, longitude)})

    # combiations of destinations
    processed_distances = []

    # check if destination already exists, if no then we add it
    for point1 in points:
        for point2 in points:
            combinated_name1 = point1['name'] + point2['name']
            combinated_name2 = point2['name'] + point1['name']

            if combinated_name1 in processed_distances or combinated_name2 in processed_distances:
                continue

            if point1['name'] == point2['name']:
                continue

            processed_distances.append(combinated_name1)

            # logic file consist all manipulations with arcgis API and calculating the destination between the links
            links.append({'name': combinated_name1, "distance": logic.destination(tuple(point1['coordinates']), tuple(point2['coordinates']))})

    # collecting all results
    result = {'points': points, 'links': links}

    #return the result in JSON format
    return flask.jsonify(result)


if __name__ == '__main__':
    app.run(port=5000)


