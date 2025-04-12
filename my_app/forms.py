from django import forms
from .models import Card, Lesson

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['word', 'translation', 'image', 'lesson']

    def clean_word(self):
        word = self.cleaned_data['word']
        if not word:
            raise forms.ValidationError("Word cannot be empty")
        return word

    def clean_translation(self):
        translation = self.cleaned_data['translation']
        if not translation:
            raise forms.ValidationError("Translation cannot be empty")
        return translation

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name:
            raise forms.ValidationError("Lesson name cannot be empty")
        return name