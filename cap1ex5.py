'''

Uma alternativa para uma LAN é simplesmente instalar um grande sistema de tempo compartilhado (timasharing) com terminais para todos os usuários. Apresente duas vantagens de um sistema cliente-servidor que utiliza LAN.

Uma rede local (LAN – Local Area Network) é uma rede de computadores que conecta dispositivos em uma área geograficamente limitada, como uma casa, escola ou empresa, permitindo a comunicação e o compartilhamento de recursos. Já um sistema de time-sharing (tempo compartilhado) é um modelo em que vários usuários acessam simultaneamente um único computador central, utilizando terminais, que são dispositivos de entrada e saída (como monitores e teclados) sem capacidade própria de processamento significativo, dependendo totalmente do sistema central.

Em comparação a esse modelo centralizado, o sistema cliente-servidor baseado em LAN apresenta vantagens importantes.



A primeira vantagem é a distribuição de processamento. Em uma arquitetura cliente-servidor, cada máquina cliente possui capacidade própria de processamento, reduzindo a sobrecarga sobre um único sistema central. Isso melhora o desempenho geral e permite que múltiplos usuários executem tarefas de forma mais eficiente e independente.

A segunda vantagem é a maior confiabilidade e flexibilidade. Em sistemas de time-sharing, uma falha no computador central pode interromper o acesso de todos os usuários. Já em uma rede LAN cliente-servidor, a falha de um equipamento não necessariamente compromete toda a rede, tornando o sistema mais robusto. Além disso, a arquitetura cliente-servidor facilita a expansão da rede, permitindo a adição de novos dispositivos e serviços conforme a necessidade.

Dessa forma, o modelo cliente-servidor em redes locais se mostra mais eficiente, escalável e confiável quando comparado ao sistema tradicional de tempo compartilhado.

🧠 O que é time-sharing (tempo compartilhado)?

É um modelo antigo de computação onde várias pessoas usam UM único computador ao mesmo tempo.

👉 Mas como isso é possível?

O sistema operacional divide o tempo do processador em pequenos pedaços e alterna rapidamente entre os usuários.

💡 Isso acontece tão rápido que parece que cada pessoa tem um computador só pra ela, mas na verdade todos estão compartilhando o mesmo.

🖥️ Exemplo simples

Imagina:

Um computador muito poderoso (servidor)

10 pessoas conectadas nele

Cada pessoa usa um terminal (só tela + teclado, sem “cérebro”)

O servidor faz assim:

0,01s → usuário 1

0,01s → usuário 2

0,01s → usuário 3

...

E fica repetindo isso MUITO rápido.

👉 Resultado: todo mundo acha que está usando sozinho.

🎮 Analogia fácil

Pensa em um videogame:

Só tem 1 controle

10 pessoas querem jogar

Então vocês fazem assim:

cada um joga por 2 segundos

depois passa pro próximo

Se isso acontecer muito rápido, parece que todo mundo está jogando ao mesmo tempo.

⚠️ Problema do time-sharing

Se o computador central cair → todo mundo para

Se muita gente usar → fica lento

Tudo depende de uma única máquina

🔄 Diferença para hoje (LAN)

Hoje:

Cada pessoa tem seu próprio computador (PC ou celular)

Não precisa dividir processamento

👉 Por isso o modelo moderno (cliente-servidor) é melhor

🧾 Resumão (pra prova)

Time-sharing é um modelo em que vários usuários compartilham um único computador central, que divide seu tempo de processamento entre eles, permitindo acesso simultâneo por meio de terminais.

'''