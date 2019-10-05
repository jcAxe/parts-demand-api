# Olá, seja bem-vindo ao projeto da Federação de Comércio!!

O desenvolvimento está usando como linguagem o Python versão: 3.6.8
As importações necessárias para o desenvolvimento são:

* Django, django versão: 2.2.5
* Postgres para python, psycopg2 versão: 2.8.3
* Django Rest Framework, djangorestframework versão: 3.10.3

Mas não se preocupe que tudo está organizado no Dockerfile!

Juntamente com o este repositório, serão fornecidos arquivos auxiliares contendo os valores necessários e sugeridos das variáveis de ambiente utilizadas no projeto.


## Rodando o projeto

Todo o processo e comandos serão realizados a partir da raiz do projeto.


Antes de mais nada, substitua os placeholders das variáveis de ambiente indicadas dentro do Dockerfile que está localizado na raiz do projeto.

Vamos buildar e rodar o container. Na linha de comando, digite:
```
sudo docker-compose build
sudo docker-compose up
```
Vamos realizar as migrações da base de dados dentro do container para garantir que tudo está no seu devido lugar. Na linha de comando, digite:
```
sudo docker-compose exec web python federation_commerce/manage.py makemigrations
sudo docker-compose exec web python federation_commerce/manage.py migrate
```
Certo, agora o projeto deve estar rodando no seu localhost na porta padrão do django, a porta 8000.

Para acessarmos completamente o sistema devemos estar autenticados. Então, devemos criar os usuários propostos: Administrador e Anunciante.
Por simplicidade, criaremos ambos os usuários em modo "superuser".
Na linha de comando, digite:
```
sudo docker-compose exec web python federation_commerce/manage.py createsuperuser
```
Será pedido um nome de usuário, email e senha. Você pode ignorar o e-mail ao apertar enter com o campo vazio.
Coloque o username como: Administrador
A senha pode ser qualquer uma, só lembre dela para acessar a plataforma.

Agora, vamos criar o Anunciante:
```
sudo docker-compose exec web python federation_commerce/manage.py createsuperuser
```

Sugerimos o username como: Anunciante
A senha pode ser qualquer uma, só lembre dela para acessar a plataforma.



Certo, agora a api, a plataforma e o admin devem estar acessíveis.
Embora as interações possam ser feitas pelo Postman, no browser é possivel:

Ver todas as demandas criadas até o momento em:
>```localhost:8000/demands/```

Ver, editar ou deletar uma demanda específica, adicionando uma id ao fim da url: (substitua o id pelo número da demanda desejada)
>```localhost:8000/demands/"id"```

Também, para concluir o estado de finalização, basta adicionar a palavra "close" no fim da url:
>```localhost:8000/demands/"id"/close ```

Demandas são criadas com seu estado de conclusão **Falso** como padrão, em caso deste valor não ser especificado.
Após acessar este endpoint, o estado de conclusão da demanda será modificado para **Verdadeiro**.

## Acessando os endpoints pelo Postman

Ao importar a collection localizada na pasta postman_requests, três variáveis de ambientes estão definidas: "url", "usr", "password". Os valores de testes dependem do seu ambiente.
**url**: seu localhost
**usr**: Administrador ou Anunciante
**password**: respectivas senhas de Administrador e Anunciante

A autenticação de cada resquest utiliza os valores de autenticação definidos na collection.

