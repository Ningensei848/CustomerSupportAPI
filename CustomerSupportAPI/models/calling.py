from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class CallingModel(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='氏名',
        help_text='the person who contacted customer support.'
    )
    phone_number = PhoneNumberField(
        verbose_name='電話番号',
        help_text="customer's phone number."
    )
    affiliation = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='所属',
        help_text="customer's affiliation (optional)."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'お客様の連絡先情報'
        ordering = ['name', 'phone_number']
