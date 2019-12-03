# ReCaptcha with oTree
## Demo
Head over to heroku for a [live demo](https://recap-demo.herokuapp.com).
Tested with oTree v2.5.3.

## Installation
- sign up for recaptcha
    - select V2 with otherwise default options 
    - make sure to add ```herokuapp.com``` as the domain if you intend to use it on Amazon Mechanical Turk.
    - for development, also add ```localhost```
- add ```django-recaptcha``` to the requirements_base.txt
- install: ```pip install -r requirements.txt```

## Usage
- add 'captcha' to otree extension apps:
```python
# settings.py
EXTENSION_APPS = [
    ...,
    'captcha',
]
```
- add recaptcha credentials the to your settings.py:
```python
# settings.py
RECAPTCHA_PUBLIC_KEY = 'MyRecaptchaKey123'
RECAPTCHA_PRIVATE_KEY = 'MyRecaptchaPrivateKey456'
```

- alternatively, use environmental variables (on heroku):
```python
# settings.py
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
```


- add a dummy field to the player, make sure it may be left blank:
```python 
# models.py
class Player(BasePlayer):
    captcha = models.CharField(blank=True)
    ...
```

- import the recaptcha field in pages.py, then add it to the page:
```python
# pages.py
from captcha.fields import ReCaptchaField

class Captcha(Page):
    form_model = 'player'
    form_fields = ['captcha']

    def get_form(self, data=None, files=None, **kwargs):
        frm = super().get_form(data, files, **kwargs)
        frm.fields['captcha'] = ReCaptchaField(label='')
        return frm
```

- add the captcha to your template:
```jinja2
# Captcha.html
{% block content %} 
    ...   
    {% formfield player.captcha %}
{% endblock %}
```

## Acknowledgements
This is heavily based on [Philipp Chapkovski's](https://github.com/chapkovski) [answer](https://groups.google.com/d/msg/otree/69qEkthJYL8/KLcpXVIXAQAJ) on the oTree Google group. I made some adjustments to make it work with oTree 2.5.3.