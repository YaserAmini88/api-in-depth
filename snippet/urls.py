from django.urls import path
from snippet import views
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('snippet/', views.snippet_list),
#     path('snippet/<int:pk>/', views.snippet_detail),
# ]


urlpatterns = [
    path('snippet/', views.SnippetList.as_view()),
    path('snippet/<int:pk>/', views.SnippetDetail.as_view()),
]

#These 2 urls will be available = http://127.0.0.1:8000/snippets.json, http://127.0.0.1:8000/snippets.api
urlpatterns = format_suffix_patterns(urlpatterns)