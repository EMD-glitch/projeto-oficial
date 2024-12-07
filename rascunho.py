contatos = []

def cadastrar_contato():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)
    print("Contato cadastrado com sucesso!")

def listar_contatos():
    if not contatos:
        print("Não há contatos cadastrados.")
    else:
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

def buscar_contato(nome):
    for contato in contatos:
        if contato['nome'] == nome:
            print(f"Contato encontrado: {contato}")
            return
    print("Contato não encontrado.")

def excluir_contato(nome):
    for i, contato in enumerate(contatos):
        if contato['nome'] == nome:
            del contatos[i]
            print("Contato excluído com sucesso!")
            return
    print("Contato não encontrado.")

while True:
    print("\nEscolha uma opção:")
    print("1. Cadastrar contato")
    print("2. Listar contatos")
    print("3. Buscar contato")
    print("4. Excluir contato")
    print("5. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == '1':
        cadastrar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        nome = input("Digite o nome do contato: ")
        buscar_contato(nome)
    elif opcao == '4':
        nome = input("Digite o nome do contato a excluir: ")
        excluir_contato(nome)
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")