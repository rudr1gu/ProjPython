# Python aula framework Django

- São Paulo 03 de Agosto de 2024  

- Professor: Leonardo Gabriel

- Criação do Site Html

- Criação de um dicionário de Objetos 

- Instalar framework django
- com este comando ` pip install django`

- caso aconteça um erro atualizar o pip install:
- com este comando ` python.exe -m pip install –upgrade pip`

- verificar os comandos disponíveis
- com este comando `django-admin`

- cria um novo projeto
- com este comando ` django-admin startproject netflix .`

- para acessar o servidor `python manage.py runserver`

- para acessar o aba de admin no python 
`http://127.0.0.1:8000/admin/`

-  Cria uma aba de filmes no projeto
- ` django-admin startapp filme`

- Para realizar migrações, iremos executar dois comandos, um será o makemigrations, para realizar as migrações, e o outro migrate, pra executar as migrações:

- usar este comando ` python manage.py makemigrations`
- usar este comando ` python manage.py migrate`
- usar este comando ` python manage.py createsuperuser`



- iremos trabalhar com três pastas principais:
- filmes
- netflix
- raiz do projeto

- fimes 
-  Em filmes criar um arquivo criar um arquivo ` urls.py `

- netflix 
- Ir netflix em no arquivo ` urls.py` e importar include
-  django importa url e importa path e included 
- como mostra o exemplo abaixo:

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('')
]
```

- abra o terminal, e escreva siga com o comando abaixo, onde será realizado o camando para manipulação de Imagens
- `pip install pillow `

- tupla de tuplas onde onde a primeira será o que vamos utilizar  e a segunda será a visualização do site. 

- deixar o defalut 0 em categorias, após realizar as migrações e aplicar que o sercidor estará funcioando.

- ir ao arquivo `settings.py` 
- ir ao link a seguir ` https://docs.djangoproject.com/en/5.0/howto/static-files/`
- será criado uma nova pasta na Raiz do Projeto
- ` static/css/imagens/js`
- será adicionado url da imagem na netflix 

- adcionar os comandos abaixo no arquivo `urls.py `

```python
 from django.contrib import admin
 from django.urls import path, include
 from django.conf import settings
 from django.conf.urls.static import static
```

```python

urlpatterns = [
    path("admin/", admin.site.urls),
    # incluir urls de filmes
    # path("/", include("filme.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```



