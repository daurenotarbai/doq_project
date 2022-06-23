from django.contrib import admin


class HiddenAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}  # Hide model in admin list


class NoAddMixin:
    def has_add_permission(self, request, obj=None):
        return False


class NoChangeMixin:
    def has_change_permission(self, request, obj=None):
        return False


class NoDeleteMixin:
    def has_delete_permission(self, request, obj=None):
        return False


class NoViewMixin:
    def has_view_permission(self, request, obj=None):
        return True


class OnlySuperUserMixin:
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser


class ReadOnlyMixin(NoAddMixin, NoChangeMixin, NoDeleteMixin):
    pass
