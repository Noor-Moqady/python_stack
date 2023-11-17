from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

def ninja_gold_page(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        request.session['attempts'] = 0

    context = {
        'gold': request.session['gold'],
        'activities': request.session['activities']
    }
    return render(request, 'ninja_gold.html', context)



def process_money(request, location=""):

    if request.method == 'POST':
        if request.POST['which_form'] == 'farm':
            request.session['attempts'] += 1 
            request.session['earned_gold']= random.randint(2,5)
            request.session['gold'] += request.session['earned_gold']
            if request.session['attempts'] == 5 and request.session['gold'] < 40 :
                request.session['messeage'] = 'You Lost'
                x = 'Lost'
            if request.session['attempts'] < 5 and request.session['gold'] >= 40:
                request.session['messeage'] = 'You Win'
                x = 'earned'

            request.session['activities'].append(f"Earned {request.session['earned_gold']} gold from farm, ({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        elif request.POST['which_form'] == 'cave':
            request.session['attempts'] += 1
            request.session['earned_gold']= random.randint(5,10)
            request.session['gold'] += request.session['earned_gold']
            if request.session['attempts'] == 5 and request.session['gold'] < 40 :
                request.session['messeage'] = "You Lost"
            if request.session['attempts'] < 5 and request.session['gold'] >= 40:
                request.session['messeage'] = "You Win"
            request.session['activities'].append(f"Earned {request.session['earned_gold']} gold from cave, ({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        elif request.POST['which_form'] == 'house':
            request.session['attempts'] += 1
            request.session['earned_gold']= random.randint(10,20)
            request.session['gold'] += request.session['earned_gold']
            if request.session['attempts'] == 5 and request.session['gold'] < 40 :
                request.session['messeage'] = "You Lost"
            if request.session['attempts'] < 5 and request.session['gold'] >= 40:
                request.session['messeage'] = "You Win"
            request.session['activities'].append(f"Earned {request.session['earned_gold']} gold from house, ({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        elif request.POST['which_form'] == 'quest':
            request.session['attempts'] += 1
            request.session['earned_gold']= random.randint(-50,50)
            request.session['gold'] += request.session['earned_gold']
            if request.session['attempts'] == 5 and request.session['gold'] < 40 :
                request.session['messeage'] = "You Lost"
            if request.session['attempts'] < 5 and request.session['gold'] >= 40:
                request.session['messeage'] = "You Win"
            if int(request.session['earned_gold']) < int(0):
                x = 'Lost'
            else :
                x = 'Earned'
            request.session['activities'].append(f"{x} {request.session['earned_gold']} gold from quest, ({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        return redirect('/')
    else:
        if location == 'farm':
            request.session['attempts'] += 1
            request.session['earned_gold']= random.randint(2,5)
            request.session['gold'] += request.session['earned_gold']
            if request.session['attempts'] == 5 and request.session['gold'] < 40 :
                request.session['messeage'] = "You Lost"
            if request.session['attempts'] < 5 and request.session['gold'] >= 40:
                request.session['messeage'] = "You Win"
            request.session['activities'].append(f"Earned {request.session['earned_gold']} gold from farm, ({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        elif location == 'cave':
            request.session['attempts'] += 1
            request.session['earned_gold']= random.randint(5,10)
            request.session['gold'] += request.session['earned_gold']
            if request.session['attempts'] == 5 and request.session['gold'] < 40 :
                request.session['messeage'] = "You Lost"
            if request.session['attempts'] < 5 and request.session['gold'] >= 40:
                request.session['messeage'] = "You Win"
            request.session['activities'].append(f"Earned {request.session['earned_gold']} gold from cave, ({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        elif location == 'house':
            request.session['attempts'] += 1
            request.session['earned_gold']= random.randint(10,20)
            request.session['gold'] += request.session['earned_gold']
            if request.session['attempts'] == 5 and request.session['gold'] < 40 :
                request.session['messeage'] = "You Lost"
            if request.session['attempts'] < 5 and request.session['gold'] >= 40:
                request.session['messeage'] = "You Win"
            request.session['activities'].append(f"Earned {request.session['earned_gold']} gold from house, ({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        elif location == 'quest':
            request.session['attempts'] += 1
            request.session['earned_gold']= random.randint(-50,50)
            request.session['gold'] += request.session['earned_gold']
            if request.session['attempts'] == 5 and request.session['gold'] < 40 :
                request.session['messeage'] = "You Lost"
            if request.session['attempts'] < 5 and request.session['gold'] >= 40:
                request.session['messeage'] = "You Win"
            if int(request.session['earned_gold']) < int(0):
                x = 'Lost'
            else :
                x = 'Earned'
            request.session['activities'].append(f"{x} {request.session['earned_gold']} gold from quest, ({strftime('%Y-%m-%d %H:%M %p', gmtime())})")

        return redirect('/')


def reset(request):
    request.session.flush()
    return redirect ('/')