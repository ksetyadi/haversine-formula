import math
import urllib2, json, string
import sys

def distance(point1, point2):
	lat1, lon1, lat2, lon2 = map(math.radians, [point1[0], point1[1], point2[0], point2[1]])
	dlat = lat2 - lat1
	dlon = lon2 - lon1
	a = (math.sin(dlat/2)**2) + (math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2)
	c = 2 * math.asin(math.sqrt(a))
	km = 6371 * c
	return km
	
def get_coordinate(addr):
	url="http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % addr
	
	response = urllib2.urlopen(url)
	jsongeocode = response.read()
	
	data = json.loads(jsongeocode)
	return (data['results'][0]['geometry']['location']['lat'], data['results'][0]['geometry']['location']['lng'])

def form_address(addr):
	return string.replace(addr, " ", "+")

if __name__ == '__main__':
	args = sys.argv[1:]
	
	if len(args) != 2:
		print "You should put two (and only two) parameters as first point and second point. No more and no less."
		exit(1)
		
	addr1 = args[0]
	addr2 = args[1]

	print distance(get_coordinate(form_address(addr1)), get_coordinate(form_address(addr2))), "km"