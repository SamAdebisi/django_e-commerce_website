from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from main import forms
from .models import ProductTag, ProductImage, Product

# Create your views here.


class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


# def contact_us(request):
#     if request.method == 'POST':
#         form = forms.ContactForm(request.POST)
#         if form.is_valid():
#             form.send_mail()
#             return HttpResponseRedirect('/')
#     else:
#         form = forms.ContactForm()
#     return render(request, 'contact_form.html', {'form': form})


class ProductListView(ListView):
    template_name = 'main/product_list.html'
    paginate_by = 4

    def get_queryset(self):
        tag = self.kwargs['tag']
        self.tag = None
        if tag != "all":
            self.tag = get_object_or_404(
                ProductTag, slug=tag
            )
        if self.tag:
            products = Product.objects.active().filter(
                tags=self.tag
            )
        else:
            products = Product.objects.active()
        return products.order_by('name')
