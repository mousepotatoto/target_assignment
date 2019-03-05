# target_assignment
In a language of your choice, write a program which will tell you how long it is until
the next bus on “BUS ROUTE” leaving from “BUS STOP NAME” going “DIRECTION”
using the api defined at http://svc.metrotransit.org/
“BUS ROUTE” will be a substring of the bus route name which is only in one bus
route
“BUS STOP NAME” will be a substring of the bus stop name which is only in one bus
stop on that route
“DIRECTION” will be “north” “east” “west” or “south”
Eg, if you wanted to know the next bus leaving from our Brooklyn Park campus to
our downtown campus:
$ go run nextbus.go “Express - Target - Hwy 252 and 73rd Av P&R - Mpls” “Target
North Campus Building F” “south”
2 Minutes
