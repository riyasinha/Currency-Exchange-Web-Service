#Akash Sharma 2016222
#Riya Sinha 2016079
import urllib.request
def currency_response(currency_from,currency_to,amount_from):
	url1="http://cs1110.cs.cornell.edu/2015fa/a1server.php?"
	url2="from="+currency_from+"&to="+currency_to+"&amt="+str(amount_from)
	data = urllib.request.urlopen(url1+url2)
	string = data.read().decode('utf8')
	return string

def has_error(s):
	valueindex = s.find('valid')
	if s[valueindex+9:valueindex+13] == 'true':
		return False
	else:
		return True

def before_space(a):
	a1 = a.find(' ')
	return float(s[:a1])
	
def after_space(a):
	a2 = a.find(' ')
	return a[a2+1:]
def exchange(currency_from,currency_to,amount_from):
	s = currency_response(currency_from,currency_to,amount_from)
	value=has_error(s)
	if (value):
		return -1
	else:
		string1 = s.find('rhs')
		string2 = s.find('"',string1+8)
		string3 = s[string1+8:string2]
		string4 = string3.find(' ')
		string5 = string3[:string4]
		return string5

#print(has_error("OMR","PKR",7.9))