from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleScope, Scope

from collections import Counter


class ArticleScopeInlineFormset(BaseInlineFormSet):

    def clean(self):
        count_base_scope = Counter()
        for form in self.forms:
            if form.cleaned_data.get('base_scope'):
                count_base_scope['base_scope'] += 1
        if count_base_scope['base_scope'] > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif count_base_scope['base_scope'] == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleScopeInline
    ]


@admin.register(Scope)
class ScopesAdmin(admin.ModelAdmin):
    pass