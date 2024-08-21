import users_wrapper as users

def main():
    while True:
        print("\nOpções:")
        print("1. Listar todos os usuários")
        print("2. Criar um novo usuário")
        print("3. Ler um usuário por ID")
        print("4. Atualizar um usuário por ID")
        print("5. Deletar um usuário por ID")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            users_list = users.list_users()
            for user in users_list:
                print(f"ID: {user['id']}, Nome: {user['name']}, Email: {user['email']}")

        elif opcao == "2":
            nome = input("Nome: ")
            username = input("Username: ")
            email = input("Email: ")
            novo_usuario = users.create_user({"name": nome, "username": username, "email": email})
            print(f"Usuário criado com sucesso: ID {novo_usuario['id']}")

        elif opcao == "3":
            user_id = int(input("Digite o ID do usuário: "))
            user = users.read_user(user_id)
            if user:
                print(f"ID: {user['id']}, Nome: {user['name']}, Email: {user['email']}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            user_id = int(input("Digite o ID do usuário que deseja atualizar: "))
            nome = input("Nome: ")
            username = input("Username: ")
            email = input("Email: ")
            usuario_atualizado = users.update_user(user_id, {"name": nome, "username": username, "email": email})
            print(f"Usuário atualizado: Nome: {usuario_atualizado['name']}, Email: {usuario_atualizado['email']}")

        elif opcao == "5":
            delete_user_id = int(input("Digite o ID do usuário que deseja deletar: ")) 
            if users.delete_user(delete_user_id):
                print(f"Usuário {delete_user_id} deletado com sucesso.")
            else:
                print(f"Erro ao tentar deletar o usuário {delete_user_id}.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
