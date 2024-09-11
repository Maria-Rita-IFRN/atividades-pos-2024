import requests
from getpass import getpass

def autenticar_usuario():
    username = input("Digite seu nome de usuário do GitHub: ")
    token = getpass("Digite seu token de acesso: ")
    return username, {'Authorization': f'token {token}'}

def exibir_seguidores(usuario, headers):
    url = f'https://api.github.com/users/{usuario}/followers'
    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 200:
        seguidores = resposta.json()
        print(f"Seguidores de {usuario}:")
        for seguidor in seguidores:
            print(f"- {seguidor['login']}")
        print(f"Total de seguidores: {len(seguidores)}")
    else:
        print(f"Erro ao buscar seguidores: {resposta.status_code}")

def seguir_usuario(alvo, headers):
    url = f'https://api.github.com/user/following/{alvo}'
    resposta = requests.put(url, headers=headers)

    if resposta.status_code == 204:
        print(f"Agora você está seguindo {alvo}.")
    else:
        print(f"Erro ao tentar seguir {alvo}: {resposta.status_code}")

def deixar_de_seguir_usuario(alvo, headers):
    url = f'https://api.github.com/user/following/{alvo}'
    resposta = requests.delete(url, headers=headers)

    if resposta.status_code == 204:
        print(f"Você deixou de seguir {alvo}.")
    else:
        print(f"Erro ao tentar deixar de seguir {alvo}: {resposta.status_code}")

def gerenciar_acoes():
    username, headers = autenticar_usuario()

    while True:
        print("\nOpções disponíveis:")
        print("1. Listar seguidores")
        print("2. Seguir um usuário")
        print("3. Deixar de seguir um usuário")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '1':
            usuario_alvo = input("Digite o nome de usuário para listar seguidores: ")
            exibir_seguidores(usuario_alvo, headers)
        elif escolha == '2':
            usuario_alvo = input("Digite o nome de usuário para seguir: ")
            seguir_usuario(usuario_alvo, headers)
        elif escolha == '3':
            usuario_alvo = input("Digite o nome de usuário para deixar de seguir: ")
            deixar_de_seguir_usuario(usuario_alvo, headers)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    gerenciar_acoes()
