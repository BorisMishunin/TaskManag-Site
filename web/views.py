from django.shortcuts import render, redirect
from web.models import tasks, users_param, TASKS_STATUSES
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import auth
from django.core.paginator import Paginator
from forms import TasksForms

def index(request):
    sel_t = tasks.objects.order_by('title')
    sel_u = users_param.objects.order_by('user')
    params = {}
    params.update(csrf(request))
    params['tasks'] = sel_t
    params['users'] = sel_u
    params['statuses'] = TASKS_STATUSES
    params['user_fl'] = []
    params['statuses_fl'] = []
    params['username'] = auth.get_user(request).username
    params['authinfo'] =''

    if ("user_fl" in request.session):
        params['user_fl'] = request.session['user_fl']
    if ("statuses_fl" in request.session):
        params["statuses_fl"] = request.session["statuses_fl"]

    if ("authinfo" in request.session):

        if request.session['authinfo']=='ok':
            user = auth.get_user(request)
            params['user_fl'].append(user.pk)
        else:
            params['authinfo'] = request.session['authinfo']
        request.session['authinfo'] = ''

    print params['user_fl']
    return render(request, 'web/index.html', params)

def save_task(request):
    if request.method == 'POST':
        form = TasksForms(request.POST)
        if form.is_valid():
            new_task =  form.save()
            new_task.save()
    return redirect('/')

@csrf_exempt
def edit_task(request):
    if request.method == 'POST':
        values = str(request.POST.get('value')).split(':')
        task = tasks.objects.get(id=values[1])
        if values[0] == '0':
            print values
            task.user = User.objects.get(id=values[2])
        else:
            task.statuses = values[2]
        task.save()
        return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')

def add_new_task(request):
    params = {}
    params.update(csrf(request))
    params['form'] = TasksForms
    return render(request, 'web/task_form.html', params)


@csrf_exempt
def show_tasks(request):
    if request.method == 'POST':

        users_id =  str(request.POST.get('users')).split(':')[1:]
        statuses_id =  str(request.POST.get('statuses')).split(':')[1:]
        page_number = request.POST.get('current_page')
        page_number = int(page_number) if page_number!=None else request.session['current_page']  if ("current_page" in request.session) else 1
        request.session['current_page'] = page_number
        sel_t = tasks.objects.all()
        request.session['user_fl']=[]
        if len(users_id)>0:
            sel_t = sel_t.filter(user__in=users_id)
            request.session['user_fl'] = map(int,users_id)
        request.session['statuses_fl']=[]
        if len(statuses_id)>0:
            sel_t = sel_t.filter(statuses__in=statuses_id)
            request.session['statuses_fl'] = map(int,statuses_id)
        sel_u = users_param.objects.order_by('user')
        params = {}
        params.update(csrf(request))
        params['tasks'] = Paginator(sel_t, 20).page(page_number)
        params['users'] = sel_u
        params['statuses'] = TASKS_STATUSES

        html = render_to_string('web/main_table.html', params)
        return HttpResponse(html, content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')