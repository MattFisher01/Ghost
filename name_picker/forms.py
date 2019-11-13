from django import forms

class LoginForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)

class name_picker_form(forms.Form):
    _c1 = None
    _c2 = 'Test2'
    _c3 = 'Test3'
    def __init__(self, *args, c1, c2, c3, **kwargs):
        self._c1 = c1
        self._c2 = c2
        self._c3 = c3
        super(name_picker_form, self).__init__(self._c1, self._c2, self._c3)

    NAME_CHOICES = [('c1', _c1), ('c2', _c2), ('c3', _c3)]
    ghost_name = forms.CharField(label='Ghost Name', widget=forms.RadioSelect(choices=NAME_CHOICES))
