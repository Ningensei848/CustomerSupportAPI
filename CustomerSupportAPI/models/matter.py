from django.db import models

import uuid

from .calling import CallingModel


class MatterModel(models.Model):
    """
    id_: 一意に識別できるようなID
    timestamp: データを入力した時刻（≒電話を受けた時刻）
    responder: 電話を受けた人
    calling: 電話をかけてきた人
        name: 名前
        phone_number: 電話番号
        affiliation: 所属 (optional)
    memo: 何でも入力していい部分，とりあえず聞いたことすべて
    title: 要約すると，何の連絡だったのか？
    place: どこで(optional)
    date: いつ(optional)
    time: 何時に(optional)
    call_back_by: いつまでに折り返すべきか (optional)
    """

    # set default automatically via db or front page. -----------------------------------------------------------
    id_ = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,  # cf. https://docs.djangoproject.com/en/3.1/ref/models/fields/#uuidfield
        editable=False,
        verbose_name='matter_id',
        help_text='It is an ID that can be assigned to a record so that it can be uniquely identified for each matter.'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='対応日時',
        help_text='Represents the time when the person receiving the call entered the data into the system, i.e., the approximate time the call was received.'
    )
    # # # # # responder = models.ForeignKey(Responder, on_delete=models.PROTECT, editable=False, verbose_name='', help_text='')
    responder = models.CharField(
        max_length=255,
        verbose_name='受信者',
        help_text='The person who received the call.'
    )   # TODO: merge own DB already

    # Minimum Information **Required**. ----------------------------------------------------------
    calling = models.ForeignKey(
        CallingModel,
        on_delete=models.PROTECT,
        verbose_name='発信者',
        help_text='the person who contacted customer support.'
    )
    memo = models.TextField(
        verbose_name='メモ',
        help_text='A column where you fill in everything you can remember for now.'
    )

    # Necessary, if possible. --------------------------------------------------------------------
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='要件',
        help_text='If you had one keyword to tell your colleagues about this telephone, it would be ...'
    )
    place = models.CharField(
        max_length=1024,  # allow short name or URL(< 1024 char)
        blank=True,
        null=True,
        verbose_name='場所',
        help_text='Where does this matter take place?'
    )

    # ---> !!Caution: if user need to input time info below, please set time default via front page.
    date = models.DateField(
        blank=True,
        null=True,
        verbose_name='日付',
        help_text='When will this matter take place?'
    )
    time = models.TimeField(
        blank=True,
        null=True,
        verbose_name='時刻',
        help_text='What time does this matter take place?'
    )
    call_back_by = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='折り返し期限',
        help_text='When do we have to call back to customer by?'
    )

    class Meta:
        verbose_name_plural = '問い合わせ'
