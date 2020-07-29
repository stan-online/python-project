from django.urls import path
from . import views

app_name = 'api1'
urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/<int:pk>/', views.product_details, name='product_details'),
]


"""
Получить список товаров
GET http://127.0.0.1/api/v1/product/

Создать товар
POST http://127.0.0.1/api/v1/product/     - данные form/json (наименование, цена и.д.)



Получить один товар
GET http://127.0.0.1/api/v1/product/5     - пример запроса

Обновить товар
POST  http://127.0.0.1/api/v1/product/5    - данные form/json (наименование, цена и.д.)
PUT   http://127.0.0.1/api/v1/product/5    - данные form/json (наименование, цена, гарантия) - обновить все

PATCH http://127.0.0.1/api/v1/product/5/name
PATCH http://127.0.0.1/api/v1/product_name/5/ - WRONG!
PATCH http://127.0.0.1/api/v1/product/5/photo_url    - данные form/json (наименование, цена) - обновить не все


Удалить товар
DELETE  http://127.0.0.1/api/v1/product/5
"""