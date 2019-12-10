from django.contrib import admin
from p_library.models import Book, Author, PubHouse


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    @staticmethod
    def pubhouse_name(obj):
        return obj.pubhouse.name

    list_display = ('title', 'author_full_name', 'pubhouse_name', )
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'pubhouse')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country')
    fields = ('full_name', 'birth_year', 'country')


@admin.register(PubHouse)
class PubHouseAdmin(admin.ModelAdmin):
    list_display = ('name', )




    