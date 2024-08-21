import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def listar_usuarios():
    response = requests.get(f"{BASE_URL}/users")
    users = response.json()
    for user in users:
        print(f"ID: {user['id']}, Nome: {user['name']}, Email: {user['email']}")

def listar_tarefas_usuario(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}/todos")
    todos = response.json()
    if todos:
        for todo in todos:
            print(f"Título: {todo['title']}, Concluído: {todo['completed']}")
    else:
        print(f"Nenhuma tarefa encontrada para o usuário com ID {user_id}")

def criar_usuario():
    dados_usuario = {
        "name": input("Nome: "),
        "username": input("Nome de usuário: "),
        "email": input("Email: "),
        "address": {
            "street": input("Rua: "),
            "suite": input("Complemento: "),
            "city": input("Cidade: "),
            "zipcode": input("CEP: "),
        },
        "phone": input("Telefone: "),
        "website": input("Website: "),
        "company": {
            "name": input("Nome da empresa: "),
        }
    }
    response = requests.post(f"{BASE_URL}/users", json=dados_usuario)
    print(f"Usuário criado com ID: {response.json()['id']}")

def ler_usuario(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        user = response.json()
        print(f"Nome: {user['name']}, Email: {user['email']}")
    else:
        print(f"Usuário com ID {user_id} não encontrado.")

def atualizar_usuario(user_id):
    dados_usuario = {
        "name": input("Nome: "),
        "username": input("Nome de usuário: "),
        "email": input("Email: "),
        "address": {
            "street": input("Rua: "),
            "suite": input("Complemento: "),
            "city": input("Cidade: "),
            "zipcode": input("CEP: "),
        },
        "phone": input("Telefone: "),
        "website": input("Website: "),
        "company": {
            "name": input("Nome da empresa: "),
        }
    }
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=dados_usuario)
    print(f"Usuário com ID {user_id} atualizado")

def deletar_usuario(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        print(f"Usuário com ID {user_id} deletado")
    else:
        print(f"Usuário com ID {user_id} não encontrado.")

def main():
    while True:
        print("\nOpções:")
        print("1. Listar todos os usuários")
        print("2. Listar tarefas de um usuário específico")
        print("3. Criar um novo usuário")
        print("4. Ler um usuário por ID")
        print("5. Atualizar um usuário por ID")
        print("6. Deletar um usuário por ID")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_usuarios()
        elif escolha == "2":
            user_id = input("Digite o ID do usuário: ")
            listar_tarefas_usuario(user_id)
        elif escolha == "3":
            criar_usuario()
        elif escolha == "4":
            user_id = input("Digite o ID do usuário: ")
            ler_usuario(user_id)
        elif escolha == "5":
            user_id = input("Digite o ID do usuário: ")
            atualizar_usuario(user_id)
        elif escolha == "6":
            user_id = input("Digite o ID do usuário: ")
            deletar_usuario(user_id)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
