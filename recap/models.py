from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Christian König gen. Kersting'

doc = """
ReCaptcha Demo
"""


class Constants(BaseConstants):
    name_in_url = 'recap'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    captcha = models.CharField(blank=True)
