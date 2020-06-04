from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# recaptcha
from captcha.fields import ReCaptchaField


class PreCaptcha(Page):
    timeout_seconds = 30

    # set True/False depending on whether you want to display the timer or not
    def js_vars(self):
        return {'hide_timer': False}

    def before_next_page(self):
        if not self.timeout_happened:
            self.player.captcha_necessary = False

class Captcha(Page):
    form_model = 'player'
    form_fields = ['captcha']

    def is_displayed(self):
        return self.player.captcha_necessary

    def get_form(self, data=None, files=None, **kwargs):
        frm = super().get_form(data, files, **kwargs)
        frm.fields['captcha'] = ReCaptchaField(label='')
        return frm

class Results(Page):
    pass


page_sequence = [PreCaptcha, Captcha, Results]
