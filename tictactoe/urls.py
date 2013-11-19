from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Render Game Board
    url(r'^$', 'tictactoe.views.game_view', name='home'),
    url(r'^select/$', 'tictactoe.views.select_piece', name='select-piece'),
    url(r'^end-game/$', 'tictactoe.views.end_game', name='end-game'),

    # Django Admin
    url(r'^admin/', include(admin.site.urls)),
)
