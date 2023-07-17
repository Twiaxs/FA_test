import json
from decimal import Decimal
from datetime import date

from fastapi import APIRouter, HTTPException, Query, UploadFile, File

from models.models import Rate
from schemas.rates import RateInput

router = APIRouter()


@router.post("/load_rates")
async def load_rates(file: UploadFile = File(...)):
    """
    Загрузка тарифов из файла.
    """
    content = await file.read()
    file_data = json.loads(content)

    rates_list = []
    for date_str, rate_inputs in file_data.items():
        for rate_input_dict in rate_inputs:
            rate_input = RateInput(**rate_input_dict)
            rate = Rate(
                date=date.fromisoformat(date_str),
                cargo_type=rate_input.cargo_type,
                rate=rate_input.rate
            )
            rates_list.append(rate)
    await Rate.bulk_create(rates_list)

    return {"message": "Тарифы успешно загружены."}


@router.get("/calculate_insurance_cost")
async def calculate_insurance_cost(
    cargo_type: str,
    declared_value: float,
    calculation_date: date = Query(...),
):
    """
    Расчет стоимости страхования.
    """
    rate = await Rate.filter(cargo_type=cargo_type, date=calculation_date).first()

    if rate:
        declared_value_decimal = Decimal(declared_value)
        insurance_cost = declared_value_decimal * rate.rate
        return {"insurance_cost": insurance_cost}

    raise HTTPException(
        status_code=404,
        detail="Тариф для указанного типа груза и даты не найден.",
    )
