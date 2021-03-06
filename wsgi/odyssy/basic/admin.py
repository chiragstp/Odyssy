from django.contrib import admin
from .models import PhotoExtended

from photologue.admin import PhotoAdmin as PhotoAdminDefault
from photologue.models import Photo


class PhotoExtendedInline(admin.StackedInline):
    model = PhotoExtended
    can_delete = False


class PhotoAdmin(PhotoAdminDefault):
    actions = ['set_active_image', 'remove_active_image']
    inlines = [PhotoExtendedInline, ]

    def set_active_image(self, request, queryset):
        queryset.update(is_public=True)

    def remove_active_image(self, request, queryset):
        queryset.update(is_public=False)

    set_active_image.short_description = "Show them on index page"
    remove_active_image.short_description = "Remove them from index page"


admin.site.unregister(Photo)
admin.site.register(Photo, PhotoAdmin)
