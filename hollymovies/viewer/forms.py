from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import Profile

class SignUpForm(UserCreationForm):

  class Meta(UserCreationForm.Meta):
    fields = ['username']

  def save(self, commit=True):
    self.instance.is_active = True

    saved_user = super().save(commit)

    simple_group = Group.objects.get(name='simple')
    saved_user.groups.add(simple_group)
    saved_user.save()

    new_profile = Profile.objects.create(user=saved_user)

    return saved_user