# Пример использования
В качестве параметра в пути мы задаем ID пользователя.  
В качестве дополнительного параметра указываем last_days, чтобы указать необходимое количество дней.  
http://localhost:8000/ordered-products/<int:customer_id>/?last_days=<int:days>  

Примеры URL:  
http://localhost:8000/ordered-products/1/?last_days=7  
http://localhost:8000/ordered-products/2/?last_days=30  
http://localhost:8000/ordered-products/3/?last_days=365

# Пример добавления продукта
http://localhost:8000/create-product/  

# Пример просмотра продукта
http://localhost:8000/product/26/
Не заморачивался с версткой, взял готовую карточку товара из bootstrap.