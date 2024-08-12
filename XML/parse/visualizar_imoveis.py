import json


def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return json.load(file).get('imobiliaria', {}).get('imoveis', [])

def exibir_menu(dados_imoveis):
    while True:
        print("\nMenu de Imóveis:")
   
        for imovel in dados_imoveis:
            endereco = imovel.get('endereco', {})
            endereco_str = f"{endereco.get('rua', '')}, {endereco.get('bairro', '')}, {endereco.get('cidade', '')}, {endereco.get('numero', '')}"
            print(f"ID: {imovel.get('ID', 'ID não disponível')} - {endereco_str}")

        try:

            id_selecionado = int(input("\nDigite o ID do imóvel para mais detalhes (ou 0 para sair): "))

            if id_selecionado == 0:
                print("Saindo...")
                break


            imovel_encontrado = next((imovel for imovel in dados_imoveis if imovel.get('ID') == id_selecionado), None)
            if imovel_encontrado:
                print("\nDetalhes do Imóvel:")
                for chave, valor in imovel_encontrado.items():
                    if isinstance(valor, dict):  
                        print(f"{chave}:")
                        for sub_chave, sub_valor in valor.items():
                            print(f"  {sub_chave}: {sub_valor}")
                    elif isinstance(valor, list): 
                        print(f"{chave}:")
                        for item in valor:
                            print(f"  {item}")
                    else:
                        print(f"{chave}: {valor}")
            else:
                print("ID não encontrado. Tente novamente.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")



    
dados_imoveis = carregar_dados_json("XML\parse\imoveis.json")
exibir_menu(dados_imoveis)
