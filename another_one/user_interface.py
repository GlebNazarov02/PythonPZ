import data_provider as prov
import logger as log

def temperature_view(sensor):
    data = prov.get_temperature(sensor)
    log.temperature_logger(data)
    return(data)

def pressure_view(sensor):
    data = prov.get_preassure(sensor)
    log.preassure_logger(data)
    return(data)

def windspeed_view(sensor):
    data = prov.get_windspeed(sensor)
    log.windspeed_logger(data)
    return(data)