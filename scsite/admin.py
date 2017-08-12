from django.contrib import admin
from .models import Branch, Track, Team, Faq, News, Job, Event, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

admin.site.register((Branch, Track, Team, Faq, News, Job, Event, Profile))

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('is_superuser', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'get_branch')
    list_select_related = ('profile', )

    def get_branch(self, instance):
        return instance.profile.main_branch
    get_branch.short_description = 'Branch'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)