# EchoVita: Triagem Acústica Espacial (Global Solution 2ESPY)

### Integrantes:
- Beatriz Cortez - RM561431
- Bruno Alves - RM563986
- Davi de Jesus - RM566316
- Gabriel Augusto - RM564126
- Raphaela Tatto - RM572059

## Contexto e Definição do Problema
O avanço da economia espacial exige soluções robustas para garantir a segurança e a saúde de astronautas e tripulantes em habitats espaciais. Em ambientes confinados, isolados e críticos como uma estação espacial, o monitoramento contínuo da saúde é um desafio, especialmente devido à latência de comunicação com a Terra e à necessidade de respostas rápidas.

Inspirado na tecnologia **EchoVita** (monitoramento bioacústico com inteligência artificial local - *Edge Computing*), este projeto propõe um sistema de processamento de backend para um nó de captação acústica espacial. O sistema processa anomalias sonoras (como tosses, vocalizações de estresse ou ruídos de despressurização) e emite metadados para um painel de monitoramento, operando de forma autônoma sem depender de internet contínua.

## Lógica de Resolução e Estruturas de Dados

Para resolver o desafio proposto e processar o alto volume de dados acústicos gerados pelos módulos da estação espacial, o sistema implementa as seguintes lógicas:

1. **Manipulação de Dados via Fila (Queue - FIFO):**
   Os sinais acústicos classificados pela IA local chegam em um fluxo contínuo. Para garantir que os eventos sejam processados e registrados na ordem cronológica exata em que ocorreram, utilizamos uma estrutura de dados Fila (First In, First Out). Os alertas entram na fila e são desenfileirados sequencialmente para processamento no painel de controle (ex: destacando alertas de severidade "Crítica").

2. **Algoritmo de Busca com Busca Binária e Recursividade:**
   Após o processamento na fila, os metadados são armazenados em um log histórico ordenado. Para permitir que engenheiros e médicos busquem ocorrências passadas com alto desempenho de tempo, o painel de busca implementa o algoritmo de Busca Binária utilizando Recursividade. A função divide a base de dados pela metade repetidamente até encontrar o ID do alerta solicitado.