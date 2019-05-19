import time
import urllib
import base64
import hmac
import hashlib
import requests
import lxml.etree

def funcion(param):
	diccionario = ('quiero', 'deseo', 'comprar', 'adquirir', 'busco', 'necesito')
	conjunciones = ('un', 'una', 'unas', 'uno', 'unos')
	str = param
	for plbr in diccionario:
		if str.__contains__(plbr):
			str = str.replace(plbr, '')
	for plbr2 in conjunciones:
		if str.__contains__(plbr2):
			str = str.replace(plbr2, '')

	str = str.replace(' ', '%20')
	key = str

	amazon_set = []
	amazon_access_key = 'AKIAIEQUIWQKHR7L7HYA'
	amazon_secret_key = b'lcfNNnla5w7NyZVJZ0zoBcVtyyv10G2+FhQ8FK10'
	m_params = {
		'Keywords': key,
		'Operation': 'ItemSearch',
		'ResponseGroup': 'Images,ItemAttributes,Offers',
		'SearchIndex': 'All',
		'Service': 'AWSECommerceService'
	}
	region = 'es'
	params = m_params
	method = 'GET'
	host = 'webservices.amazon.' + region
	uri = '/onca/xml'
	params['Service'] = 'AWSECommerceService'
	params['AWSAccessKeyId'] = 'AKIAIEQUIWQKHR7L7HYA'
	params['Timestamp'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
	associate_tag = 'bestprix09-21'
	if associate_tag:
		params['AssociateTag'] = associate_tag
	for param in sorted(params.keys()):
		if 'canonicalized_query' in locals():
			canonicalized_query = canonicalized_query + '&' + param.replace('%7E', '~') + '=' + params[param].replace(
				'%7E', '~')
		else:
			canonicalized_query = '&' + param.replace('%7E', '~') + '=' + params[param].replace('%7E', '~')
	string_to_sign = method + '\n' + host + '\n' + uri + '\n' + canonicalized_query;
	signature = base64.b64encode(
		hmac.new(key=amazon_secret_key, msg=string_to_sign.encode(), digestmod=hashlib.sha256).digest())
	amazon_request_url = 'http://' + host + uri + '?' + canonicalized_query + '&Signature=' + signature.decode().replace(
		'+', '%2B').replace('=', '%3D')
	print(amazon_request_url)

invocacion = ('Botti', 'botti', 'boti', 'Boti')
str_saludo_inicial = "(Si quiere parar el asistente escriba 'salir') \nHola, soy Botti, tu asistente personal de compras. Para invocarme solo necesitas escribit Botti...\n>>>"

#Inicio
comp_invocacion = input(str_saludo_inicial)

encendido = False
continua = True
exit = False

i = 0

while continua:
	if(i == 0):
		frase = input(str_saludo_inicial)
	else:
		frase = input()

	if frase.__contains__('salir'):
		print("Adios.")
		continua = False
		i+1
		break
	else:
		for plbr in invocacion:
			if frase.__contains__(plbr):
				encendido = True
				frase = frase.replace(plbr, '')
				break
		if encendido:
			funcion(frase)
			i=0
			encendido = False
		if encendido == False:
			i+1
			input("Lo siento, no puedo entender tu petición. Recuerda invocarme con 'Botti'.\n>>>")







