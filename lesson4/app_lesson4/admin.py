from django.contrib import admin
from .models import Advertisment

# Register your models here.
class AdvertismentAdmin(admin.ModelAdmin):
        list_display = ["id","title","description","price","created_at","auction"]
        list_filter = ["auction","created_at"]
        actions = ["make_auction_as_false","make_auction_as_true"]
        fielosets=[]



        @admin.action(description="Убрать возможность торга")
        def make_auction_as_false(self,request, queryset):
                queryset.update(auction=False)

        @admin.action(description="Добавить возможность торга")
        def make_auction_as_true(self, request, queryset):
                queryset.update(auction=True)


admin.site.register(Advertisment,AdvertismentAdmin)