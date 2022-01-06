from django.shortcuts import render, redirect

from .forms import FollowUsersForm

@login_required
def follow_users(request):
    form = FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('flux')
    return render(request, 'followers/follow_users.html', context={'form': form})