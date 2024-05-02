# metrify 📊📈📉

Sistema de coleta automática de métricas com base nos webhooks do Github
Projects.

## Configuração do ambiente de desenvolvimento

### Instalação das ferramentas

Para executar o projeto localmente, é necessário instalar as seguintes
ferramentas:

- [**Python** (^3.12)](#python)
- [**venv**](#venv)
- [**pipx** (opcional porém recomendado)](#pipx)
- [**Poetry**](#poetry)
- [**MongoDB**](#mongodb)

#### Python

Instalação do intérprete pode ser realizado de acordo com o manual disponícel na
[documentação oficial](https://www.python.org/downloads/release/python-3120/).
Pode ser necessário realizar a instalação através dos repositórios do time
[deadsnakes](https://github.com/deadsnakes).

#### venv

Ambientes virtuais são a maneira mais convenvional de isolar a instalação de
pacotes python no contexto do sistema operacional. A ferramenta pode ser
instalada de acordo com a
[documentação oficial](https://virtualenv.pypa.io/en/stable/installation.html).
Pode ser necessário realizar a instalação através dos repositórios do time
[deadsnakes](https://github.com/deadsnakes).

#### pipx

pipx é um gerenciador de pacotes que permite a execução de apliações Python em
ambientes isolados. A instalação da ferramenta é opcional, porém recomendada
para instalar o Python Poetry (ver próxima seção), que é utilizado para o
gerenciamento de dependências do projeto. O processo de instalação está
disponível na [documentação oficial](https://pipx.pypa.io/stable/installation/).

#### Poetry

O Poetry é a ferramenta de gerenciamento de dependências do projeto; pode ser
instalada de acordo com o manual encontrado na
[documentação oficial](https://python-poetry.org/docs/#installation);
recomenda-se realizar a instalação através do `pipx`.

#### MongoDB

Instale uma versão atual gerenciador de banco de dados na versão _Community
Edition_ de acordo com o manual para a distribuição do SO da sua máquina na
[documentação oficial](https://www.mongodb.com/docs/manual/installation/).

### Instalação das dependências do projeto

Para instalar as dependências do projeto basta inicializar o ambiente virtual e
executar o comando de instalação:

```bash
source venv/bin/activate
poetry install
```

## Executando a aplicação localmente

Após a instalação de todos os recursos, certifique-se de ativar o ambiente
virtual para executar o servidor Flask:

```bash
source venv/bin/activate
flask run
```

A aplicação estará disponível em no endereço `127.0.0.1:5000`.
