bike-data-querify
=================

Python interface to query data from bike-data-collector

q1 -> Query 1
Returns a matrix with the bike station ocupation for a set of E stations between t1 and t2

Call example:

python main.py q1 [Hashed array of stations] [timestamp t1 YYYYMMDDHHMM] [timestamp t2 YYYYMMDDHHMM] [bike system]

To hash array of stations:
echo '1,23,27,113,214,335' | gzip -cf| base64
> H4sIAIKUrVEAAzPUMTLWMTLXMTQEUoYmOsbGplwA/BpnLBQAAAA=

python main.py q1 H4sIAIKUrVEAAzPUMTLWMTLXMTQEUoYmOsbGplwA/BpnLBQAAAA= 201306010000 2013060300 bicing

Output example:
id=1 20 21 21 21 21 20
id=113 18 18 18 18 20 18
id=214 23 23 23 23 23 24
id=23 22 23 23 27 27 27
id=27 17 17 17 16 14 13
id=335 17 17 17 20 22 23



