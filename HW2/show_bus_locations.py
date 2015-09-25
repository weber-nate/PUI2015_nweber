import urllib2
import json
import sys


if __name__=='__main__':
	API_KEY = sys.argv[1] 
	BUS_LINE =  sys.argv[2]
	url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=" + API_KEY + "&LineRef=" + BUS_LINE

	data = json.load(urllib2.urlopen(url))
	# jsonFile = open("/Users/Nate/Documents/CUSP/HW2/Q60.json", 'r')
	# data = json.load(jsonFile) #- local testing
	busCount = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'])

	buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	latitude = []
	longitude = []
	for i in range(len(buses)):
		lat = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		latitude.append(lat)
		lng = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		longitude.append(lng)

	print "Bus Line: " + BUS_LINE
	print "Number of Active Buses: " + str(len(buses))

	busNumber = 0

	for a in range(len(longitude)):
		print "Bus " + str(busNumber) + " is at latitude " + str(latitude[a]) + " and longitude " + str(longitude[a])
		busNumber += 1

	