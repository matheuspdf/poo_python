class SistemaCadastra:
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):  # 1
            print("Acessando o banco de dados...")  # 2
            print(f"Cadastrar usuário {nome}, idade {idade}")
        else:
            print("Dados inválidos.")  # 3


# 1 - Validar = responsabilidade
# 2 - Acessar banco de dados = responsabilidade
# 3 - Tratamento de erros = responsabilidade
