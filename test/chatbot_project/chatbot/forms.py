from django import forms

PARAGRAPH_CHOICES = [
    (1, '1 paragraph'),
    (2, '2 paragraphs'),
    (3, '3 paragraphs'),
]

TONE_CHOICES = [
    ('formal', 'Formal'),
    ('friendly', 'Friendly'),
    ('professional', 'Professional'),
]

class ChatForm(forms.Form):
    user_input = forms.CharField(label='User Input', max_length=100)
    num_paragraphs = forms.ChoiceField(label='Number of Paragraphs', choices=PARAGRAPH_CHOICES)
    tone = forms.ChoiceField(label='Writing Tone', choices=TONE_CHOICES)
