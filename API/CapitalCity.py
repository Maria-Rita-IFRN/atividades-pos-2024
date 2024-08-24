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

xml_data = get_api_data("CapitalCity", "NZ")
print("CapitalCity Function Result:")
print(parse_xml(xml_data))


xml_data = get_api_data("CountryName", "NZ")
print("\nCountryName Function Result:")
print(parse_xml(xml_data))

xml_data = get_api_data("CurrencyName", "NZ")
print("\nCurrencyName Function Result:")
print(parse_xml(xml_data))

xml_data = get_api_data("LanguageName", "NZ")
print("\nLanguageName Function Result:")
print(parse_xml(xml_data))
