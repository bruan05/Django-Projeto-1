from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Info, Pet

class InfoListView(ListView):
    model = Info, Pet
    
class InfoCreateView(CreateView):
    model = Info, Pet
    fields = ["title","tipe","breed","color","genero", "deadline"]
    success_url = reverse_lazy("info_list")
    
class InfoUpdateView(UpdateView):
    model = Info, Pet
    fields = ["title","tipe","breed","color","genero", "deadline"]
    success_url = reverse_lazy("info_list")
    
class InfoDeleteView(DeleteView):
    model = Info, Pet
    success_url = reverse_lazy("info_list")
    
class InfoCompleteView(View):
    def get(self, request, pk):
        Info = get_object_or_404(Info, pk=pk)
        Info.mark_has_complete()
        return redirect("info_list")
    