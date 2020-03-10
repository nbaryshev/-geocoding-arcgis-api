import flask
import requests
import csv
from io import StringIO
import logic

app = flask.Flask(__name__)


@app.route('/getAddresses', methods=('GET','POST'))
def get_addresses():
    csv_file_url = flask.request.form.get("file")
    csv_file_content = requests.get(csv_file_url).text

    f = StringIO(csv_file_content)
    reader = csv.reader(f, delimiter=',')
    csv_data = list(reader)
    csv_data.pop(0)

    points = []
    links = []

    for row in csv_data:
        name = row[0]
        latitude = float(row[1])
        longitude = float(row[2])


        points.append({'name': name, 'address': logic.geocoding(latitude, longitude), 'coordinates': (latitude, longitude)})


    processed_distances = []

    for point1 in points:
        for point2 in points:
            combinated_name1 = point1['name'] + point2['name']
            combinated_name2 = point2['name'] + point1['name']

            if combinated_name1 in processed_distances or combinated_name2 in processed_distances:
                continue

            if point1['name'] == point2['name']:
                continue

            processed_distances.append(combinated_name1)

            links.append({'name': combinated_name1, "distance": logic.destination(tuple(point1['coordinates']), tuple(point2['coordinates']))})


    result = {'points': points, 'links': links}

    return flask.jsonify(result)


if __name__ == '__main__':
    app.run(port=5000)


