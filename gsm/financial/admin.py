from django.contrib import admin
from django.contrib.admin import TabularInline

from gsm.financial.models import (Historico, Conta, Pagamento)


# import locale
# locale.setlocale(locale.LC_ALL, '')
@admin.register(Historico)
class AdminHistorico(admin.ModelAdmin):
    # valor_total vem de models.py na classe HistoricoManager
    list_display = ('descricao', 'operacao', 'totais', 'baixado', 'restam')
    # list_display = ('descricao', 'totais', 'pagar_baixado', 'receber_baixado', 'saldo')
    # readonly_fields = ['totais', 'pagar_baixado', 'receber_baixado']

    # def totais(self, obj):
    #     if not obj.totais:
    #         return obj.totais
    #     else:
    #         return '%.2f' % obj.totais


class InlinePagamento(TabularInline):
    model = Pagamento


@admin.register(Conta)
class AdminConta(admin.ModelAdmin):
    list_display = ('pessoa',
                    'historico',
                    'data_vencimento',
                    'data_pagamento',
                    'valor_titulo',
                    'operacao',
                    'status',
                    'descricao')

    search_fields = ('descricao',)
    # list_filter = ('data_vencimento', 'status', 'operacao', 'historico', 'pessoa',)
    inlines = [InlinePagamento, ]
