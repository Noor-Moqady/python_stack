from django.shortcuts import render, redirect
import random
def start(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 10)
        request.session['attempts'] = 0
        request.session['message'] ='Guess a number between 1 and 100.'
    
    return render(request,'great_number.html')
def guess(request):
    request.session['attempts'] +=1
    request.session['guess'] = request.POST['guess']

    if int(request.POST['guess']) < int(request.session['number']):
        request.session['message'] = 'low'
        request.session['win'] = False

    elif int(request.POST['guess'])  > int(request.session['number']):
        request.session['message'] = 'high'
        request.session['win'] = False
    else:
        request.session['message'] = f'Congratulations! You guessed the number {request.session["number"]} in {request.session["attempts"]} attempts.'
        request.session['win'] = True
    
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
def handel(request):
    request.session['x']= request.POST['win_name']
    
    return redirect ('/show')
def show(request):
    return render(request,'show.html')

