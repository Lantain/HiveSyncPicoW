import urequests
import ujson
import config

def send_record(payload):
        url = f"{config.HIVESYNC_HOST}/sensors/{config.SENSOR_ID}/records"
        headers = {'content-type': 'application/json'}
        data = ujson.dumps(payload)
        response = urequests.post(url, headers =headers, data=data).json()
        print(response)