from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student

from .forms import StudentForm


# By generic class


class StudentCreateView(CreateView):
    template_name = 'students/student_create.html'
    form_class = StudentForm
    queryset = Student.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    template_name = 'students/student_create.html'
    form_class = StudentForm
    queryset = Student.objects.all()

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class StudentDetailView(DetailView):
    template_name = 'students/student_detail.html'
    queryset = Student.objects

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student, id=id_)


class StudentDeleteView(DeleteView):
    template_name = 'students/student_delete.html'

    def get_object(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        print(id_)
        return get_object_or_404(Student, id=id_)

    def get_success_url(self, **kwargs):
        return reverse('students:list')


class StudentListView(ListView):
    template_name = 'students/student_list.html'
    # If you don't want generic name of template <modelname>_list.html
    queryset = Student.objects.all()

# By functions


# def student_create_view(request):
#     form = StudentForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         form = StudentForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'students/student_create.html', context)


# def student_detail_view(request, id):
#     # obj = Student.objects.get(id=id)
#     obj = get_object_or_404(Student, id=id)
#
#     context = {
#         'obj': obj,
#     }
#     return render(request, "students/student_detail.html", context)


# def student_delete_view(request, id):
#     obj = get_object_or_404(Student, id=id)
#     if request.method == "POST":
#         obj.delete()
#         return redirect('../../')
#     context = {
#         "object": obj
#     }
#     return render(request, "students/student_delete.html", context)


# def student_list(request):
#     queryset = Student.objects.all()
# context = {
#     "object_list": queryset
# }
# return render(request,"students/students_list.html",context)
