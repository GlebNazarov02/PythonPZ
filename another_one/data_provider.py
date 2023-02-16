from random import randint

def get_temperature(sensor):
    return randint(-23,0) if sensor else randint(0,21)

def get_preassure(sensor):
    return randint(700,740) if sensor else randint(740,760)

def get_windspeed(sensor):
    return randint(5,10) if sensor == 1 else randint(0,5)

def data_collection(sensor = 1):
    return (get_temperature(sensor), get_preassure(sensor), get_windspeed(sensor))