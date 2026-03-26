'''

Um servidor envia pacotes a um cliente via satélite. Os pacotes devem atravessar um ou vários satélites antes de chegarem ao seu destino. Os satélites usam comutação de pacotes store-and-forward, com um tempo de comutação de 100 ms. Se os pacotes percorrem uma distancia total de 29700 km, por quantos satélites os pacotes terão que passar se 1% do atraso for causado pela comutação de pacotes? 


Resolição:

o que é store-and-forward ?
- Store-and-forward é um método de comutação de pacotes em redes de comunicação onde os pacotes são armazenados temporariamente em um dispositivo intermediário (como um roteador ou satélite) antes de serem encaminhados para o próximo destino. O dispositivo armazena o pacote inteiro, verifica sua integridade e, em seguida, o encaminha para o próximo salto na rota até chegar ao destino final. Esse processo pode introduzir um atraso adicional devido ao tempo necessário para armazenar e processar os pacotes, além do tempo de propagação.

o que é tempo de comutação de pacotes ?
- O tempo de comutação de pacotes é o tempo necessário para um dispositivo intermediário (como um roteador ou satélite) processar um pacote de dados antes de encaminhá-lo para o próximo destino. Esse tempo inclui o tempo necessário para armazenar o pacote, verificar sua integridade, tomar decisões de encaminhamento e, em alguns casos, realizar outras operações de processamento. O tempo de comutação de pacotes pode variar dependendo do dispositivo e da carga de tráfego na rede.

O que é propagação ?
- A propagação é o processo pelo qual um sinal de comunicação se propaga através de um meio físico, como o ar, o espaço ou um cabo. Em redes de comunicação, a propagação refere-se ao tempo que leva para um sinal viajar do ponto de origem ao ponto de destino. O tempo de propagação é influenciado pela distância entre os pontos e pela velocidade do sinal no meio de transmissão. Em redes de satélites, a propagação pode ser significativa devido às grandes distâncias envolvidas.

deferença de propagação e comutação de pacotes ?
- A diferença entre propagação e comutação de pacotes é que a propagação se refere ao tempo que leva para um sinal viajar do ponto de origem ao ponto de destino, enquanto a comutação de pacotes se refere ao tempo necessário para um dispositivo intermediário processar um pacote de dados antes de encaminhá-lo para o próximo destino. A propagação é influenciada pela distância e pela velocidade do sinal, enquanto a comutação de pacotes é influenciada pelo processamento do dispositivo intermediário.

- Tempo de comutação de pacotes: 100 ms
- Distância total: 29700 km
- Se 1% é de comutação de pacotes. Entao 99% é de propagação.
- Cada satélite adiciona 100 ms de comutação de pacotes.


Questão: Quantos satélites existem no caminho?
resposta: O resultado deu menos que 1 satélite, o que não faz sentido físico.

'''

# ----------------------------------------
# Cálculo do número de satélites (N)
# ----------------------------------------

import sympy as sp

# Dados do problema
tempo_por_satelite = 100 / 1000  # 100 ms → 0.1 s
distancia_total = 2.97 * 10**7   # metros (29700 km)
velocidade = 2 * 10**8           # m/s (2/3 da luz)

# Tempo de propagação
tempo_propagacao = distancia_total / velocidade  # segundos

# Definindo a variável N
N = sp.symbols('N')

# Equação:
# N * 0.1 = 0.01 * (tempo_propagacao + N * 0.1)
equacao = N * tempo_por_satelite - 0.01 * (tempo_propagacao + N * tempo_por_satelite)

# Resolver a equação
resultado = sp.solve(equacao, N)

# Mostrar resultados
print("Tempo de propagação (s):", tempo_propagacao)
print("Número de satélites (N):", resultado[0])


'''

👉 Isso quer dizer que **o tempo que o satélite demora para processar a informação é muito grande comparado ao tempo que o sinal leva para viajar**.

---

## 🔹 Em palavras simples

* O sinal viaja rápido (quase na velocidade da luz)
* Mas cada satélite **segura e processa o dado por um tempo considerável (100 ms)**

👉 Então o “atraso” não vem da distância
👉 Vem do **processamento dentro dos satélites**

---

## 🔹 Traduzindo para rede de computador

👉 Nessa rede:

* O problema **não é a distância**
* O problema é o **equipamento no caminho (os satélites)**

---

## 🔹 Resumo final

👉 “A rede é lenta não porque está longe, mas porque os dispositivos no caminho demoram para processar os dados.”


'''