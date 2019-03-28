import time
from threading import Thread
import json
import requests
from methods import Methods

class Bot:
    token = None
    baseUrl = "https://api.telegram.org/bot{}/{}"
    update_id = None
    threadCount = None
    main = None
    updates = None

    def __init__(self, token, threadCount=100):
        self.Token = token
        self.threadCount = threadCount

    def Methods(self):
        return Methods(self.token)

    def run(self, main):
        self.main = main
        while 1:
            if self.update_id is None:
                self.updates = self._sendRequest(self._urlMethod('getUpdates'), {})
                if self.updates is not None:
                    if len(self.updates) >= self.threadCount:
                        self._createThreadUpdate(self.threadCount)
                    else:
                        self._createThreadUpdate(len(self.updates))
                else:
                    time.sleep(1)
            else:
                self.updates = self._sendRequest(self._urlMethod('getUpdates'), {'offset': self.update_id})
                if self.updates is not None:
                    if len(self.updates) >= 100:
                        self._createThreadUpdate(self.threadCount)
                    else:
                        self._createThreadUpdate(len(self.updates))

                else:
                    time.sleep(1)

    def _createThreadUpdate(self, count):
        t = []
        for i in range(0, count):
            t.append(createThread(i, "{}".format(i), self.updates[i], self.main))
        for i in range(0, count):
            self.update_id = int(self.updates[i]['update_id']) + 1
            t[i].start()

    def _sendRequest(self, url, data=None):
        res = requests.post(url, params=data)
        data = json.loads(res.content.decode('utf-8'))
        try:
            return data['result']
        except:
            return None

    def _urlMethod(self, method):
        return self.baseUrl.format(self.Token, method)

class createThread(Thread):
    def __init__(self, threadID, name, update, main):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.update = update
        self.main = main

    def run(self):
        self.main(self.update)
