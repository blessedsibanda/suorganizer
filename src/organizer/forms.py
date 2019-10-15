from django import forms 

from .models import Tag


class TagForm(forms.Form):
    name = forms.CharField(max_length=31)
    sug = forms.SlugField(
        help_text='A label for URL config',
        max_length=31,
        required=False,
    )

    def clean_name(self):
        return self.cleaned_data['name'].lower()

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
