# Classe base para Carro
class Carro:
    def __init__(self, categoria, transmissao, combustivel, marca, modelo):
        self.categoria = categoria
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.marca = marca
        self.modelo = modelo

# Classe para instâncias de carros da locadora
class Veiculo(Carro):
    def __init__(self, carro_base, ano, placa):
        # Herdando atributos do carro base
        super().__init__(carro_base.categoria, carro_base.transmissao, carro_base.combustivel,
                         carro_base.marca, carro_base.modelo)
        self.ano = ano
        self.placa = placa
        self.disponivel = True  # atributo para saber se o carro está disponível

# Classe Cliente
class Cliente:
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

# Classe Locação
class Locacao:
    def __init__(self, cliente, veiculo, inicio, fim):
        self.cliente = cliente
        self.veiculo = veiculo
        self.inicio = inicio
        self.fim = fim
        self.veiculo.disponivel = False

# Sistema da Locadora
class Locadora:
    def __init__(self):
        self.carros_base = []  # carros cadastrados como base
        self.veiculos = []     # instâncias de carros disponíveis
        self.clientes = []
        self.locacoes = []

    def cadastrar_carro_base(self):
        categoria = input("Informe a categoria do carro: ")
        transmissao = input("Informe a transmissão (Automática/Manual): ")
        combustivel = input("Informe o tipo de combustível: ")
        marca = input("Informe a marca: ")
        modelo = input("Informe o modelo: ")
        carro = Carro(categoria, transmissao, combustivel, marca, modelo)
        self.carros_base.append(carro)
        print("Carro base cadastrado com sucesso!")

    def cadastrar_veiculo(self):
        if self.carros_base:
            print("Carros base disponíveis:")
            for idx, c in enumerate(self.carros_base, 1):
                print(f"{idx}) {c.categoria} - {c.marca} {c.modelo}")
            opc = input("O carro está em uma categoria já cadastrada? [S/N]: ").upper()
            if opc == "S":
                num = int(input("Escolha o número do carro base: ")) - 1
                carro_base = self.carros_base[num]
            else:
                self.cadastrar_carro_base()
                carro_base = self.carros_base[-1]
        else:
            print("Nenhum carro base encontrado. Cadastrando um novo...")
            self.cadastrar_carro_base()
            carro_base = self.carros_base[-1]

        ano = input("Informe o ano do carro: ")
        placa = input("Informe a placa do carro: ")
        veiculo = Veiculo(carro_base, ano, placa)
        self.veiculos.append(veiculo)
        print("Veículo cadastrado com sucesso!")

    def cadastrar_cliente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        rg = input("RG: ")
        cliente = Cliente(nome, cpf, rg)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")

    def realizar_locacao(self):
        disponiveis = [v for v in self.veiculos if v.disponivel]
        if not disponiveis:
            print("Nenhum veículo disponível para locação!")
            return

        print("Veículos disponíveis:")
        for idx, v in enumerate(disponiveis, 1):
            print(f"{idx}) {v.categoria} {v.marca} {v.modelo} - Placa: {v.placa}")
        escolha = int(input("Escolha o carro pelo número: ")) - 1
        veiculo = disponiveis[escolha]

        cpf = input("Informe o CPF do cliente: ")
        cliente = next((c for c in self.clientes if c.cpf == cpf), None)
        if not cliente:
            print("Cliente não encontrado! Cadastre o cliente primeiro.")
            return

        inicio = input("Data de início da locação (dd/mm/aaaa): ")
        fim = input("Data de fim da locação (dd/mm/aaaa): ")
        locacao = Locacao(cliente, veiculo, inicio, fim)
        self.locacoes.append(locacao)
        print("Locação realizada com sucesso!")

    def relatorio_locacoes(self):
        if not self.locacoes:
            print("Nenhuma locação registrada.")
            return
        for loc in self.locacoes:
            v = loc.veiculo
            c = loc.cliente
            print("\n--- Locação ---")
            print(f"Veículo: {v.categoria} {v.marca} {v.modelo}, Ano: {v.ano}, Placa: {v.placa}")
            print(f"Cliente: {c.nome}, CPF: {c.cpf}, RG: {c.rg}")
            print(f"Período: {loc.inicio} até {loc.fim}")

# Função principal
def main():
    locadora = Locadora()
    while True:
        print("\nBem-vindo a Locadora Boa Viagem, escolha uma opção:")
        print("1) Cadastrar um Novo Veículo")
        print("2) Cadastrar um Novo Cliente")
        print("3) Realizar a locação de um Veículo")
        print("4) Relatório de locação")
        print("5) Sair")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            locadora.cadastrar_veiculo()
        elif opc == "2":
            locadora.cadastrar_cliente()
        elif opc == "3":
            locadora.realizar_locacao()
        elif opc == "4":
            locadora.relatorio_locacoes()
        elif opc == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
