# Estrutura básica para um projeto Python

Esse repositório tem um exemplo de como organizar um projeto Python com testes de unidade. Foi usado o pipenv para criar o ambiente virtual e gerenciar os pacotes.

## Ferramentas necessárias

- Python3
- pip3 (para instalar o pipenv)
  - `pip3 install --user pipenv`
- IDE
  - [PyCharm](https://www.jetbrains.com/pt-br/pycharm); ou
  -  [Visual Studio Code](https://code.visualstudio.com) com as seguintes extensões
     - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
     - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

### Configurando o pipenv

Fazer uso do [pipenv](https://pipenv.pypa.io/en/stable/) como gerenciador de pacotes. Ele substitui o `pip` e o `virtualenv`.

Para garantir que o diretório `.venv` será criado dentro do diretório do projeto e não em `$HOME/.local/...`, coloque a seguinte linha no arquivo de configuração da tua shell (`.bashrc` ou `.zshrc` no home do seu usuário).
```bash
export PIPENV_VENV_IN_PROJECT=1
``` 
Carregue novamente a shell (p.ex. fechando o terminal atual e abrindo um novo terminal, ou `source ~/.bashrc` ou `source ~/.zshrc`)

## Criando a estrutura do projeto

```bash
mkdir python-olamundo
cd python-olamundo

# criando ambiente virtual
pipenv --three
# carregando ambiente virtual
pipenv shell

# criando estrutura de diretórios (pacotes Python) e arquivos (módulos Python)
mkdir saudacao
touch saudacao/__init__.py
touch saudacao/ola_mundo.py
mkdir tests
touch tests/__init__.py
touch tests/test_ola_mundo.py
```

Após isso o diretório do projeto deverá ficar como apresentado abaixo.

```bash
python-olamundo
├── Pipfile
├── saudacao
│   ├── __init__.py
│   └── ola_mundo.py
└── tests
    ├── __init__.py
    └── test_ola_mundo.py
```

## Instalando pacotes com o pipenv

Ao instalar um pacote com o pipenv, esse será automaticamente adicionado no arquivo [Pipfile](Pipfile) o qual manterá todas as dependências de pacotes desse projeto.

```bash
# Exemplo para demonstrar como instalar a biblioteca Requests
pipenv install requests
```

Isso irá criar o arquivo `Pipfile.lock` e uma explicação sobre o mesmo pode ser [encontrada aqui](https://realpython.com/pipenv-guide/#the-pipfilelock).

Se clonar um repositório que já tenha os arquivos `Pipfile` e `Pipfile.lock`, você pode instalar os pacotes ali informados com o comando: 

```bash
pipenv install
```

Isso seria equivalente ao comando `pip install -r requirements.txt`.

## Testes de unidade com `unittest`

No arquivo [test_ola_mundo.py](tests/test_ola_mundo.py) tem um simples teste de unidade feito com o framework [unittest](https://docs.python.org/3/library/unittest.html) do Python.

### Executar testes no terminal

```bash
# caso ainda não tenha carregado o ambiente virtual
pipenv shell

# para executar o teste de unidade
python -m unittest -v tests/test_ola_mundo.py
```

### Executar testes com o VSCode

- Abrir a paleta de comando e procurar por **Python: Discover Tests**, informar o diretório, padrão do nome dos arquivos, etc. Depois disso, acima de cada classe vai aparecer `Run Test`
- Para executar os testes, abra o painel (*view*) de testes e escolha quais testes deseja executar

> Esse repositório já contém [as configurações do vscode](.vscode/settings.json) para descoberta dos testes de unidade.

### Testes com o PyCharm

- Veja [documentação oficial](https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#create-test) da JetBrains.

## Convenção para escrita do código

Nesse repositório seguiu-se a proposta [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).

### Módulos e pacotes

- **Módulos** são arquivos Python (`.py`) e devem possuir nomes curtos, sempre em caixa baixa e com o estilo snake_case
- **Pacotes** são diretórios que contém módulos Python e devem possuir nomes curtos, sempre em caixa baixa e evitar o estilo snake_case
  - A partir do Python 3.3, o arquivo `__init__.py` dentro do pacote é necessário quando se deseja executar algum comportamento quando o pacote for importado. Caso contrário, esse arquivo [não é mais necessário](https://www.python.org/dev/peps/pep-0420/). 

### Nomes de classes, métodos, funções e variáveis

- `NomeDeClasses` devem seguir o formato CamelCase (PascalCase)
- Métodos, funções e variáveis sempre em caixa baixa e com o estilo snake_case

## Licença de software

Sempre que fizer um software é interessante indicar sob qual a licença o mesmo está sendo disponibilizado. Acesse https://choosealicense.com e veja qual licença seria mais adequada para o seu projeto e coloque a mesma no arquivo [LICENSE](LICENSE) na raiz do projeto.

## Referências

- https://realpython.com/python-application-layouts/
- https://pipenv.pypa.io/en/stable/
- https://realpython.com/pipenv-guide/
- https://packaging.python.org/overview/