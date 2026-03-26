'''

Um fator que influencia no atraso de um sistema de comunicação de pacotes store-and-forwrard é qual o tempo necessário para armazenar um pacote por um por um switch. Se o tempo de comutação é 20ms, é provável que esse seja um fator importante na resposta de um sistema cliente-servidor quando o cliente está em Nova York e o serviço está na California. Suponha que a velocidade de propagação em cobre e fibra seja a 2/3 da velocidade da luz no vácuo.

'''

"""
Exercício: Análise de atraso em rede store-and-forward

Dados:
- Tempo de comutação por switch: 20 ms
- Velocidade de propagação: 2/3 da velocidade da luz
- Distância aproximada NY → Califórnia: 4500 km 
- velocidade da luz: 3 x 10^8 m/s
- numero de switches: variável (entrada do usuário)

Objetivo:
Comparar tempo de propagação com tempo de comutação
"""

# -----------------------------
# 1. Definição de constantes
# -----------------------------

c = 3 * 10**8  # velocidade da luz (m/s) R: 300,000,000 m/s
v = (2/3) * c  # velocidade no meio físico R: 200,000,000 m/s

distancia = 4.5 * 10**6  # 4500 km em metros

tempo_switch = 20  # ms por switch

# -----------------------------
# 2. Entrada do usuário
# -----------------------------

num_switches = int(input("\n OBS: \n - 2 ou 3 → mais realista (rede simples)\n - 5 ou 6 → rede maior (internet real)\n - 10+ → pra testar e ver o impacto crescer \n    Digite o número de switches: "))

# -----------------------------
# 3. Cálculos
# -----------------------------

# Tempo de propagação (s)
tempo_propagacao = distancia / v # distancia = 4500 | v= 200,000,000 m/s | R: 0.0000225 s

# Converter para ms
tempo_propagacao_ms = tempo_propagacao * 1000 # tempo_propagacao = 0.0000225 s * 1000 | R: 0.0225 ms

# Tempo total de comutação
tempo_total_switch = num_switches * tempo_switch # num_switches = 3 | tempo_switch = 20 ms | R: 60 ms

# Tempo total da comunicação
tempo_total = tempo_propagacao_ms + tempo_total_switch # tempo_propagacao_ms = 0.0225 ms + tempo_total_switch = 60 ms | R: 60.0225 ms

# -----------------------------
# 4. Saída
# -----------------------------

print("\n--- RESULTADOS ---")
print(f"Velocidade no cabo: {v:.2e} m/s")
print(f"Tempo de propagação: {tempo_propagacao_ms:.2f} ms")
print(f"Tempo total de comutação: {tempo_total_switch} ms")
print(f"Tempo total da comunicação: {tempo_total:.2f} ms")

# Comparação
if tempo_total_switch > tempo_propagacao_ms:
    print("Conclusão: O tempo de comutação é MAIS relevante.")
else:
    print("Conclusão: O tempo de propagação é MAIS relevante.")

    '''
    -tempo de computação é o fator dominante no atraso total, especialmente à medida que o número de switches aumenta. Mesmo com uma velocidade de propagação muito alta, o tempo gasto em cada switch pode superar significativamente o tempo de propagação, tornando a comutação o principal contribuinte para o atraso total.
    -tempo de propagação é relativamente pequeno em comparação com o tempo de comutação, especialmente em distâncias longas como entre Nova York e Califórnia. Portanto, otimizar o tempo de comutação (por exemplo, usando switches mais rápidos ou reduzindo o número de switches) pode ter um impacto mais significativo na redução do atraso total do que otimizar a velocidade de propagação.

    O que é tempo de computação?
    O tempo de computação refere-se ao tempo gasto para processar um pacote em um switch, incluindo a leitura do cabeçalho, a tomada de decisão de encaminhamento e a preparação do pacote para transmissão. Em um sistema store-and-forward, o switch deve receber o pacote inteiro antes de começar a processá-lo, o que contribui para o atraso total. O tempo de computação é influenciado pela eficiência do hardware do switch e pela complexidade das operações de processamento necessárias para encaminhar o pacote.

    O que é tempo de propagação?
    O tempo de propagação é o tempo que leva para um sinal viajar de um ponto a outro na rede. Ele é calculado dividindo a distância entre os pontos pela velocidade de propagação do sinal no meio físico (como cobre ou fibra óptica). O tempo de propagação é influenciado pela distância e pela velocidade de propagação, mas não é afetado pelo número de switches ou pelo processamento em cada switch.
    '''