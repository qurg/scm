from django import forms


class CustomerOrderAdminForm(forms.ModelForm):
    # pre_carton = forms.CharField(widget=forms.TextInput(attrs={'size': 30}), label='预报件数')
    # pre_weight = forms.CharField(widget=forms.TextInput(attrs={'size': 30}), label='预报重量')
    # pre_volume = forms.CharField(widget=forms.TextInput(attrs={'size': 30}), label='预报体积')
    # carton = forms.CharField(widget=forms.TextInput(attrs={'size': 35}), label='件数')
    # weight = forms.CharField(widget=forms.TextInput(attrs={'size': 35}), label='重量')
    # volume = forms.CharField(widget=forms.TextInput(attrs={'size': 35}), label='体积')

    size = forms.CharField(widget=forms.Textarea(attrs={'size': 35, 'rows': 4}), label='尺寸', required=False)
    pre_size = forms.CharField(widget=forms.Textarea(attrs={'size': 35, 'rows': 4}), label='预报尺寸', required=False)
