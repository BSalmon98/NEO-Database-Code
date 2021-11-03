"""Extract data on near-Earth objects and close approaches from CSV\
   and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
                         near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_collection = []
    with open(neo_csv_path, 'r') as neo_csv:
        neo_reader = csv.reader(neo_csv)
        next(neo_reader)
        for row in neo_reader:
            if row[7] == 'Y':
                neo_collection.append(NearEarthObject(
                    row[3], row[4], row[15], True))
            else:
                neo_collection.append(NearEarthObject(
                    row[3], row[4], row[15], False))
    return neo_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about
                         close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approach_collection = []
    with open(cad_json_path, 'r') as cad_json:
        approaches = json.load(cad_json)
        for row in approaches['data']:
            approach_collection.append(CloseApproach(
                row[0], row[3], row[4], row[7]))
        return approach_collection
