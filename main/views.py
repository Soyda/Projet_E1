from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TestForm, FileFieldForm
from django.views.generic.edit import FormView
from django.template.defaulttags import register
from django.urls import reverse_lazy
import requests
import pandas as pd
import os
from django.utils.html import mark_safe

URL_API = "http://host.docker.internal:8080"

@register.filter # pour pouvoir utiliser range dans le template
def get_range(start=0,value=0):
    return range(start,value)

# Create your views here.

@login_required
def login_required_view(request):
    response = requests.get(URL_API).json()
    return render(request, 'main/login_required_page.html', {'response': response})

def test_form(request):
    fm = TestForm(request.POST)
    if request.method =="POST":
        if fm.is_valid():
            print("name:",fm.cleaned_data["name"]) #// request.POST["name"]
            print("email:",fm.cleaned_data['email'])
            return render(request,'main/test_form_done.html',{'name':fm.cleaned_data["name"],
                                                            'email':fm.cleaned_data['email'],
                                                            'loop': fm.cleaned_data['loop']})
    fm = TestForm()
    return render(request,'main/test_form.html', {'form':fm})

# @login_required
# def add_file(request):
#     pass
# from django.views.generic.edit import FormView
# from .forms import FileFieldForm

class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'main/add_file.html'  # Replace with your template.
    success_url = reverse_lazy('main:add_file_done')  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            uploaded_files = []

            for f in files:
                    # Get the file extension
                _, file_extension = os.path.splitext(f.name)

                # Read the first 4 rows of the file using pandas
                if file_extension.lower() in ['.csv']:
                    df = pd.read_csv(f, nrows=4, header=None)
                elif file_extension.lower() in ['.xls', '.xlsx']:
                    df = pd.read_excel(f, nrows=4, header=None, engine='openpyxl')
                    date_column = df.select_dtypes(include=['datetime64']).columns
                    df[date_column] = df[date_column].astype(str)
                else:
                    continue  # Skip unsupported file types

                # Convert the DataFrame to a list of lists
                first_4_rows = df.values.tolist()

                # Save the file and store the file name and the first 4 rows in the session
                uploaded_files.append({'name': f.name, 'first_4_rows': first_4_rows})

            # Store the file names and the first 4 lines in the session
            self.request.session['uploaded_files'] = uploaded_files

            return super().form_valid(form)
        else:
            return self.form_invalid(form)

@login_required
def add_file_done(request):
    file_names = request.session.get('uploaded_files', [])
    return render(request, 'main/add_file_done.html', 
                    {'file_names': file_names})

    
@login_required
def see_verbatims(request):
    response = requests.get(f"{URL_API}/verbatims/").json()
    # response = requests.get(f"{URL_API}/structures/").json()
    df_html = mark_safe(pd.DataFrame(response).to_html())
    return render(request, 'main/see_verbatims.html', {'df_html': df_html})

@login_required
def stats_verbatims(request):
    pass