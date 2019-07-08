from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse





# class UserInfo(User):
#     nomecompleto = models.CharField('Nome Completo', max_length=100, null=False, blank=False)
#     base = models.ForeignKey('core.client', null=True, blank=True, related_name="base",
#                              on_delete=models.CASCADE, verbose_name="Base ou Representação")
#     horario = models.ForeignKey('accounts.horario', null=False, blank=False, related_name="horario",
#                                 on_delete=models.CASCADE, verbose_name="Escolha seu Horário")
#     funcao = models.CharField('Função', max_length=50, null=False, blank=False)
#     ctps = models.CharField('Carteira de Trabalho', max_length=20, null=False, blank=False)
#     serie = models.CharField('Série', max_length=10, null=False, blank=False)
#
#     class Meta:
#         verbose_name = 'Perfil de Usuário'
#         verbose_name_plural = 'Perfil de Usuários'
#
#     def save(self, *args, **kwargs):
#         self.nomecompleto = self.nomecompleto.upper()
#         self.funcao = self.funcao.upper()
#
#         super(UserInfo, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.nomecompleto
