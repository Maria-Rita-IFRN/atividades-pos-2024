from xml.dom.minidom import parse
import json 


dom = parse("imobiliaria.xml")

imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName('imovel')


def parse_imovel(imovel):
    descricao = imovel.getElementsByTagName('descricao')[0].firstChild.nodeValue
    proprietario_element = imovel.getElementsByTagName('proprietario')[0]
    nome = proprietario_element.getElementsByTagName('nome')[0].firstChild.nodeValue
    email_element = proprietario_element.getElementsByTagName('email')
    email = email_element[0].firstChild.nodeValue if email_element else None
    telefones = [telefone.firstChild.nodeValue for telefone in proprietario_element.getElementsByTagName('telefone')]
    
    endereco_element = imovel.getElementsByTagName('endereco')[0]
    rua = endereco_element.getElementsByTagName('rua')[0].firstChild.nodeValue
    bairro = endereco_element.getElementsByTagName('bairro')[0].firstChild.nodeValue
    cidade = endereco_element.getElementsByTagName('cidade')[0].firstChild.nodeValue
    numero_element = endereco_element.getElementsByTagName('numero')
    numero = numero_element[0].firstChild.nodeValue if numero_element else None
    
    caracteristicas_element = imovel.getElementsByTagName('caracteristicas')[0]
    tamanho = caracteristicas_element.getElementsByTagName('tamanho')[0].firstChild.nodeValue
    numQuartos = caracteristicas_element.getElementsByTagName('numQuartos')[0].firstChild.nodeValue
    numBanheiros = caracteristicas_element.getElementsByTagName('numBanheiros')[0].firstChild.nodeValue
    
    valor = imovel.getElementsByTagName('valor')[0].firstChild.nodeValue
    
    return {
        "descricao": descricao,
        "proprietario": {
            "nome": nome,
            "email": email,
            "telefone": telefones
        },
        "endereco": {
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "numero": numero
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": numQuartos,
            "numBanheiros": numBanheiros
        },
        "valor": valor
    }


imoveis_json = [parse_imovel(imovel) for imovel in imoveis]
json_data = {"imobiliaria": {"imovel": imoveis_json}}


with open('imobiliaria.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)


print(json.dumps(json_data, indent=4, ensure_ascii=False))