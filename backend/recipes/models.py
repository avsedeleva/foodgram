from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    color = models.CharField(
        verbose_name=('Цветовой HEX-код'),
        max_length=7,
        help_text=('Цветовой HEX-код (например, #49B64E)'
    ))
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=50
    )
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения',
        max_length=50
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        null=True
    )

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='recipes/'
    )
    text = models.TextField(
        verbose_name='Текстовое описание'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        related_name= 'recipes'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        related_name= 'recipes'
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления'
    )

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name
