# API-IBGE-python
Este script tem como objetivo buscar dados da API do IBGE e imprimir informações específicas obtidas em resposta.

Pré-requisitos:
Python 3.x
Bibliotecas: requests e python-dotenv. Você pode instalá-las usando:
pip install requests python-dotenv

Configuração:
Crie um arquivo .env no diretório raiz do seu projeto.
Adicione o link da API no arquivo .env da seguinte forma:
IBGE_API_KEY=seu_link_aqui
Substitua seu_link_aqui pelo link da API que você deseja usar.

Uso:
Para executar o script, use:
python nome_do_seu_script.py

Funcionamento:
O script carrega o link da API do arquivo .env, realiza uma requisição GET para obter os dados, 
analisa a resposta JSON e imprime as informações da variável e da série.

Tratamento de Erros:
O script inclui tratamentos de erros para:
Erros de requisição à API.
Estrutura de resposta inesperada da API.
Outros erros inesperados.
