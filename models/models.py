from tortoise import fields
from tortoise.models import Model


class Rate(Model):
    """
    Модель для хранения тарифов.
    """

    date = fields.DateField(null=False)
    cargo_type = fields.CharField(max_length=255, null=False)
    rate = fields.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        """
        Метакласс для модели Rate.
        """
        table = "rates"
