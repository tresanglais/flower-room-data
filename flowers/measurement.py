from datetime import datetime
import math


class Measurement(object):
    def __init__(self, temperature=math.inf, humidity=math.inf, ph=math.inf):
        self.datetime = datetime.now()
        self.temperature = float(temperature)
        self.humidity = float(humidity)
        self.ph = float(ph)
        self.doc = None

    def __repr__(self):
        return (
            f'Measurement(\
                datetime={self.datetime}, \
                temperature={self.temperature}, \
                humidity={self.humidity}, \
                ph={self.ph}, \
            )'
        )

    # create a firestore document if any measurement is found
    def create_document(self):
        if self.temperature < math.inf or self.humidity < math.inf or self.ph < math.inf:
            return {
                u'time': self.datetime,
                u'temp': self.temperature,
                u'hum': self.humidity,
                u'ph': self.ph
            }
        else:
            raise Exception('All measurements are empty, skipping upload')
