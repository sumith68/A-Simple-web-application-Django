# Create your views here.
from django.shortcuts import render_to_response
from foods.models import User
from foods.models import recipe

def user(request):
    return render_to_response('user_auth.html')
def user_auth(request):
    name=request.POST['name']
    password=request.POST['word']
    p=User.objects.get(u_name=name)

    if p.p_word==password and p.u_name==name:
        return render_to_response('items.html')
    else:
        return render_to_response('un_authorised.html')
def updation(request):
	ingre=request.POST['ingre']
	photo=request.POST['photo']
	rec=request.POST['rec']
	p=recipe(ingredients=ingre,photo=photo,recipesteps=rec)
	p.save()
	return render_to_response('updated.html')


