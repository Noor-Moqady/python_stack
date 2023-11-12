from django.shortcuts import render,redirect

def counter(request):
    
    if  'count' not in request.session:
        request.session['count']=1
        
    else:
        request.session['count']+=1

    return render(request,'counter.html')
def counter2(request):
    
    if  'count' not in request.session:
        request.session['count']=1
    else:
        request.session['count']+=2

    return render(request,'counter.html')
def reset(request):
    request.session.clear()
    return redirect ('/visits')
def delete(request):
    request.session.pop('count')
    return redirect ('/visits')