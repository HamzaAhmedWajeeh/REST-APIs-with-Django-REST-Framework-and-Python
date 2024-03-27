from django.contrib import admin

from watchlist_app.models import WatchList, StreamingPlatform, Reviews

admin.site.register(WatchList)
admin.site.register(StreamingPlatform)
admin.site.register(Reviews)
