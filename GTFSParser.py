#!/usr/bin/env python3

import os
import pandas as pd
import sys


gtfs_tables = ['agency', 'routes', 'trips', 'stop_times', 'stops', 'calendar']
gtfs_tables_opt = ['calendar_dates', 'fare_attributes', 'fare_rules', 'shapes', 'frequencies', 'feed_info']

# TODO replace dummy log with logging
def log(*args, **kwargs):
    print(*args, **kwargs)


def print_columns(inputfiles):
    for inputkey, inputfile in inputfiles.items():
        log(f'parsing {inputfile}...')
        df = pd.read_csv(inputfile)

        #if {'route_id', 'route_long_name'} <= set(df):

        log('Columns:')
        for key in df.keys():
            log(f'  {key}')


def load_df(inputfiles):
    log("loading PandaFrames...")
    # four tables needs to be accessed to get route_id from station_name
    df_routes = pd.read_csv(inputfiles['routes'], index_col='route_id')
    df_trips = pd.read_csv(inputfiles['trips'], index_col='trip_id')
    df_stops = pd.read_csv(inputfiles['stops'], index_col='stop_id')
    df_stop_times = pd.read_csv(inputfiles['stop_times'], index_col='stop_id')

    return (df_routes, df_trips, df_stops, df_stop_times)


def get_route_ids(df_routes, df_trips, df_stops, df_stop_times, station_name):
    """
    Get a list of route_ids passing by the station provided (as stop_id)
    This is equivalent to SQL:

    SELECT DISTINCT routes.route_id
      FROM routes
      INNER JOIN trips ON routes.route_id = trips.route_id
      INNER JOIN stop_times ON stop_times.trip_id = trips.trip_id
      INNER JOIN stops ON stops.stop_id = stop_times.stop_id
      WHERE stops.stop_name LIKE '<station_name>%';
    
    """
    log(f'querying routes passing by stop: {station_name}...')

    # filter stops which contains the station_name keyword
    df_stops_filtered = df_stops[ df_stops.stop_name.str.contains(station_name) ]
    log(f'df_stops_filt: {len(df_stops_filtered)}')

    # join stops with stop_times
    df_stops_join = df_stops_filtered.join(df_stop_times, on='stop_id', how='inner', lsuffix='_prim', rsuffix='_fkey')
    log(f'df_stops_join:  len:{len(df_stops_join)} idx:{df_stops_join.index.name}')

    df_trips_join = df_stops_join.join(df_trips, on='trip_id', how='inner')
    log(f'df_trips_join:  len:{len(df_trips_join)} idx:{df_trips_join.index.name}')

    df_routes_join = df_trips_join.join(df_routes, on='route_id', how='inner')
    log(f'df_routes_join: len:{len(df_routes_join)} idx:{df_routes_join.index.name}')

    return df_routes_join.route_id.unique()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        log(f'{sys.argv[0]} <input-dir> <station-name>')
        sys.exit(1)

    inputdir = os.path.expanduser(sys.argv[1])
    station_name = str(sys.argv[2])

    # feed only existing files
    gtfs_files = {t: '%s.txt' % t for t in gtfs_tables + gtfs_tables_opt}
    log(f'GTFS files: {gtfs_files}')
    inputfiles = {k: os.path.join(inputdir, f) for k, f in gtfs_files.items() if f in os.listdir(inputdir)}
    log(f'input files: {inputfiles}')

    df_tuple = load_df(inputfiles)
    route_ids = get_route_ids(*df_tuple, station_name)
    log(f'route_ids: {route_ids}')
