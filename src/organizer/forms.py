from django import forms 

from .models import Tag, Startup


class SlugCleanMixin:
    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if slug == 'create':
            return forms.ValidationError("Slug may not be 'create'.")
        return slug


class LowerCaseNameMixin:
    def clean_name(self):
        return self.cleaned_data['name'].lower()


class TagForm(LowerCaseNameMixin, forms.ModelForm):
    class Meta:
        model = Tag 
        fields = '__all__'

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if slug == 'create':
            return forms.ValidationError("Slug may not be 'create'.")
        return slug

    def save(self):
        return Tag.objects.create(
            name=self.cleaned_data['name'],
            slug=self.cleaned_data['slug'],
        )


class StartupForm(LowerCaseNameMixin, SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'
