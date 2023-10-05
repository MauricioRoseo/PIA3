from datetime import datetime
from django import forms
from forum.models import Post


class PostModelForm(forms.ModelForm):
    error_css_class = "alert-danger"

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields["pub_date"].initial = datetime.today()

    def clean(self):
        cleaned_data = super().clean()
        pub_date = cleaned_data.get("pub_date")
        pub_date = pub_date.replace(tzinfo=None)

        if pub_date > datetime.today():
            self.add_error(
            "pub_date", forms.ValidationError("Não é permitido datas futuras")
            )

    class Meta:
        model = Post
        fields = ('post_title', "body_text", "pub_date")
        widgets = {
            "pub_date": forms.widgets.DateInput(attrs={"type": "date"}),
        }
        labels = {"body_text": "",}