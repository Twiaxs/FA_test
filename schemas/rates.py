from pydantic import BaseModel


class RateInput(BaseModel):
    """
    Модель для загрузки тарифов.
    """

    cargo_type: str
    rate: float
