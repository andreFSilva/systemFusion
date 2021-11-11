from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import Servico, Funcionarios, Profissao, Clientes, Produtos
from django.contrib import messages

from .forms import ContatoForm
from django.views.generic import FormView


class IndexView(FormView):
    template_name = 'core/index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()[:6]
        context['funcionarios'] = Funcionarios.objects.order_by('?').all()[:6]
        context['profissoes'] = Profissao.objects.order_by('?').all()[:6]
        context['produtos'] = Produtos.objects.order_by('?').all()[:3]
        context['clientes'] = Clientes.objects.order_by('?').all()[:6]
        return context

    # Email
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


