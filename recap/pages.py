from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# recaptcha
from captcha.fields import ReCaptchaField


class Captcha(Page):
    form_model = 'player'
    form_fields = ['captcha']

    def get_form(self, data=None, files=None, **kwargs):
        frm = super().get_form(data, files, **kwargs)
        frm.fields['captcha'] = ReCaptchaField(label='')
        return frm


class Results(Page):
    pass


page_sequence = [Captcha, Results]
