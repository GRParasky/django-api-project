# API para loja

Esse é um projeto de uma API para loja, contendo dois endpoints: ```Products``` e ```Owners```.

Para acessar a API, é necessário baixar o repositório, instalar as dependências necessárias e rodar a aplicação, usando os seguintes comandos:


```
pip install -r requirements.txt
python manage.py makemigrations storage
python manage.py makemigrations owner
python manage.py migrate
python manage.py runserver
```


O endpoint ```Products``` possibilita todas as quatro principais requisições ```HTTP``` relacionadas a Produtos.
<br>

- ```/products```

| Requisição | Descrição |
| ---------- | --------- | 
| ```GET``` | Retorna todos os produtos cadastrados.  Também é possível informar um código de produto válido/existente, retornando apenas o registro correspondente |
| ```POST``` | Cadastra um novo produto |
| ```PATCH``` | Atualiza um produto já cadastrado. É necessário informar um código de produto válido/existente |
| ```DELETE``` | Exclui um produto cadastrado. É necessário informar um código de produto válido/existente |
<br>

O endpoint ```Owners``` possibilita todas as quatro principais requisições ```HTTP``` relacionadas aos Donos.
<br>

- ```/owners```

| Requisição | Descrição |
| ---------- | --------- | 
| ```GET``` | Retorna todos os donos cadastrados. Também é possível informar um código de dono válido/existente, retornando apenas o registro correspondente |
| ```POST``` | Cadastra um novo dono |
| ```PATCH``` | Atualiza um dono já cadastrado. É necessário informar um código de dono válido/existente |
| ```DELETE``` | Exclui um dono cadastrado. É necessário informar um código de dono válido/existente 
