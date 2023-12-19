import sys
import time

configfile = sys.argv[1]

cfg_context = {}
code = open(configfile).read()
exec(code, cfg_context)

sensorfiles = cfg_context['SENSORFILES']

while True:
    for f in sensorfiles:
        tempstr = open(f).read()
        print(int(tempstr)/1000)
    time.sleep(1)
