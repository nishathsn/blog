from django import forms

from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Blog.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is taken.")

class BlogFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data #dictonary
    #     print("cleaned_data", cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "pathan trailer":
    #         raise forms.ValidationError('the title is taken.')
    #     print("title", title)
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "pathan trailer":
            self.add_error('title', 'this title is taken')
            #raise forms.ValidationError('the title is taken.')
        if "trailer" in content or "trailer" in title.lower():
            self.add_error('content', "trailer cannot be in content")
            raise forms.ValidationError("trailer is not allowed")
        return cleaned_data