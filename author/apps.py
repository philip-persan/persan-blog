from django.apps import AppConfig


class AuthorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'author'

    def ready(self, *args, **kwargs) -> None:
        import author.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready
