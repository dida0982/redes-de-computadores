# Capítulo 1 - Exercício 1

#Exercício: Você estabelece um canal de cominucação entre dois castelos medievais, permitindo que um corvo treinado carregue rapidamente um pergaminho do castelo que enviou ao castelo que recebe, a 160km de distância. o corvo voa a uma velocidade média de 40 km/h e carrega um pergaminho de cada vez. Cada pergaminho contem 1,8 tb de dados. Calcule a taxa de dados deste canal ao enviar (i) 1,8 tb de dados; (ii) 3,6 tb de dados; (iii) fluxo infinito de dados.

#Dados do Problema:
distancia = 160  # 160km
velocidade = 40  # 40km/h
tempo = distancia/velocidade # 4h
capacidade_pergaminho = 1.8 # 1,8TB
#um pergaminho por viagem
taxa = capacidade_pergaminho/tempo #0.45 TB/h


print('(i) Envio de 1,8 TB')
print('Taxa de dados: ', taxa, 'TB/h' )
converter_bps = taxa * (10**12) * 8 /3600
print(f'Convertido para bps: {converter_bps:,.2f} (1 Gbps)')

print("")
print('(ii) Envio de 3.6 tb de dados:')
taxa2 = (capacidade_pergaminho*2)/(tempo*2)
print('Taxa de dados: ', taxa2 )
