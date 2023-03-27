from farmec.forms import CustomModelForm
from . models import Blog, Exhibition

class BlogForm(CustomModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class ExhibitionForm(CustomModelForm):
    class Meta:
        model = Exhibition
        fields = '__all__'
    