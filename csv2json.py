# This is a sample Python script to convert a csv file to json
import os
from tkinter import filedialog as fd
import csv
import json

if __name__ == '__main__':
    # select from a desktop modal window dialog the csv files to be converted
    csvList = fd.askopenfilenames(
        title='Select csv files',
        filetypes=(('Python files', '*.csv'), ('All files', '*.*'))
    )
    # for each selected file
    for csvName in csvList:
        # get csv name, define json name
        csvFullPath, c = os.path.split(csvName)
        jsonName = c[:-4] + '.json'
        # process file
        with open(csvName, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.DictReader(csvfile, dialect=dialect)
            data = [row for row in reader]
        with open(os.path.join(csvFullPath, jsonName), 'w') as jsonfile:
            json.dump(data, jsonfile)
