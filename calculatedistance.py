"""
Author: Fatih Baday
Email: fatih.baday@outlook.com
Purpose: Its calculate distance between Moscow Ring Road and location that given by use http api.
"""

# Loading libraries.
import os
import logging
import datetime
import googlemaps

from config import constant
from flask import Blueprint, make_response, jsonify, request

app_calcdist = Blueprint('calculate_distance', __name__)

# Define constant variables
CONFIG = constant()
GMAPS = googlemaps.Client(key=CONFIG.variables['API_KEY'])


@app_calcdist.route('/api/calcdist', methods=['GET'])
def calcdist():
    """
    Author: Fatih Baday
    Purpose: It calculates the distance between two given locations. Return the result.
    Input:  1. location (str - required on query string)
    Output: 1. result (float)
    """
    location = request.args.get("location")

    # Check location parameters.
    if location is None or type(location) != str:
        logging.warning("Location information is incomplete or sent in the wrong format.")
        msg = {"code": "400",
               "Description": "Error",
               "Error_message": "Location information is incomplete or sent in the wrong format."}
        response = make_response(jsonify(msg))
        response.status_code = 400
        response.headers["Content-Type"] = "application/json"
        return response

    # Calculate distance.
    calc_dist_result = GMAPS.distance_matrix(origins=CONFIG.variables['DEFAULT_LOCATION'],
                                             destinations=location)

    # Check result of calculation. If status is not 'OK', stop function and return error.
    if calc_dist_result["rows"][0]["elements"][0]["status"] != 'OK':
        logging.warning("Distance could not be measured.")
        msg = {"code": "400",
               "Description": "Error",
               "Error_message": "Distance could not be measured."}
        response = make_response(jsonify(msg))
        response.status_code = 400
        response.headers["Content-Type"] = "application/json"
        return response

    # Save result to file.
    file_path = os.path.join("", CONFIG.variables['SAVE_FILE_NAME'])
    result_str = "Destination address: " + str(calc_dist_result["destination_addresses"]) + \
                 " & Origin address: " + str(calc_dist_result["origin_addresses"]) + \
                 " & Distance (text): " + calc_dist_result["rows"][0]["elements"][0]["distance"]["text"] + \
                 " & Distance (value km): " + str(calc_dist_result["rows"][0]["elements"][0]["distance"]["value"]) + \
                 "\n"
    result_str = str(datetime.datetime.now()) + " -> " + result_str
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.writelines(result_str)

    else:
        with open(file_path, 'a') as file:
            file.writelines(result_str)

    return jsonify(calc_dist_result)
