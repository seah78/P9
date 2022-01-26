from django import forms


class FollowUsersForm(forms.Form):
    follower = forms.CharField(max_length=100)
