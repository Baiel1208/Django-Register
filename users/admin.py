from django.contrib import admin


from . import models as m

# Register your models here.
# admin.site.register(m.User)

@admin.register(m.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )


@admin.register(m.EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created', )