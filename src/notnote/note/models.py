from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import User
from django import forms

class Note(models.Model):
    blank_msg = 'but not an empty note!'
    
    text = models.TextField(blank=True) # prevents the default error message and handle validation in other place
    order = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    
    def title(self):
        """
        >>> n = Note()
        >>> n.text = '''Here it goes line 1
        ... and then comes line 2
        ... finally - line 3'''
        >>> n.title()
        'Here it goes line 1'
        >>> n.text = "here we type a lot of characters to test whether it trunkates correct - after the 24th char :-)"
        >>> n.title()
        'here we type a lot of ch...'
        >>> n.text = '''   
        ...      line starts here     
        ...        '''
        >>> n.title()
        'line starts here'
        """
        MAX_LEN = 24
        
        text = self.text.strip().split('\n')[0]
        if len(text) > MAX_LEN:
            title = text[:MAX_LEN] + '...'
        else:
            title = text
             
        return title
    
class NoteForm(forms.ModelForm):
    
    def clean_text(self):
        if not self.cleaned_data['text'].strip():
            raise ValidationError(Note.blank_msg)
        return self.cleaned_data['text']
    
    class Meta:
        model = Note
        exclude = ('order', 'user')
        
        
        