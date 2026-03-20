# Capítulo 1 - Exercício 1

#Exercício: Você estabelece um canal de cominucação entre dois castelos medievais, permitindo que um corvo treinado carregue rapidamente um pergaminho do castelo que enviou ao castelo que recebe, a 160km de distância. o corvo voa a uma velocidade média de 40 km/h e carrega um pergaminho de cada vez. Cada pergaminho contem 1,8 tb de dados. Calcule a taxa de dados deste canal ao enviar (i) 1,8 tb de dados; (ii) 3,6 tb de dados; (iii) fluxo infinito de dados.

distancia = 160  # km
velocidade = 40  # km/h
tempo = distancia / velocidade  # 4h
capacidade_pergaminho = 1.8     # TB

# taxa em TB/h
taxa_TB_h = capacidade_pergaminho / tempo

# conversões
bytes_por_TB = 10**12
bits_por_byte = 8
segundos_por_hora = 3600

# taxa em bits/s
taxa_bps = (taxa_TB_h * bytes_por_TB * bits_por_byte) / segundos_por_hora

print('(i) Envio de 1,8 TB')
print(f'Taxa de dados: {taxa_TB_h} TB/h')
print(f'Convertido para bps: {taxa_bps:,.2f} (~1 Gbps)\n')

print('(ii) Envio de 3,6 TB')
print(f'Taxa de dados: {taxa_TB_h} TB/h (mesma taxa)\n')

print('(iii) Fluxo infinito de dados')
print(f'Taxa de dados sustentada: {taxa_TB_h} TB/h (~1 Gbps)')
