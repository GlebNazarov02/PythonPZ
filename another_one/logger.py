from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{};temperature;{}\n'
                    .format(time,data))

def preassure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{};preassute;{}\n'
                    .format(time,data))

def windspeed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv','a') as file:
        file.write('{};windspeed;{}\n'
                    .format(time,data))