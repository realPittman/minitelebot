import requests
import json
import time
from threading import Thread
import time
class Main():
	url = "https://api.telegram.org/bot{}/{}"
	update_id = None
	updates = None
	main = None
	threadCount = None
	def __init__(self, Token, threadCount = 100):
		self.Token = Token
		self.threadCount = threadCount
	def sendRequest(self, method, params):
		res = requests.post(self._url_method(method) ,params=params)
		data = json.loads(res.content.decode('utf-8'))
		try:
			return data['result']
		except:
			return None
	def _url_method(self, method):
		return self.url.format(self.Token,method)
	
	def _createThreadUpdate(self,count):
		t = []
		for i in range(0,count):
			t.append(updateThread(i, "{}".format(i),self.updates[i],self.main))
		for i in range(0,count):
			self.update_id = int(self.updates[i]['update_id']) + 1
			t[i].start()
	def polling(self, main):
		self.main = main
		while 1 :
			if self.update_id == None :
				self.updates = self.sendRequest('getUpdates', {})
				if self.updates != None :
					if len(self.updates) >= self.threadCount :
						self._createThreadUpdate(self.threadCount)
					else:
						self._createThreadUpdate(len(self.updates))	
				else:
					time.sleep(1)
			else:
				self.updates = self.sendRequest('getUpdates', {'offset' : self.update_id})
				if self.updates != None :
					if len(self.updates) >= 100 :
						self._createThreadUpdate(self.threadCount)
					else:
						self._createThreadUpdate(len(self.updates))
					
				else:
					time.sleep(1)
class Bot(Main):
	Methods = ['getme','getupdates','setwebhook','deletewebhook','getwebhookinfo','sendmessage','forwardmessage','sendphoto','sendaudio','senddocument','sendvideo','sendvoice','sendvideonote','sendmediagroup','sendlocation','editmessagelivelocation','stopmessagelivelocation','sendvenue','sendcontact','sendanimation','sendchataction','getuserprofilephotos','getfile','kickchatmember','unbanchatmember','restrictchatmember','promotechatmember','exportchatinvitelink','setchatphoto','deletechatphoto','setchattitle','setchatdescription','pinchatmessage','unpinchatmessage','leavechat','getchat','getchatadministrators','getchatmemberscount','getchatmember','setchatstickerset','deletechatstickerset','answercallbackquery','editmesagetext','editmesagemedia','editmesagecaption','editmesagereplymarkup','deletemesage','stickerset','sendsticker','getstickerset','uploadstickerfile','createnewstickerset','addstickertoset','setstickerpositioninset','deletestickerfromset','answerinlinequery','sendgame','setgamescore','getgamehighscores']
	def __init__(self,Token):
		self.Token = Token
		super().__init__(self.Token)
	def __getattr__(self, method):
		return self.exec_method(method)
	def exec_method(self, method):
		def methodName(*args, **kwargs):
			if method.lower() in self.Methods:
				self.sendRequest(method , args[0])
			else:
				print("Method {} undefined".format(method))
		return methodName

class updateThread(Thread):
	def __init__(self, threadID, name, update, main):
		Thread.__init__(self)			
		self.threadID = threadID
		self.name = name
		self.update = update
		self.main = main
	def run(self):
		self.main(self.update)