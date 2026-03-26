print("Questão 9: \n Um sistema cliente-servidor usa uma rede de satélite, com o satélite a uma altura de 40.000 km. Qual é o maior atraso em resposta a uma solicitação?")

print("Resolução:")
print("- altura de 40.000 km")
print("- do servidor ao satélite: 40.000 km")
print("- do satélite ao servidor: 40.000 km")
print("- do cliente ao satélite: 40.000 km")
print("- do satélite ao cliente: 40.000 km")
print("- ou seja, 4 x 40.000 km = 160.000 km")

print("distância total = 160.000 km")

print("- converter para metros: 160.000 km x 1.6**8 m/km = 160.000.000 m")
print("- velocidade da luz no vácuo (3*10**8). Mas em redes usamos 2/3 disso (2*10**8 m/s): 3 x 10**8 m/s")
print("- calcular o tempo: tempo = 1,6*10**8/2*10**8 = 0.8 s")


altura = 40000  # km

velocidade_luz = 2 * 10**8  # m/s

distancia_total = 4 * altura * 10**3  # km → m

tempo = distancia_total / velocidade_luz # s

print("Atraso total (s):", tempo, "s")
print("Atraso total (ms):", tempo * 1000, "ms")
