from django import forms

class TestForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput) #// this is a hidden field to catch bots
    # #// this is a validator to catch bots
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
    loop = forms.IntegerField()

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


structures_list = [
    ('1', 1),
    ('2', 2),
    ('10', 10),
]
type_client_list = [
    ('particulier', 'Particulier'),
    ('professionnel', 'Professionnel')
]

class DateInput(forms.DateInput):
    input_type = 'date'

class VerbatimForm(forms.Form):
    date = forms.DateField(widget=DateInput())
    type_client = forms.ChoiceField(
        # required=False,
        choices=type_client_list      
        
    )
    structure = forms.ChoiceField(
        # required=False,
        choices=structures_list
              
    )
    text = forms.CharField(widget=forms.Textarea)