from django.views.generic import create_update
from django.http import QueryDict

def create_object_with_current_user(request, model=None, template_name=None,
        template_loader=create_update.loader, extra_context=None, post_save_redirect=None,
        login_required=False, context_processors=None, form_class=None):
    
    original = request.POST
    new = dict(request.POST)
    #new['user'] = request.user
    new['user'] = str(request.user.id)
    request.POST = QueryDict(new) 
    
    response = create_update.create_object(request, model, template_name, 
      template_loader, extra_context, post_save_redirect, login_required, 
      context_processors, form_class)
    
    request.POST = original
    
    return response

