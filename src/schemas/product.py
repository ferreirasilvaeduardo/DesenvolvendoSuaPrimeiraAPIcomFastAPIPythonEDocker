from decimal import Decimal
from typing import Annotated, Optional

from pydantic import AfterValidator, Field

from src.schemas.base import BaseSchemaMixin, OutSchema
from src.utils.utils import convert_decimal_128

Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: Decimal = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutSchema):
    ...


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[Decimal_] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product status")


class ProductUpdateOut(ProductOut):
    ...
