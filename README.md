# metrify 📊📈📉

![Tox](https://github.com/open-metrify/metrify/actions/workflows/tests.yaml/badge.svg)
![Docs](https://github.com/open-metrify/metrify/actions/workflows/docs.yaml/badge.svg)

Sistema de coleta automática de métricas com base na API do Github.

[Documentação Completa](https://open-metrify.github.io/metrify/index.html)

## Instalação & Execução

Para executar o projeto localmente, é necessário instalar as seguintes
ferramentas:

- [**Python** (^3.12)](#python)
- [**venv**](#venv)
- [**pipx** (opcional porém recomendado)](#pipx)
- [**Poetry**](#poetry)
- [**Docker**](#docker-e-compose)

### Python

Instalação do intérprete pode ser realizada de acordo com o manual disponível na
[documentação oficial](https://www.python.org/downloads/release/python-3120/).
Pode ser necessário realizar a instalação através dos repositórios do
[deadsnakes](https://github.com/deadsnakes).

### venv

Ambientes virtuais são a maneira mais convencional de isolar a instalação de
pacotes python no contexto do sistema operacional. A ferramenta pode ser
instalada de acordo com a
[documentação oficial](https://virtualenv.pypa.io/en/stable/installation.html).
Pode ser necessário realizar a instalação através dos repositórios do
[deadsnakes](https://github.com/deadsnakes).

### pipx

pipx é um gerenciador de pacotes que permite a execução de apliações Python em
ambientes isolados. A instalação da ferramenta é opcional, porém recomendada
para instalar o Python Poetry (ver próxima seção), que é utilizado para o
gerenciamento de dependências do projeto. O processo de instalação está
disponível na [documentação oficial](https://pipx.pypa.io/stable/installation/).

### Poetry

O Poetry é a ferramenta de gerenciamento de dependências do projeto; pode ser
instalada de acordo com o manual encontrado na
[documentação oficial](https://python-poetry.org/docs/#installation);
recomenda-se realizar a instalação através do `pipx`.

### Docker e Compose

Docker e a ferramenta auxiliar Compose são utilizados para isolar a execução de
processos e aplicações em máquinas virtualizadas separadamente do ambiente do
sistema operacional. Para instalar as ferramentas, siga os passos especificados
para a distribuição do seu SO de acordo com a
[documentação oficial](https://docs.docker.com/desktop/install/linux-install/).

### Instalação das dependências do projeto

Para instalar as dependências do projeto basta inicializar o ambiente virtual e
executar o comando de instalação:

```bash
source venv/bin/activate
poetry install
```

## Executando a aplicação localmente

> Antes de inicializar a aplicação, é necessário ativar o container do banco de
> dados do projeto no [docker](#docker-e-compose). Para verificar o status atual
> do container execute o comando `docker ps`:
>
> ```bash
> docker ps
> CONTAINER ID   IMAGE                  COMMAND                  CREATED        STATUS             PORTS                                       NAMES
> 918266dc5863   mongo                  "docker-entrypoint.s…"   6 days ago     Up About an hour   27017/tcp                                   metrify_mongo_1
> ```
>
> Caso o container do metrify não conste na lista apresentada, execute o
> [compose](#docker-e-compose) (dentro do projeto) para ativar os containers:
>
> ```bash
> # Dependendo da versão do Docker instalada no sistema, execute "docker compose" ou "docker-compose", se o compose for instalado separadamente. Consultar documentação oficial.
>
> docker compose up -d mongo
> Creating metrify_mongo_1 ... done
> ```

Após a instalação de todos os recursos, certifique-se de ativar o ambiente
virtual para executar o servidor Flask:

```bash
source venv/bin/activate
flask run
```

A aplicação estará disponível em no endereço `127.0.0.1:5000`.
