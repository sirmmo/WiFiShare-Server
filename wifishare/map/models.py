from pymongo import MongoClient
from bson.code import Code

from django.conf import settings

class WiFiStore():
	def __init__(self):
		self.client = MongoClient(settings.MONGO_SETTINGS)
		self.db = self.client.wifishare
		self.data_scans = self.db.scans
		self.data_walks = self.db.walks

	def store(self, data):
		self.data_scans.insert(data)
		return

	def locate(self, ident, pattern):
		self.mapper = Code("""
				function(){
					this.scans.forEach(function(z) {
						if (z.ssid in [%s])
							emit(z, 1);
					});
				}
			""")
		self.reducer = Code("""
				function(key, values){
					var total = 0;
					return total;
				}
			""")
		result = self.data_scans.map_reduce(self.mapper, self.reducer, "wifi")

		for doc in result.find():
			print doc
		return 

	def map(self, bbox):
		return

