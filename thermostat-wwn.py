from datetime import datetime
try:
    from config import *
except:
    print("ERROR: you haven't copied config-default.py to config.py and setup your identity")
    raise

import nest

access_token_cache_file = 'nest.json'

napi = nest.Nest(client_id=nest_id, client_secret=nest_secret, access_token_cache_file=access_token_cache_file)


# if napi.authorization_required:
#     print('Go to ' + napi.authorize_url + ' to authorize, then enter PIN below')
#     pin = input("PIN: ")
#     napi.request_token(pin)


def get_temperature():
    for device in napi.thermostats:
        temp = device.temperature
        return temp


def get_temp_scale():
    for device in napi.thermostats:
        scale = device.temperature_scale
        return scale


def get_date_time():
    # d = date.today()
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return dt


def get_target_temp():
    for device in napi.thermostats:
        target_temp = device.target
        return target_temp


def get_hvac_state():
    for device in napi.thermostats:
        hvac_state = device.hvac_state
        return hvac_state


def get_is_fan_timer_active():
    for device in napi.thermostats:
        is_fan_timer_active = device.fan
        return is_fan_timer_active


# def get_json_data():
#     for structure in napi.structures:
#         print ('Structure: %s' % structure.name)
#         print ('    Away: %s' % structure.away)
#         val = (structure.time_zone)
#
#     for device in structure.thermostats:
#         print ('        Device: %s' % device.name)
#         print ('            Temp: %0.1f' % device.temperature)
#         print ('            Humidity: %s' % device.humidity)
#         print ('            Has_Fan: %s' % device.has_fan)
#         print ('            Is_Using_Emergency_Heat:%s' % device.is_using_emergency_heat)
#         print ('            Temp_Scale:%s' % device.temperature_scale)
#         print ('            hvac_state:%s' % device.hvac_state)
#         print ('            can_cool:%s' % device.can_cool)
#
#     # Access advanced structure properties:
#     for structure in napi.structures:
#         print ('Structure   : %s' % structure.name)
#         print (' Postal Code                    : %s' % structure.postal_code)
#         print (' Country                        : %s' % structure.country_code)
#         print (' num_thermostats                : %s' % structure.num_thermostats)
#
#         return val


def get_thermostat_data():
    '''
    with open('thermostat_data.csv', "a") as csvfile:
        write_file = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        write_file.writerow([" Temperature", "Date and Time", "HVAC State", "Target Temperature", "Is Fan Timer Active"])

        while(True):
            write_file.writerow([str(get_temperature())+get_temp_scale(), get_date_time(), get_hvac_state(), str(get_target_temp())+get_temp_scale(), get_is_fan_timer_active()])
            print "Writing to the File"
            time.sleep(60)
            print "*" * 20
    '''
    print("Temp: ", str(get_temperature())+get_temp_scale())
    print("Time: ", get_date_time())
    print("hvac state: ", get_hvac_state())
    print("target temp: ", str(get_target_temp())+get_temp_scale())
    print("is fan active: ", get_is_fan_timer_active())

get_thermostat_data()
