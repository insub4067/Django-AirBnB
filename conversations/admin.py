from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """Conversation Admin Definition"""

    pass
