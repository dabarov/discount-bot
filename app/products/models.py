from django.db import models


class Item(models.Model):
    external_id = models.CharField(max_length=20, db_index=True)
    title = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)

    @property
    def latest_price(self):
        return self.prices.all().order_by("created_at").latest()


class Price(models.Model):
    item_id = models.ForeignKey(
        Item, on_delete=models.SET_NULL, related_name="prices", null=True
    )
    price = models.IntegerField(db_index=True, default=0)
    created_at = models.DateTimeField(auto_now=True)
