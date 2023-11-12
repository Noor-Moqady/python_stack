from django.shortcuts import render, redirect

def display_form(request):
    return render(request, "Dojo_Survey.html")

def handel_form(request):
        
    request.session['x']= request.POST['name']
    request.session['y']= request.POST['Dojo Location']
    request.session['z']= request.POST['favorite language']
    request.session['w']= request.POST['comment']
    request.session['f']= request.POST['gender']
    request.session['n'] = "Yes" if 'email_updates' in request.POST else "No"

    return redirect("/show_result")
def show(request):
    return render(request,'submit_info.html')
