"""
Usage:
  python main.py parse_raw_athlete_events_to_csv
  python main.py identify_unique_games_to_json    > olympics/import_json/games.json
  python main.py parse_countries_csv_to_json      > olympics/import_json/countries.json
  python main.py generate_games_script_commands   > tmp/games_script_commands.txt
  python main.py parse_athlete_events_csv_to_json <game> > olympics/import_json/<game>.json
  python main.py generate_games_import_commands   > tmp/games_import_commands.txt
  python main.py generate_mongo_init_commands     > tmp/mongo_init_commands.txt
  -
  python main.py parse_openflights_data airports  > openflights/import_json/airports.json
  python main.py parse_openflights_data airlines  > openflights/import_json/airlines.json
  python main.py parse_openflights_data routes    > openflights/import_json/routes.json
  python main.py parse_openflights_data planes    > openflights/import_json/planes.json
  python main.py parse_openflights_data countries > openflights/import_json/countries.json
  -
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import csv
import json
import os
import sys
import time
import traceback
import uuid

from datetime import datetime

from docopt import docopt

RAW_ATHLETTE_EVENTS    = '../olympics/raw/athlete_events.csv'
RAW_COUNTRIES          = '../olympics/raw/noc_regions.csv'
PARSED_ATHLETTE_EVENTS = '../olympics/raw/athlete_events_parsed.csv'
GAMES_JSON             = '../olympics/import_json/games.json'
PARSED_CSV_FIELD_DELIM = '|'
VERSION = 'November 2021'


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=VERSION)
    print(arguments)

def parse_raw_athlete_events_to_csv():
    infile  = RAW_ATHLETTE_EVENTS
    outfile = PARSED_ATHLETTE_EVENTS
    print('parse_raw_athlete_events_to_csv: {}'.format(infile))
    fields = "id|name|sex|age|height|weight|team|noc|games|year|season|city|sport|event|medal|medal_value".split('|')
    rows, row = list(), list()
    print("field count: {} {}".format(str(len(fields)), fields))
    
    # header row
    for field in fields:
        row.append(field)
    rows.append(row)

    with open(infile, 'rt') as csvfile:
        rdr = csv.DictReader(csvfile)
        for idx, obj in enumerate(rdr):
            row = list()
            if idx < 300000:
                #print(obj)
                row.append(parse_int(obj['id']))
                row.append(parse_str(obj['name']))
                row.append(parse_str(obj['sex']).lower())
                row.append(parse_int(obj['age']))
                row.append(parse_float(obj['height']))
                row.append(parse_float(obj['weight']))
                row.append(parse_str(obj['team']).lower())
                row.append(parse_str(obj['noc']).lower())
                row.append(parse_str(obj['games']).lower().replace(' ','_'))
                row.append(parse_int(obj['year']))
                row.append(parse_str(obj['season']).lower())
                row.append(parse_str(obj['city']).lower())
                row.append(parse_str(obj['sport']).lower())
                row.append(parse_str(obj['event']).lower())
                row.append(parse_str(obj['medal']).lower())
                row.append(medal_value(obj['medal']))
                rows.append(row)

    with open(outfile, 'w') as f:
        for row in rows:
            line = PARSED_CSV_FIELD_DELIM.join(row)
            #print(line)
            f.write(line)
            f.write("\n")
        print('file written: {}  count: {}'.format(outfile, len(rows)))

def parse_countries_csv_to_json():
    infile = RAW_COUNTRIES
    with open(infile, 'rt') as csvfile:
        rdr = csv.DictReader(csvfile)
        for idx, obj in enumerate(rdr):
            j = obj_to_mongoimport_json(obj)
            print(j)

def identify_unique_games_to_json():
    infile = PARSED_ATHLETTE_EVENTS
    unique_games = dict()
    with open(infile, 'rt') as csvfile:
        rdr = csv.DictReader(csvfile, delimiter='|')
        for idx, obj in enumerate(rdr):
            game = dict()
            game['games'] = obj['games']
            game['city'] = obj['city']
            key = obj['games']
            unique_games[key] = game

    games_keys = sorted(unique_games.keys())
    for key in games_keys:
        game = unique_games[key]
        j = obj_to_mongoimport_json(game)
        print(j)

def generate_games_script_commands():
    infile = PARSED_ATHLETTE_EVENTS
    unique_games = dict()
    with open(infile, 'rt') as csvfile:
        rdr = csv.DictReader(csvfile, delimiter='|')
        for idx, obj in enumerate(rdr):
            key = obj['games']
            unique_games[key] = 1

    games_keys = sorted(unique_games.keys())
    for game in games_keys:
        cmd  = 'python main.py parse_athlete_events_csv_to_json {} > olympics/import_json/g{}.json'
        print('')
        print("echo 'parsing game {}'".format(game))
        print(cmd.format(game, game))

def generate_games_import_commands():
    infile = PARSED_ATHLETTE_EVENTS
    unique_games = dict()
    with open(infile, 'rt') as csvfile:
        rdr = csv.DictReader(csvfile, delimiter='|')
        for idx, obj in enumerate(rdr):
            key = obj['games']
            unique_games[key] = 1

    games_keys = sorted(unique_games.keys())
    for game in games_keys:
        print('')
        print("echo 'importing game g{}'".format(game))
        print("mongoimport --db olympics \\")
        print("    --collection g{} \\".format(game))
        print("    --file olympics/import_json/{}.json \\".format(game))
        print("    --numInsertionWorkers 1 \\")
        print("    --batchSize 24")
        print('sleep 3')

def generate_mongo_init_commands():
    infile = PARSED_ATHLETTE_EVENTS
    unique_games = dict()
    with open(infile, 'rt') as csvfile:
        rdr = csv.DictReader(csvfile, delimiter='|')
        for idx, obj in enumerate(rdr):
            key = obj['games']
            unique_games[key] = 1

    print('')
    print('// generated by: main.py generate_mongo_init_commands()')
    print('')
    games_keys = sorted(unique_games.keys())

    print('')
    for game in games_keys:
        print('db.g{}.drop()'.format(game))

    print('')
    for game in games_keys:
        print('db.createCollection("g{}")'.format(game))
        # print('db.g{}.ensureIndex(<"name" : 1>, <"unique" : false>)'.format(game).replace('<','{').replace('>','}'))
        # print('db.g{}.ensureIndex(<"noc" : 1>, <"unique" : false>)'.format(game).replace('<','{').replace('>','}'))
        # print('db.g{}.ensureIndex(<"event" : 1>, <"unique" : false>)'.format(game).replace('<','{').replace('>','}'))

    print('')
    for game in games_keys:
        print('db.g{}.count()'.format(game))

def parse_athlete_events_csv_to_json(game):
    infile = PARSED_ATHLETTE_EVENTS
    with open(infile, 'rt') as csvfile:
        rdr = csv.DictReader(csvfile, delimiter='|')
        for idx, obj in enumerate(rdr):
            if game == obj['games']:
                j = obj_to_mongoimport_json(obj)
                print(j)

def parse_openflights_data(name):
    infile = '../openflights/raw/{}.dat'.format(name)
    row_count = 0
    with open(infile, 'rt') as csvfile:
        rdr = csv.DictReader(csvfile)
        for idx, obj in enumerate(rdr):
            row_count = row_count + 1
            j = obj_to_mongoimport_json(obj)
            print(j)

def obj_to_mongoimport_json(obj):
    # example: {"_id":{"$oid":"5cb21be890d09ce938a7b3b7"},"name":"Putnam County Airport","city":"Greencastle","country":"United States","iata_code":"4I7","latitude":"39.6335556","longitude":"-86.8138056","altitude":"842","timezone_num":"-5","timezone_code":"America/New_York","location":{"type":"Point","coordinates":[-86.8138056,39.6335556]}}
    id = uuid.uuid4()
    return json.dumps(obj, separators=(',', ':'))

def parse_int(s):
    try:
        return str(int(s.strip()))
    except:
        return '-1'

def parse_float(s):
    try:
        return str(float(s.strip()))
    except:
        return '-1'

def parse_str(s):
    try:
        s1 = s.strip()
        if s1 == 'NA':
            s1 = ''
        s1 = s1.replace('"',"")
        s1 = s1.replace("'","")
        s1 = s1.replace(",","")
        s1 = s1.replace("|","")
        return s1
    except:
        return '?'

def medal_value(s):
    # gold, silver, bron
    try:
        s1 = s.strip().lower()
        if s1.startswith('g'):
            return '3'
        if s1.startswith('s'):
            return '2'
        if s1.startswith('b'):
            return '1'
        return '0'
    except:
        return '-1'

def load_json_file(infile):
    with open(infile) as json_file:
        return json.load(json_file)

def write_obj_as_json_file(outfile, obj):
    txt = json.dumps(obj, sort_keys=False, indent=2)
    with open(outfile, 'wt') as f:
        f.write(txt)
    print("file written: " + outfile)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        func = sys.argv[1].lower()

        if func == 'parse_raw_athlete_events_to_csv':
            parse_raw_athlete_events_to_csv()
        elif func == 'identify_unique_games_to_json':
            identify_unique_games_to_json()
        elif func == 'parse_countries_csv_to_json':
            parse_countries_csv_to_json()
        elif func == 'generate_games_script_commands':
            generate_games_script_commands()
        elif func == 'generate_games_import_commands':
            generate_games_import_commands()
        elif func == 'generate_mongo_init_commands':
            generate_mongo_init_commands()
        elif func == 'parse_athlete_events_csv_to_json':
            game = sys.argv[2]
            parse_athlete_events_csv_to_json(game)
        elif func == 'parse_openflights_data':
            name = sys.argv[2]
            parse_openflights_data(name)
        else:
            print_options('Error: invalid function: {}'.format(func))
    else:
        print_options('Error: no function argument provided.')
