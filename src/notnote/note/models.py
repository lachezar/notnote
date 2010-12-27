from django.db import models
from django.contrib.auth.models import User
from django import forms

class Note(models.Model):
    text = models.TextField()
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
        ...    line starts here   
        ...    '''
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
    
    class Meta:
        model = Note
        exclude = ('order', 'user')
        