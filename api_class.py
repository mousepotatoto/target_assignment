import requests
import json
import re
import api_constants
import datetime


class NextBus(object):

	def __init__(self):
		pass

	#This method calls /NexTrip/Routes and return Route Id which is the route code for the given bus route string
	#http://svc.metrotransit.org/NexTrip/Routes?format=json
	def get_route(self, bus_route):
		api_url = '{}NexTrip/Routes?format=json'.format(api_constants.ENDPOINT)
		response = requests.get(url=api_url)
		data = json.loads(response.text)
		route = str('')
		#Returns a list of Transit routes that are in service on the current day.
		for i in range(0, len(data)):
		  regex = re.match(r'^\d+\s-\s(\w.+)$', data[i]['Description'])
		  if regex is not None and regex.groups()[0] == bus_route:
			  route = data[i]['Route']
		if (len(route) == 0):
		  print('No route found!')
		  exit()
		return route

	# verifies the direction and if found matched direction return the valid ID
	def get_direction(self, direction):
		dir = [value for key, value in api_constants.DIRECTIONS.items() if direction.lower() in  key]
		if not dir: # exit if not 1 = South, 2 = East, 3 = West, 4 = North
		  print('You have entered an invalid direction')
		  exit()
		return dir[0]

    #Returns a list of Timepoint stops for the given Route/Direction.
	def get_stop(self, bus_stop, bus_route, direction):
		api_url = '{}NexTrip/Stops/{}/{}?format=json'.format(api_constants.ENDPOINT, bus_route, direction)
		resp = requests.get(url=api_url)
		data = json.loads(resp.text)
		stop = [data[i]['Value'] for i in range(len(data)) if (bus_stop == data[i]['Text'] or bus_stop == data[i]['Value'])]
		if (len(stop) == 0):
		  print('No buses found for this direction')
		  exit()
		return stop[0]

	# Returns the scheduled departures for a selected route, direction and timepoint stop.
	def get_nex_trip(self, bus_route, direction, bus_stop):
		url = '{}NexTrip/{}/{}/{}?format=json'.format(api_constants.ENDPOINT, bus_route, direction, bus_stop)
		resp = requests.get(url=url)
		data = json.loads(resp.text)
		dept_time = data[0]['DepartureTime']
		return dept_time

    #datetime value of the departure time.
	def parse_time(self, time):
		timestamp = int(re.search(r'(\d+)', time).group())
		bus_time = datetime.datetime.fromtimestamp(timestamp / 1000)
		now = datetime.datetime.now()
		minutes = str(bus_time - now).split(":")[1] # get the minutes from the timestamps
		return minutes
