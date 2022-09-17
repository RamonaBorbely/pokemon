from tui import *

"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""


# TODO: Your code here


def retrieve_total_records(list_of_records):
    total_records(len(list_of_records))


def retrieve_record_by_serial_no(list_of_records):
    serial_no = serial_number()
    if serial_no < 1 or serial_no > 633:
        print("The serial number should be between 1 and 633")
    else:
        for record in list_of_records[1:]:
            if serial_no == int(record[0]):
                return record


def retrieve_records_by_date(list_of_records):
    dates = observation_dates()
    records_to_return = []
    for record in list_of_records[1:]:
        for date in dates:
            if record[1] == date:
                records_to_return.append(record)
    return records_to_return


def retrieve_records_by_region(list_of_records):
    country = []  # to hold the dict keys
    records_by_country = {}

    for row in list_of_records[1:]:
        country.append(row[3])  # taking keys frm list of lists

    keys_for_dict = set(country)  # make keys to not repeat

    for i in keys_for_dict:
        records_by_country[i] = []  # adding keys to dict and a list to each key to fill later

    for row in list_of_records[1:]:
        for key in records_by_country:
            if row[3] == key:
                records_by_country[key].append(row)
    for key in records_by_country:
        print(key, records_by_country[key])
    return records_by_country


def retrieve_summary(list_of_records):
    countries = []
    all_countries = []
    summary = {}
    summed = {}
    confirmed, deaths, recovered = 0, 0, 0
    for row in list_of_records[1:]:
        countries.append(row[3])

    for country in countries:
        if country not in all_countries:
            all_countries.append(country)

    for key in all_countries:
        summary[key] = []

    for row in list_of_records[1:]:
        for key in summary:
            if row[3] == key:
                summary[key].append([row[5], row[6], row[7]])

    for key, value in summary.items():
        for i in range(len(value)):
            confirmed += int(value[i][0])
            deaths += int(value[i][1])
            recovered += int(value[i][2])
        summed[key] = [confirmed, deaths, recovered]

    return summed








