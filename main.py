import json

class FilaTelemetria:
    """
    Classe que implementa a estrutura de dados Fila (Queue) 
    para processamento FIFO (First In, First Out).
    """

    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None

    def tamanho(self):
        return len(self.itens)


def carregar_dados_json(caminho_arquivo):
    """Lê o arquivo JSON e retorna os dados."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print(f"[+] {len(dados)} registros carregados com sucesso do arquivo {caminho_arquivo}.")
            return dados
    except FileNotFoundError:
        print(f"[-] Erro: Arquivo {caminho_arquivo} não encontrado.")
        return []
    except json.JSONDecodeError:
        print("[-] Erro: Falha ao decodificar o arquivo JSON.")
        return []


def processar_fila_alertas(dados_brutos):
    """
    Carrega os dados na Fila e simula o processamento do Edge Computing.
    Retorna uma lista processada (log histórico) para futura busca.
    """
    fila = FilaTelemetria()
    historico_processado = []

    for alerta in dados_brutos:
        fila.enfileirar(alerta)

    print(f"\n[*] Iniciando processamento da Fila (Total: {fila.tamanho()} alertas)...")

    while not fila.esta_vazia():
        alerta_atual = fila.desenfileirar()
        if alerta_atual['severidade'] == "Critica":
            print(f"    [!] ALERTA CRÍTICO PROCESSADO: {alerta_atual['modulo']} - {alerta_atual['anomalia']}")

        historico_processado.append(alerta_atual)

    print("[+] Processamento da fila concluído.")
    return historico_processado


def busca_binaria_recursiva(lista, alvo_id, inicio, fim):
    """
    Busca um alerta específico pelo ID utilizando Busca Binária e Recursividade.
    A lista deve estar ordenada pelo ID.
    """
    if inicio > fim:
        return None

    meio = (inicio + fim) // 2
    id_meio = lista[meio]['id']

    if id_meio == alvo_id:
        return lista[meio]
    elif id_meio > alvo_id:
        return busca_binaria_recursiva(lista, alvo_id, inicio, meio - 1)
    else:
        return busca_binaria_recursiva(lista, alvo_id, meio + 1, fim)


def main():
    print("=" * 50)
    print(" SISTEMA DE TRIAGEM ACÚSTICA ESPACIAL - ECHOVITA")
    print("=" * 50)

    arquivo_dados = 'data.json'

    dados_telemetria = carregar_dados_json(arquivo_dados)

    if not dados_telemetria:
        return

    historico_alertas = processar_fila_alertas(dados_telemetria)

    print("\n" + "=" * 50)
    print(" PAINEL DE BUSCA DE METADADOS")
    print("=" * 50)

    while True:
        entrada = input("Digite o ID do alerta que deseja buscar (ou '0' para sair): ")

        if entrada == '0':
            print("Encerrando o sistema. Bom trabalho, comandante.")
            break

        try:
            id_busca = int(entrada)

            resultado = busca_binaria_recursiva(historico_alertas, id_busca, 0, len(historico_alertas) - 1)

            if resultado:
                print("\n[+] Alerta Localizado:")
                print(f"    ID: {resultado['id']}")
                print(f"    Módulo: {resultado['modulo']}")
                print(f"    Anomalia: {resultado['anomalia']}")
                print(f"    Severidade: {resultado['severidade']}")
                print(f"    Timestamp: {resultado['timestamp']}\n")
            else:
                print(f"\n[-] Alerta com ID {id_busca} não encontrado nos registros.\n")

        except ValueError:
            print("\n[-] Por favor, digite um número de ID válido.\n")


if __name__ == "__main__":
    main()