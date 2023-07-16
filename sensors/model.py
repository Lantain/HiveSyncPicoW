import config

def build_sensors_payload(sensors):
    merged = dict()
    for sensor in sensors:
        v = sensor.values()
        if v is not None:
            merged.update(v)
            if config.DEBUG is True:
                sensor.log()
    return merged