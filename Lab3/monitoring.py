import requests
import json
import logging
from time import sleep

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logging.error('Http Error: {errh}'.format(errh=errh))
    except requests.exceptions.ConnectionError as errc:
        logging.error('Error Connecting: {errc}'.format(errc=errc))
    except Exception as err:
        logging.error('Other error: {err}'.format(err=err))
    else:
        data = json.loads(r.content)
        logging.info("Server unavailable. Server time: %s", data['date'])
        logging.info("Requested page : %s", data['current_page'])
        logging.info("Response contains:")
        for key in data.keys():
            logging.info("Key: %s, Value: %s", key, data[key])


if __name__ == '__main__':
'''
    while True:
        main("http://localhost:8000/health")
        sleep(60)
'''
