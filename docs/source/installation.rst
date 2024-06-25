Instalação
==========

Overview
--------
Esta página descreve o processo de instalação, configuração e execução local da
aplicação.

Instalação das ferramentas
~~~~~~~~~~~~~~~~~~~~~~~~~~

Para executar o projeto localmente, é necessário instalar as seguintes
ferramentas:

-  `Python (^3.12) <#python>`__
-  `venv <#venv>`__
-  `pipx (opcional porém recomendado) <#pipx>`__
-  `Poetry <#poetry>`__
-  `Docker <#docker-e-compose>`__

Python
^^^^^^

Instalação do intérprete pode ser realizada de acordo com o manual
disponível na `documentação
oficial <https://www.python.org/downloads/release/python-3120/>`__. Pode
ser necessário realizar a instalação através dos repositórios do
`deadsnakes <https://github.com/deadsnakes>`__.

venv
^^^^

Ambientes virtuais são a maneira mais convencional de isolar a
instalação de pacotes python no contexto do sistema operacional. A
ferramenta pode ser instalada de acordo com a `documentação
oficial <https://virtualenv.pypa.io/en/stable/installation.html>`__.
Pode ser necessário realizar a instalação através dos repositórios do
`deadsnakes <https://github.com/deadsnakes>`__.

pipx
^^^^

pipx é um gerenciador de pacotes que permite a execução de apliações
Python em ambientes isolados. A instalação da ferramenta é opcional,
porém recomendada para instalar o Python Poetry (ver próxima seção), que
é utilizado para o gerenciamento de dependências do projeto. O processo
de instalação está disponível na `documentação
oficial <https://pipx.pypa.io/stable/installation/>`__.

Poetry
^^^^^^

O Poetry é a ferramenta de gerenciamento de dependências do projeto;
pode ser instalada de acordo com o manual encontrado na `documentação
oficial <https://python-poetry.org/docs/#installation>`__; recomenda-se
realizar a instalação através do ``pipx``.

Docker e Compose
^^^^^^^^^^^^^^^^

Docker e a ferramenta auxiliar Compose são utilizados para isolar a
execução de processos e aplicações em máquinas virtualizadas
separadamente do ambiente do sistema operacional. Para instalar as
ferramentas, siga os passos especificados para a distribuição do seu SO
de acordo com a `documentação
oficial <https://docs.docker.com/desktop/install/linux-install/>`__.

Instalação das dependências do projeto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Antes de instalar qualquer módulo adicional no intérprete python, é importante
isolar o ambiente da aplicação através de um ambiente virutal. Caso seja a 
primeira vez executando o sistema, talvez seja necessário criar os arquivos do 
ambiente local:

.. code:: bash

   python3.12 -m venv venv

Para instalar as dependências do projeto basta inicializar o ambiente
virtual e executar o comando de instalação:

.. code:: bash

   source venv/bin/activate
   poetry install

Executando a aplicação localmente
---------------------------------

   Antes de inicializar a aplicação, é necessário ativar o container do
   banco de dados do projeto no `docker <#docker-e-compose>`__. Para
   verificar o status atual do container execute o comando
   ``docker ps``:

   .. code:: bash

      docker ps
      CONTAINER ID   IMAGE                  COMMAND                  CREATED        STATUS             PORTS                                       NAMES
      918266dc5863   mongo                  "docker-entrypoint.s…"   6 days ago     Up About an hour   27017/tcp                                   metrify_mongo_1

   Caso o container do metrify não conste na lista apresentada, execute
   o `compose <#docker-e-compose>`__ (dentro do projeto) para ativar os
   containers:

   .. code:: bash

      # Dependendo da versão do Docker instalada no sistema, execute "docker compose" ou "docker-compose", se o compose for instalado separadamente. Consultar documentação oficial.

      docker compose up -d mongo
      Creating metrify_mongo_1 ... done

É necessário exportar as credenciais da aplicação em um arquivo ``.env``
para que seja possível realizar a integração com os serviços do Github;
para fazer isso, adicione o arquivo na raiz do projeto da seguinte
maneira:

.. code:: diff

       .
       ├── .coverage
       ├── docker-compose.yml
       ├── docs
       │   ├── build
       │   ├── make.bat
       │   ├── Makefile
       │   └── source
   +   ├── .env
       ├── .flaskenv
       ├── .github
       │   └── workflows
       ├── .gitignore
       ├── LICENSE.rst
       ├── metrify
       ...

Registre os dados de configuração para a integração:

.. code:: sh

   # .env
   APP_ID="app_id"
   PRIVATE_KEY_PATH="./.private-key.pem"
   INSTALLATION_ID="your_installation_id"

As variáveis ``APP_ID`` e ``INSTALLATION_ID`` são referentes ao ID universal do
Github App e ID da instalação do app na organização de destino, respectivamente.
A variável de ambiente ``PRIVATE_KEY_PATH`` deve apontar para a localização do
arquivo ``.pem`` da chave privada da aplicação (consultar com equipe de
desenvolvimento para adquirir uma chave de acesso).

Recomenda-se salvar a chave de acesso em um arquivo ``.private-key.pem``
na raiz do projeto, como demonstrado no exemplo de configuração, da
seguinte maneira:

.. code:: diff

       .
       ├── .coverage
       ├── docker-compose.yml
       ├── docs
       │   ├── build
       │   ├── make.bat
       │   ├── Makefile
       │   └── source
       ├── .env
   +   ├── .private-key.pem
       ├── .flaskenv
       ├── .github
       │   └── workflows
       ├── .gitignore
       ├── LICENSE.rst
       ├── metrify
       ...

Após a instalação de todos os recursos, certifique-se de ativar o
ambiente virtual para executar o servidor Flask:

.. code:: bash

   source venv/bin/activate
   flask run

A aplicação estará disponível em no endereço ``127.0.0.1:5000``.

pre-commit
----------

O projeto é configurado para executar uma checagem rápida do código
antes de cada commit no controle de versão. Para habilitar os *hooks*,
basta executar o comando de instalação:

.. code:: bash

   # Com o ambiente virtual ativo e após instalar as dependências do projeto (poetry install)
   pre-commit install

Testes unitários
----------------

Estrutura
~~~~~~~~~

O repositório do projeto é disposto de acordo com a estrutura a seguir:

::

   .
   ├── metrify
   │   ├── hello
   │   │   ├── __init__.py
   │   │   ├── strategies.py
   │   │   └── routes.py
   │   ├── __init__.py
   │   └── metrify.py
   ├── poetry.lock
   ├── pyproject.toml
   ├── README.md
   ├── tests
   │   ├── hello
   │   │   ├── __init__.py
   │   │   └── test_strategies.py
   │   └── __init__.py
   └── tox.ini

Onde os arquivos de teste no diretório ``tests/`` devem espelhar a
disposição dos arquivos no diretório-fonte (``metrify/``).

-  A estrutura de diretórios deve ser identica aos pacotes de código de
   serviço; a nomenclatura dos arquivos de teste deve seguir o padrão
   “test_<src>.py”, onde “src” refere-se ao nome do arquivo que está
   sendo testado.

-  A estrutura do código de teste deve espelhar o código que está sendo
   testado; o arquivo de teste deve seguir o padrão de um suite de testes (em
   forma de classe) por função testada, seguindo a nomenclatura "Test<Subject>",
   onde "Subject" refere-se ao nome função sendo testada, em
   `PascalCase <https://www.theserverside.com/definition/Pascal-case/>`__; cada
   caso de teste deve ser representado por um método da classe, com um nome
   descritivo.

.. code:: python

   # file: tests.hello.test_strategies

   from metrify.hello.strategies import hello

   class TestHello:
       """Test suite for `hello` function"""

       def test_hello(self):
           """Returns 'Hello, World!'"""
           assert hello() == "Hello, World!"

Executando testes e checagem com tox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O projeto está configurado para realizar a execução dos testes,
formatação, linting e checagem através do
`pytest <https://docs.pytest.org/en/8.2.x/>`__,
`autopep8 <https://pypi.org/project/autopep8/>`__,
`pylint <https://pylint.org/>`__ e `mypy <https://mypy-lang.org/>`__, e
automatizado através do `tox <https://tox.wiki/en/4.15.0/>`__.

É possível executar todos as checagens do sistema através do tox (via
Poetry):

.. code:: bash

   poetry run tox

Executar etapas do processo de checagem separadamente:

.. code:: bash

   poetry run pytest                   # testes
   poetry run pylint metrify tests     # linter
   poetry run mypy metrify tests       # type check

Ou em arquivos individuais:

.. code:: bash

   poetry run pylint metrify/hello/strategies.py
   poetry run pytest tests/hello/test_strategies.py
   ...
