from django import forms
from django import surveyModel

class survey(forms.ModelForm):
    class Meta:
        model = surveyModel
        fields = (
            'name',
            'war_and_peace',
            'immigration',
            'gun_control',
            'crime',
            'drugs',
            'civil_rights',
            'jobs',
            'environment',
            'budget_and_economy',
            'tax_reform',
            'social_security',
            'infrastructure',
            'education',
            'healthcare',
            'abortion',
        )