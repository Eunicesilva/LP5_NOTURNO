from datetime import datetime

def validar_nome(nome):
    nome = nome.strip()
    if len(nome) < 2:
        raise ValueError("O nome deve ter pelo menos 2 caracteres.")
    return nome

def validar_email(email):
    email = email.strip()
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("E-mail inválido.")
    return email

def validar_data_nascimento(data):
    data = data.strip()
    try:
        data_obj = datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida. Use o formato DD/MM/AAAA.")
    return data_obj.strftime("%d/%m/%Y")