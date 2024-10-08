# Sales API

## Descrição
Esta é uma API RESTful desenvolvida em **Django Rest Framework (DRF)** para o gerenciamento de **vendas**, **produtos**, **clientes** e **vendedores**. O projeto utiliza **MySQL** como banco de dados e está dockerizado usando **Docker Compose**. A documentação da API é gerada automaticamente usando **Swagger** e **ReDoc**.

## Pré-requisitos
Antes de começar, certifique-se de ter os seguintes softwares instalados:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Iniciar o Projeto
Para rodar o projeto, siga as etapas abaixo:

1. No diretório raiz do projeto, execute o comando para subir os containers:

    ```bash
    docker-compose up --build
    ```

    Este comando vai:
    - Criar e rodar o container do banco de dados **MySQL**.
    - Rodar a aplicação **Django** no container.

2. Acesse a aplicação em seu navegador:

    ```
    http://localhost:8000
    ```

3. Para acessar a documentação **Swagger** da API, utilize:

    ```
    http://localhost:8000/swagger/
    ```

4. Para acessar a documentação **ReDoc** da API:

    ```
    http://localhost:8000/redoc/
    ```

## Configurações da API
A API tem os seguintes endpoints principais:

- `/api/clientes/` - Endpoints para gerenciar clientes.
- `/api/produtos/` - Endpoints para gerenciar produtos.
- `/api/vendas/` - Endpoints para gerenciar vendas.
- `/api/vendedores/` - Endpoints para gerenciar vendedores.

## Rodando Migrações
Se houver alterações no banco de dados ou na modelagem, lembre-se de rodar as migrações:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

ou acesse o modo interativo:
```bash
docker exec -it django_app bash
cd app
python manage.py makemigrations
python manage.py migrate
```