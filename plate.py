import requests
import os
from pprint import pprint


def plate_recognition():
    # os.system('fswebcam -q  capture.jpg')
    regions = ['hu', 'us-ca'] 
    with open('capture.jpg', 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=regions),
            files=dict(upload=fp),
            headers={'Authorization': 'Token 830777e03179f94991f4f24a20351e66ddaf0e5e'})
    data=response.json()
    return(data['results'][0]['plate'])
