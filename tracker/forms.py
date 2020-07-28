from django import forms

from .models import Shot

SHOT_TYPES = [
        ('forehand', 'forehand'),
        ('backhand', 'backhand'),
        ('volley', 'volley'),

    ]

SHOT_LOCATIONS = [
        ('deep left', 'deep left'),
        ('deep right', 'deep right'),
        ('short left', 'short left'),
        ('short right', 'short right'),
    ]

LANDING_SPOTS = [
        ('deep cross', 'deep cross'),
        ('deep line', 'deep line'),
        ('short cross', 'short cross'),
        ('short line', 'short line'),
    ]

IN_OUT = [
        ('in', 'in'),
        ('out', 'out'),
        ('net', 'net'),
    ]


class ShotRecordingForm(forms.ModelForm):
    shot_location = forms.ChoiceField(widget=forms.RadioSelect, choices=SHOT_LOCATIONS)
    shot_type = forms.ChoiceField(widget=forms.RadioSelect, choices=SHOT_TYPES)
    landing_spot = forms.ChoiceField(widget=forms.RadioSelect, choices=LANDING_SPOTS)
    in_out = forms.ChoiceField(widget=forms.RadioSelect, choices=IN_OUT)

    class Meta:
        model = Shot
        fields = [
            'shot_group',
            'shot_location',
            'shot_type',
            'landing_spot',
            'in_out',
        ]
