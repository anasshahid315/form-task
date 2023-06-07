from django.shortcuts import render, HttpResponseRedirect
from mainApp.models import Country, State, City, Employee
from django.http import JsonResponse

def dataPage(Request):
    data = Employee.objects.all()
    return render (Request, 'data.html', {'data': data})


def get_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse({'states': list(states)})
    
def get_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse({'cities': list(cities)})


def homePage(Request):
    countryId = Request.GET.get('country', None)
    stateId = Request.GET.get('state', None)
    state = None
    district = None
    fields = ('firstname', 'lastname', 'email', 'country', 'state', 'city',  'gender', 'dob','age' )
    if countryId:
        getCountry = Country.objects.get(id=countryId)
        state = State.objects.filter(country=getCountry)
    if stateId:
        getState = State.objects.get(id=stateId)
        city = City.objects.filter(state=getState)
    country = Country.objects.all()
    if(Request.method=="POST"):
        e = Employee()
        e.firstname = Request.POST.get("firstname")
        e.lastname = Request.POST.get("lastname")
        e.email = Request.POST.get("email")
        e.age = Request.POST.get("age")
        e.dob = Request.POST.get("dob")
        e.country = Request.POST.get("country")
        e.city = Request.POST.get("city")
        e.state = Request.POST.get("state")
        e.gender = Request.POST.get("gender")
        e.save()
        return HttpResponseRedirect("/")
    return render(Request, 'home.html', locals())


def deletePage(Request, num):
    data = Employee.objects.get(id= num)
    if(data):
        data.delete()
    return HttpResponseRedirect(Request, 'data.html', {'data': data})



def updatePage(Request, num):
    data = Employee.objects.get(id= num)
    if(data):
        if(Request.method == "POST"):
            
            data.firstname = Request.POST.get("firstname")
            data.lastname = Request.POST.get("lastname")
            data.email = Request.POST.get("email")
            data.age = Request.POST.get("age")
            data.dob = Request.POST.get("dob")
            data.country = Request.POST.get("country")
            data.city = Request.POST.get("city")
            data.state = Request.POST.get("state")
            data.gender = Request.POST.get("gender")
            data.save()
            return HttpResponseRedirect('/')
        return render(Request, "update.html", {'data':data})
    return HttpResponseRedirect("/")