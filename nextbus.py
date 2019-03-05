import sys
from api_class import NextBus

def main():
	next_bus = NextBus()
	bus_route = next_bus.get_route(sys.argv[1])
	direction = next_bus.get_direction(sys.argv[3])
	bus_stop = next_bus.get_stop(sys.argv[2], bus_route, direction)
	get_nex_trip = next_bus.get_nex_trip(bus_route, direction, bus_stop)
	mins = next_bus.parse_time(get_nex_trip)

	if (int(mins) >= 1):
	    print('The next bus leaves in ' + mins + ' minute')
	else:
		print('No busses found at this time')


if __name__ == '__main__':
    main()


#python3.7 nextbus.py 'A Line Roseville-St Paul-Minneapolis' 'Rosedale Transit Center' 'south'
