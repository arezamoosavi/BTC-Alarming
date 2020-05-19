from tortoise import fields
from tortoise.models import Model


class BTC_USD(Model):
    id = fields.IntField(pk=True)
    amount = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "btc_usd"
        table_description = "This table contains bitcoin value in us dollar"

    def __str__(self):
        return "bitcoin in {} is {} us dollar".format(self.created_at, self.amount)

class BTC_EUR(Model):
    id = fields.IntField(pk=True)
    amount = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "btc_eur"
        table_description = "This table contains bitcoin value in euro"

    def __str__(self):
        return "bitcoin in {} is {} us dollar".format(self.created_at, self.amount)

