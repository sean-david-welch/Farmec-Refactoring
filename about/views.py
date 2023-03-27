from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . models import Employee, Timeline, Term, Privacy
from . forms import EmployeeForm, TimelineForm, TermForm, PrivacyForm

models = {
    'employee': Employee,
    'timeline': Timeline,
    'term': Term,
    'privacy': Privacy,
}

forms = {
    'employee': EmployeeForm,
    'timeline': TimelineForm,
    'term': TermForm,
    'privacy': PrivacyForm,
}

#######################################################
#################### About Views ######################
#######################################################
def about(request):
    employees = Employee.objects.all()
    timelines = Timeline.objects.all()

    context = {'employees': employees, 'timelines': timelines}
    return render(request, 'about/about.html', context)

def terms(request):
    terms = Term.objects.all()

    context = {'terms': terms}
    return render(request, 'about/terms.html', context)

def privacy(request):
    privacy = Privacy.objects.all()

    context = {'privacy': privacy}
    return render(request, 'about/privacy.html', context)

#######################################################
################# About Models C.R.U.D. ###############
#######################################################

def create_model_about(request, model_name):
    form_class = forms[model_name]

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('about')
    else:
        form = form_class()

    context = {'form': form, 'model_name': model_name}
    return render(request, 'model_form.html', context)

def edit_model_about(request, model_name, pk):
    model = models[model_name].objects.get(id=pk)
    form_class = forms[model_name]
    form = form_class(instance=model)

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
            return redirect('about')
        
    context = {'form': form, 'model_name': model_name}
    return render(request, 'model_form.html', context)

def delete_model_about(request, model_name, pk):
    model = models[model_name].objects.get(id=pk)
    
    if request.method == 'POST':
        model.delete()
        return redirect('about')
    
    context = {'object': model}
    return render(request, 'delete_model.html', context)

