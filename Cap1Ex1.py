# Capítulo 1 - Exercício 1
#Throughput: Taxa de dados, ou throughput, é a quantidade de dados que pode ser transmitida por unidade de tempo. A taxa de dados é geralmente expressa em bits por segundo (bps), mas também pode ser expressa em bytes por segundo (Bps), kilobits por segundo (kbps), megabits por segundo (Mbps), gigabits por segundo (Gbps), etc.

#Exercício: Você estabelece um canal de cominucação entre dois castelos medievais, permitindo que um corvo treinado carregue rapidamente um pergaminho do castelo que enviou ao castelo que recebe, a 160km de distância. o corvo voa a uma velocidade média de 40 km/h e carrega um pergaminho de cada vez. Cada pergaminho contem 1,8 tb de dados. Calcule a taxa de dados deste canal ao enviar (i) 1,8 tb de dados; (ii) 3,6 tb de dados; (iii) fluxo infinito de dados.

#Dados do Problema:
distancia = 160  # km
velocidade = 40  # km/h
dados_por_pergaminho = 1.8  # TB
tempo_de_viagem = distancia / velocidade  # 160 / 40 = 4 horas. Em 4h ele faz todo o percurso.

#taxa de dados:
taxa = dados_por_pergaminho / tempo_de_viagem  # 1.8 TB / 4h = 0.45 TB/h
print('Distancia: 160 km')
print('Velocidade: 40 km/h')
print(f'Tempo de viagem: {tempo_de_viagem} h')
print("Dados por pergaminho: 1.8 TB")

print("")

print(f'(i) Taxa de dados para 1,8 TB: {taxa} TB/h')
print("")
print(f'(ii) Taxa de dados para 3,6 TB: {taxa} TB/h')
print("")
print(f'(iii) Taxa de dados para fluxo infinito de dados: {taxa} TB/h')

