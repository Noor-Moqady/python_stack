from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt


def login_registration(request):

    return render(request,'index.html')

def main(request):
    if 'user_id' in request.session:
        list=[]
        this_user=User.objects.get(id=request.session['user_id'])
        for friend in this_user.allfriends.all():
            list.append(friend.id)
        context={
            'user':this_user,
            'allpost':Post.objects.all(),
            'allphoto':Image.objects.all(),
            'alluser':User.objects.all(),
            'user_friends_list':list
        }
        return render(request,'feed.html',context)
    else:
        return redirect ('/')


def registre_proccess(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hash1= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        registered_user = User.objects.create(
            first=request.POST['fname'],
            last=request.POST['lname'],
            email=request.POST['email'],
            password=hash1,
            dob=request.POST['dob'],
            gender=request.POST['gender']
            )
        messages.success(request, "Registered successfully")
        request.session['user_id']=registered_user.id
        request.session['user_name']=registered_user.first
        return redirect('/FLEXBOOK')

def login_proccess(request):
    user = User.objects.filter(email=request.POST['lemail'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['lpassword'].encode(), logged_user.password.encode()):
                request.session['user_id']=logged_user.id
                request.session['user_name']=logged_user.first
                messages.success(request, "Login successfully")
                return redirect('/FLEXBOOK')
    else:
        messages.error(request,'Invalid authentication')
        return redirect ('/')

def post(request):
    this_user=User.objects.get(id=request.session['user_id'])
    this_post=Post.objects.create(
        desc=request.POST['post_desc'],
        posted_by=this_user
    )
    filepath = request.FILES.get('img', False)
    this_image=Image.objects.create(
        photo=filepath,
        uploaded_by=this_user,
        related_post=this_post
    )
        
    return redirect('/FLEXBOOK')

def comment(request,id):
    this_user=User.objects.get(id=request.session['user_id'])
    this_post=Post.objects.get(id=int(id))
    this_comment=Comment.objects.create(
        desc=request.POST['comment_desc'],
        commented_by=this_user,
        related_post=this_post,
    )
    return redirect('/FLEXBOOK')

def change(request):
    return render(request,'change.html')

def update(request):
    this_user=User.objects.get(id=request.session['user_id'])
    this_user.avatar=request.FILES['avatar']
    this_user.save()
    return redirect('/FLEXBOOK')

def like(request,id):
    this_user=User.objects.get(id=request.session['user_id'])
    this_post=Post.objects.get(id=int(id))
    this_post.liked_by.add(this_user)
    return redirect('/FLEXBOOK')

def control(request):
    if 'user_id' in request.session:
        context={
            'account':User.objects.all()
        }
        return render(request,'control.html',context)
    else:
        return redirect ('/')

def control_del(request,id):
    this_user=User.objects.get(id=int(id))
    this_user.delete()
    return redirect('/control')

def add_friend(request,id):
    re_user=User.objects.get(id=request.session['user_id'])
    add_user=User.objects.get(id=int(id))
    if re_user.this_user.all:
        this_friend=Friend.objects.create(
            user=re_user, 
        )
        this_friend.friends.add(add_user)
    else:
        this_friend=Friend.objects.filter(user=re_user)
        this_friend.friends.add(add_user)
    return redirect('/FLEXBOOK')


def delete_post(request,id):
    this_post=Post.objects.get(id=int(id))
    this_post.delete()
    return redirect('/FLEXBOOK')

def delete_comment(request,id):
    this_comment=Comment.objects.get(id=int(id))
    this_comment.delete()
    return redirect('/FLEXBOOK')

def logout(request):
    request.session.flush()
    return redirect ('/')

# def upload_file(request):
#     context={
#         'alluser':User.objects.all()
#     }
        
#     return render(request,'index.html',context)

# def porcces(request):
#     this_user=User.objects.create(
#         name=request.POST['name'],
#         desc=request.POST['desc'],
#         photo=request.FILES['img']
#     )
#     return redirect('/')