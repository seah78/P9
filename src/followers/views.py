from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from followers.models import UserFollows
from .forms import FollowUsersForm
from authentication.models import User

@login_required
def follow_users(request):
    context = {}
    form = FollowUsersForm()
    if request.method == 'POST':
        follower = request.POST['follower']
        try:
            user = User.objects.get(username__exact=follower)
        except User.DoesNotExist:
            user = None
        
        if user:
            UserFollows.objects.create(user=request.user, followed_user=user)
            return redirect('follow_users')
        
    context['form'] = form
    context['following'] = UserFollows.objects.filter(user__exact=request.user)
    context['followed_by'] = UserFollows.objects.filter(followed_user__exact=request.user)
    return render(request, 'followers/follow_users.html', context)
        
@login_required
def delete_follow(request, user_id):
    user = User.objects.get(id__exact=user_id)
    follow = UserFollows.objects.get(
        user__exact=request.user,
        followed_user__exact=user
    )
    if follow:
        follow.delete()
    return redirect('follow_users')