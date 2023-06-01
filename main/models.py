from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=125, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'


class Post(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    title = models.CharField(max_length=125, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    author = models.CharField(max_length=125, verbose_name='Имя автора')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')
    location = models.CharField(max_length=125, verbose_name='Место сьемки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self) -> str:
        return f"{self.title} | {self.category} | {self.author}"
    
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикаций'
    
    

