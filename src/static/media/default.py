# EXAMPLE SCRIPT DEMONSTRATING FEATURES AS THEY ARE DEVELOPED

# Edit text file

# Read backend defined STATIC constants

versionStr = 'Platform Version', STATIC_PLATFORMVERSION



# Use "Log" Function in place of traditional builtin "Print Command"

log(versionStr)



#save and retrieve data in "persistent" storage variable

storage.mycustomvalue = "This platform is in Alpha stage."

log(storage.mycustomvalue)



log("----------------------")



#Access trade data from "data" variable

todaysHigh = "Today's High", data.high

log(todaysHigh)









# Define and use "Tick" function, runs for every interval in the selected backtest timeframe.

def tick():

    log("output from within the tick")