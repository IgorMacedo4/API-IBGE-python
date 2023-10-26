import os
import requests
from dotenv import load_dotenv

#Carrega as variaveis ambientes do arquivo .env
load_dotenv()

def buscar_dados_do_ibge():
    """
    Busca dados da API do IBGE e imprime as informações da variável e da série.
    """
    link = os.getenv("IBGE_API_KEY")

    try:
        # Enviando uma requisição GET para a API
        requisicao = requests.get(link)
        requisicao.raise_for_status()  # Lança uma exceção para erros HTTP

        # Analisando a resposta JSON
        informacoes = requisicao.json()

        # Extraindo as informações desejadas da resposta
        item_busca = informacoes[0]['variavel']  # variável
        resultados = informacoes[0]['resultados'][0]['series']  # séries

        # Imprimindo as informações extraídas
        print(item_busca)
        print(resultados)

    except requests.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}")
    except KeyError:
        print("Erro: Estrutura de resposta inesperada da API.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chamando a função para buscar e imprimir os dados
buscar_dados_do_ibge()
