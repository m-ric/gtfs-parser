# gtfs-parser

GTFS-parser is a simple python3 script which
* reads GTFS files from folder given as argument,
* finds the route_id passing by the station whose name is given as argument.

Note: GTFS files are expected to be compliant CSV files with `.txt` extension.
Example:

```
$ GTFSParser.py ~/GTFS/Montreal "Grand Central"

GTFS files: {'agency': 'agency.txt', 'routes': 'routes.txt', 'trips': 'trips.txt', 'stop_times': 'stop_times.txt', 'stops': 'stops.txt', 'calendar': 'calendar.txt', 'calendar_dates': 'calendar_dates.txt', 'fare_attributes': 'fare_attributes.txt', 'fare_rules': 'fare_rules.txt', 'shapes': 'shapes.txt', 'frequencies': 'frequencies.txt', 'feed_info': 'feed_info.txt'}
input files: {'agency': '../GTFS/agency.txt', 'routes': '../GTFS/routes.txt', 'trips': '../GTFS/trips.txt', 'stop_times': '../GTFS/stop_times.txt', 'stops': '../GTFS/stops.txt', 'calendar': '../GTFS/calendar.txt', 'calendar_dates': '../GTFS/calendar_dates.txt', 'shapes': '../GTFS/shapes.txt'}
querying routes passing by stop: Grand Central...
df_stops_filt: 9
df_stops_join:  len:5464 idx:stop_id
df_trips_join:  len:5464 idx:stop_id
df_routes_join: len:5464 idx:stop_id
route_ids: ['2' '4' '5' '6' '6X' '7' '7X' 'GS']
```
