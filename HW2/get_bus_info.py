import urllib2
import json
import csv
import sys


if __name__=='__main__':
	API_KEY = sys.argv[1]
	BUS_LINE = sys.argv[2]
	CSV_FILE = sys.argv[3] 
	url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=" + API_KEY + "&LineRef=" + BUS_LINE

	data = json.load(urllib2.urlopen(url))
	#jsonFile = open("/Users/Nate/Documents/CUSP/HW2/Q60.json", 'r') #- for local test.
	#data = json.load(jsonFile) #- local testing

	buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	
	latitude = []
	longitude = []
	stopName = []
	stopStatus = []

	for i in range(len(buses)):
		lat = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		latitude.append(lat)
		lng = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		longitude.append(lng)
		stp_nm = buses[i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
		if stp_nm == "":
			stp_stts = "N/A"
		stopName.append(stp_nm)
		stp_stts = buses[i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
		if stp_stts == "":
			stp_stts = "N/A"
		stopStatus.append(stp_stts)

	with open(CSV_FILE, 'wb') as csvFile: #writes lat, long, stop name, and status to csv
		writer = csv.writer(csvFile)
		headers = ['Latitude', 'Longitude', 'Stop Name' , 'Stop Status']
		writer.writerow(headers)

		for num in range(len(latitude)):
			writer.writerow([latitude[num],longitude[num],stopName[num],stopStatus[num]])

