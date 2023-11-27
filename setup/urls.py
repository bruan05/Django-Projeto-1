from django.contrib import admin
from django.urls import path
from todos.views import InfoListView, InfoCreateView, InfoUpdateView, InfoDeleteView, InfoCompleteView



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", InfoListView.as_view(), name="info_list"),
    path("create", InfoCreateView.as_view(), name="info_create"),
    path("update/<int:pk>", InfoUpdateView.as_view(), name="info_update"),
    path("delete/<int:pk>", InfoDeleteView.as_view(), name="info_delete"),
    path("complete/<int:pk>", InfoCompleteView.as_view(), name="info_complete")
]
