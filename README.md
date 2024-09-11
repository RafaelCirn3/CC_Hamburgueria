# 🍔 Hamburgueria - Sistema de Pedidos e Comandas 🍟

Este é um sistema de gestão de mesas, comandas e pedidos para uma hamburgueria, desenvolvido com Django. Ele permite gerenciar mesas, registrar comandas, adicionar produtos a pedidos e calcular o valor total dos pedidos.

## 🚀 Funcionalidades

- Gerenciamento de Mesas (disponibilidade e ocupação)
- Registro de Comandas associadas às mesas
- Cadastro de produtos e itens em um pedido
- Cálculo automático do valor total dos pedidos
- Interface de administração para gerenciar todos os dados

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Django 3.2+**
- **SQLite** (pode ser substituído por outros bancos de dados, como PostgreSQL)
- **HTML/CSS** para interface básica (se houver templates)

---

## 📦 Como Instalar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/seu_projeto.git
cd seu_projeto
```

### 2. Crie e ative um ambiente virtual
É altamente recomendado utilizar um ambiente virtual para isolar as dependências do projeto.

```bash
# Crie o ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual (Linux/Mac)
source venv/bin/activate

# Ative o ambiente virtual (Windows)
venv\Scripts\activate
```
### 3. Instale as dependências do projeto
Com o ambiente virtual ativado, instale todas as dependências necessárias usando o arquivo requirements.txt.

```bash
pip install -r requirements.txt

pip freeze > requirements.txt
```
### 4. Realize as migrações do banco de dados
Antes de rodar o projeto, é necessário aplicar as migrações ao banco de dados.

```bash
python manage.py migrate
```

### 5. Crie um superusuário para acessar o Django Admin

```bash
python manage.py createsuperuser
```

### 6. Execute o servidor de desenvolvimento
Finalmente, inicie o servidor de desenvolvimento para ver o projeto em execução.


```bash
python manage.py runserver
```
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
coisas para fazer: 
Forms, Views, Urls, Validações e Regras de Negócios nas views

Sequência de apps para fazer
- Estoque
- Mesa
- Produto