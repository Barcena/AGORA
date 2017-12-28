from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
 #Friend
from modules.business.models import B2cProfile



    # def get(self, request):
    #     form = HomeForm()
    #     posts = Post.objects.all().order_by('-created')
    #     users = User.objects.exclude(id=request.user.id)
    #     #friend = Friend.objects.get(current_user=request.user)
    #     #friends = friend.users.all()
        
    #     args = {
    #         'form': form, 'posts': posts, 'users': users, # 'friends': friends, 
    #     }
    #     return render(request, self.template_name, args)

    # def post(self, request):
    #     form = HomeForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         post.save()

    #         text = form.cleaned_data['post']
    #         form = HomeForm()
    #         return redirect('home:home')

    #     args = {'form': form, 'text': text}
    #     return render(request, self.template_name, args)


def showB2cHome(request):
    template_name ='home/home.html','base.html'
    queryset=B2cProfile.objects.all()

    context = {
         "object_list":queryset
    }
    return render(request, template_name, context)

'''def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')'''
