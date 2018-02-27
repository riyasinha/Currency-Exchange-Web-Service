#Akash Sharma 2016222
#Riya Sinha 2016079
import unittest
from urllib.request import urlopen
from a1 import *

class testa1(unittest.TestCase):

		"""Testing the currency_response """
		def testcurrency_response(self):	
			self.assertEqual(currency_response("USD","INR",2.5), '{ "lhs" : "2.5 United States Dollars", "rhs" : "166.773675 Indian Rupees", "valid" : true, "error" : "" }')
			self.assertEqual(currency_response("USD","BTC",7.6), '{ "lhs" : "7.6 United States Dollars", "rhs" : "0.013248986102 Bitcoins", "valid" : true, "error" : "" }')
			self.assertEqual(currency_response("MTL","CHF",8.3), '{ "lhs" : "8.3 Maltese Liri", "rhs" : "11.900181245813 Swiss Francs", "valid" : true, "error" : "" }')
			self.assertEqual(currency_response("BBD","QAR",4.1), '{ "lhs" : "4.1 Barbadian Dollars", "rhs" : "7.4646814 Qatari Rials", "valid" : true, "error" : "" }')
			self.assertEqual(currency_response("OMR","PKR",7.9), '{ "lhs" : "7.9 Omani Rials", "rhs" : "2141.9510843223 Pakistani Rupees", "valid" : true, "error" : "" }')

		def testhas_error(self):
			self.assertEqual(has_error('{ "lhs" : "100 United States Dollars", "rhs" : "6670.947 Indian Rupees", "valid" : true, "error" : "" }'),False)	
			self.assertEqual(has_error('{ "lhs" : "205 Bahraini Dinar", "rhs" : "717.99330620085 Australian Dollars", "valid" : true, "error" : "" }'),False)
			self.assertEqual(has_error('{ "lhs" : "848 Liberian Dollars", "rhs" : "1350.31152219166 Sri Lankan Rupees", "valid" : false, "error" : "" }'),True)
			self.assertEqual(has_error('{ "lhs" : "785 Russian Rubles", "rhs" : "45.113553435144 Saudi Riyals", "valid" : true, "error" : "" }'),False)
			self.assertEqual(has_error('{ "lhs" : "236 South African Rand", "rhs" : "131445.64624509 Laotian Kip", "valid" : false, "error" : "" }'),True)
		def testexchange(self):
			self.assertEqual(exchange("USD","INR",100),"6670.947")
			self.assertEqual(exchange("BHD","AUD",205),"717.99330620085")
			self.assertEqual(exchange("LRD","LKR",848),"1350.3115221918")
			self.assertEqual(exchange("RUB","SAR",785),"45.113553435144")
			self.assertEqual(exchange("ZAR","LAK",236),"131445.64621209")

if __name__ == '__main__':
	unittest.main()