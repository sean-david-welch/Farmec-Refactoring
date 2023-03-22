from farmec.forms import CustomModelForm
from .models import Supplier, Machine, Product, Video

class SupplierForm(CustomModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class MachineForm(CustomModelForm):
    class Meta:
        model = Machine
        fields = '__all__'

class ProductForm(CustomModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class VideoForm(CustomModelForm):
    class Meta:
        model = Video
        fields = '__all__'