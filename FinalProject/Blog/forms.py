from django import forms

class Post (forms.Form):
    author = forms.CharField(max_length=50)
    title = forms.CharField(max_length =100)
    subtitle = forms.CharField(max_length=50)
    img = forms.ImageField()
    post = forms.CharField(max_length=4000, widget=forms.Textarea(attrs={"rows": 12}))

class ChatForm (forms.Form):
    chat = forms.CharField(max_length=400)

