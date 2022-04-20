import datetime

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ['name', 'cost', 'solar_field_cost', 'bop_cost', 'construction_cost', 'mobility_cost', 'storage_cost']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['num_colect'].initial = 40
        self.fields['vol_storage'].initial = 0
        self.fields['integration'].initial = "SL_S_PD"
        self.fields['fluid'].initial = "steam"
        self.fields['dist_supply'].initial = 20
        self.fields['surface'].initial = "cubierta de hormigón"
        self.fields['transport'].initial = "ship"
        self.fields['distance'].initial = 400
        self.fields['pressure'].initial = 8
        self.fields['real_offer'].initial = False
        self.fields['pub_date'].initial = datetime.date.today

