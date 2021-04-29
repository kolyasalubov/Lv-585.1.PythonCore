from datetime import datetime

from marshmallow import Schema, fields, validate


def validate_date(date_text: str, date_format: str) -> bool:
    try:
        datetime.strptime(date_text, date_format)
        return True
    except ValueError:
        return False


class ClientSchema(Schema):
    first_name = fields.String(required=True, allow_none=False)
    last_name = fields.String(required=True, allow_none=False)
    middle_name = fields.String(required=True, allow_none=False)
    phone_number = fields.String(required=True, allow_none=False)
    email = fields.String(required=True, allow_none=False)
    passport_number = fields.String(required=True, allow_none=False)
    itn = fields.String(required=True, allow_none=False)


class CreditCardSchema(Schema):
    card_number = fields.String(
        validate=[validate.Length(equal=16), lambda p: p.isdigit()], required=True, allow_none=False
    )
    expiration_date = fields.String(
        validate=[validate.Length(equal=7), lambda p: validate_date(p, '%Y-%m')], required=True, allow_none=False
    )
    merchant_id = fields.String(required=True, allow_none=True)


class OrderPutSchema(Schema):
    id = fields.Integer(required=False, allow_none=True)
    status = fields.String(required=True, allow_none=True)
    total = fields.Float(required=True, allow_none=True)
    payment_method = fields.String(required=True, allow_none=True)
    created_at = fields.String(required=False, allow_none=True)
