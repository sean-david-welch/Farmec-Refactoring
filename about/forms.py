from farmec.forms import CustomModelForm
from .models import Employee, Timeline, Term, Privacy

class EmployeeForm(CustomModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class TimelineForm(CustomModelForm):
    class Meta:
        model = Timeline
        fields = '__all__'

class TermForm(CustomModelForm):
    class Meta:
        model = Term
        fields = '__all__'

class PrivacyForm(CustomModelForm):
    class Meta:
        model = Privacy
        fields = '__all__'