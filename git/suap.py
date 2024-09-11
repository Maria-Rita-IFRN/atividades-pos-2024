import requests
import json
import os
from getpass import getpass

base_url = "https://suap.ifrn.edu.br/api/"

def solicitar_credenciais():
    username = input("Informe seu login no SUAP: ")
    secret_key = getpass("Informe sua senha: ")
    return username, secret_key

def gerar_token_autenticacao(base_url, username, secret_key):
    payload = {"username": username, "password": secret_key}
    auth_endpoint = base_url + "v2/autenticacao/token/"
    response = requests.post(auth_endpoint, json=payload)
    
    if response.status_code == 200:
        return response.json().get("access")
    else:
        print(f"Erro na autenticação: {response.status_code}")
        print("Detalhes:", response.json())
        return None

def consultar_boletim(base_url, auth_token, academic_year):
    headers = {"Authorization": f'Bearer {auth_token}'}
    boletim_endpoint = f"{base_url}v2/minhas-informacoes/boletim/{academic_year}/1"
    response = requests.get(boletim_endpoint, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao consultar o boletim: {response.status_code}")
        print("Detalhes:", response.json())
        return None

def mostrar_boletim(boletim_dados):
    print(f"{'Disciplina':<35}{'Média Final':<15}")
    print("-" * 50)
    
    for subject in boletim_dados:
        subject_name = subject.get('disciplina', 'Informação indisponível')
        final_grade = subject.get('media_disciplina', 'N/D')
        final_grade_str = str(final_grade) if final_grade is not None else 'N/D'
        
        print(f"{subject_name:<35}{final_grade_str:<15}")

def iniciar_suap():
    if os.path.exists('credenciais.json'):
        with open('credenciais.json', 'r') as file:
            try:
                data = json.load(file)
                auth_token = data.get('auth_token')
                
                if auth_token:
                    usar_token = input("Deseja usar o token armazenado? (s/n): ").strip().lower()
                    if usar_token != 's':
                        auth_token = None
            except json.JSONDecodeError:
                auth_token = None
    else:
        auth_token = None
    
    if not auth_token:
        username, secret_key = solicitar_credenciais()
        auth_token = gerar_token_autenticacao(base_url, username, secret_key)
        if auth_token:
            with open('credenciais.json', 'w') as file:
                json.dump({"auth_token": auth_token}, file)
        else:
            print("Autenticação falhou. Por favor, verifique suas credenciais.")
            return
    
    academic_year = input("Informe o ano letivo (ex: 2024): ")
    boletim_dados = consultar_boletim(base_url, auth_token, academic_year)
    if boletim_dados:
        mostrar_boletim(boletim_dados)

if __name__ == "__main__":
    iniciar_suap()
