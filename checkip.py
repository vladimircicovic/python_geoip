import sys
from geoip import geolite2


if len(sys.argv) < 2:
    print("missing file with ip")
    exit(0)

filepath = sys.argv[1]

with open(filepath) as fp:
   line = "something"

   while line:
       line = fp.readline().strip()

       if not line:
            break

       match = geolite2.lookup(line)

       print(line + " " + match.country + " " + match.continent + " " + match.timezone + " " + str(match.location[0]) + " " + str(match.location[1]))

fp.close()

