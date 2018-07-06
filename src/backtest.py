

import sys








usercode =  str(sys.argv[1]) #Eventually needs to be a file name and read file here instead of in view as well 
#as well as list of parameters for tick interval and date range
code = compile(usercode, '<string>', 'exec')
#code = compile_restricted(usercode, '<string>', 'exec')


##FUNCTION HERE
# Create new backtest instance
# Get all tick data per selected tick and time range from parameters passed to us
# Loop through each object, assigning values to the "STORAGE" object and running the user's code against it.
# Create a new instance of "backtest"
STATIC_PLATFORMVERSION = '0.2.1a'


class storageObject(dict):
	pass

class dataObject(dict):
	pass

storage = storageObject()
data = dataObject()
data.high = 405.92

def log(logtext):
	print logtext



exec(code) #in restricted_globals


#BEGIN LOOP
tick()




#output results of user code (buy/Sell/plot/etc) to a "BackTestLog" instance that has reference to "backtest" instance
#END LOOP

