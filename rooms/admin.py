from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.HouseRule, models.Facility, models.Amenity)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Custom Photo Admin"""

    pass


# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Custom Room Admin"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "host",
                    "description",
                    "country",
                    "city",
                    "price",
                    "address",
                )
            },
        ),
        (
            "Time",
            {
                "fields": (
                    "check_in",
                    "check_out",
                )
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "beds",
                    "baths",
                    "bedroooms",
                )
            },
        ),
        (
            "More about space",
            {
                "fields": (
                    "room_type",
                    "amenities",
                    "house_rules",
                    "facilities",
                )
            },
        ),
    )

    ordering = ("created",)

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "baths",
        "bedroooms",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "host__superhost",
        "instant_book",
        "room_type",
        "amenities",
        "house_rules",
        "facilities",
        "country",
        "city",
    )

    search_fields = (
        "city",
        "host__username",
    )

    filter_horizontal = (
        "amenities",
        "house_rules",
        "facilities",
    )
