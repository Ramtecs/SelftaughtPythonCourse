author_ = 'Ramses Murillo'
'''/import datetime library
import datetime
Print("Creation date is: ", datetime.datetime.now())
'''
import datetime

todaysdate = datetime.datetime.now()
print("File run", todaysdate)




#1. Create a list of tuples, with each tuple containing the longitude and latitude of somewhere you've lived or visited.
WhereIlived ={"San jose":"Costa Rica","Vancouver, WA": "USA"}

Location1=["San Jose, Costa Rica","9.928069, -84.090729"]
Location2=["Bellingham, Washington","48.754902, -122.478119"]

Locations=["9.928069, -84.090729","48.754902, -122.478119"]
print("I have lived in ",Location1[0],"with coordinates: ",Locations[0])
print("I have lived in ",Location2[0],"with coordinates: ",Locations[1])

'''
results:
File run 2019-07-30 22:19:38.219695
I have lived in  San Jose, Costa Rica with coordinates:  9.928069, -84.090729
I have lived in  Bellingham, Washington with coordinates:  48.754902, -122.478119
'''
