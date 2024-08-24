import requests
from xml.dom.minidom import parseString
def get_api_data(function_name, country_code):
    url = f"http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso/{function_name}?sCountryISOCode={country_code}"
    response = requests.get(url)
    return response.content

def parse_xml(xml_data):
    dom = parseString(xml_data)
    pretty_xml = dom.toprettyxml()
    return pretty_xml

xml_data = get_api_data("CapitalCity", "NO")
print("CapitalCity Function Result:")
print(parse_xml(xml_data))

from zeep import Client
wsdl = 'http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL'
client = Client(wsdl=wsdl)
numero = 223
response = client.service.NumberToWords(numero)
print(f"O número {numero} por extenso é: {response}")


