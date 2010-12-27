from models import Note, NoteForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    
    if request.method == 'GET':        
        object_list = Note.objects.filter(user=request.user).order_by('order', '-id')
        return direct_to_template(request, 'note/list.html', {'object_list': object_list})
    return HttpResponseRedirect(reverse(index))

@login_required
def new(request):
    
    if request.method == 'GET':        
        form = NoteForm()
    elif request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.order = 0
            note.save()
            return HttpResponseRedirect(reverse(index))
            
    return direct_to_template(request, 'note/details.html', {'form': form})

@login_required
def delete(request):
    
    if request.method == 'POST':
        note = get_object_or_404(Note, pk=request.POST.get('note_id', '0'), user=request.user)
        note.delete()
        
    return HttpResponseRedirect(reverse(index))

@login_required
def update(request, id):    
    note = get_object_or_404(Note, pk=id, user=request.user)
    
    if request.method == 'GET':
        form = NoteForm(model_to_dict(note))
    elif request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(index))        
        
    return direct_to_template(request, 'note/details.html', {'form': form, 'note_id': note.id})

