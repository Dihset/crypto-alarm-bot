from decimal import Decimal

from pydantic import BaseModel, Field


class Candlestick(BaseModel):
    start_time: int = Field(..., alias="t")
    close_time: int = Field(..., alias="T")
    pair: str = Field(..., alias="s")
    interval: str = Field(..., alias="i")
    first_trade_id: int = Field(..., alias="f")
    last_trade_id: int = Field(..., alias="L")
    open_price: Decimal = Field(..., alias="o")
    close_price: Decimal = Field(..., alias="c")
    high_price: Decimal = Field(..., alias="h")
    low_price: Decimal = Field(..., alias="l")
    base_asset_volume: str = Field(..., alias="v")
    number_of_trades: int = Field(..., alias="n")
    is_closed: bool = Field(..., alias="x")
    quote_asset_volume: str = Field(..., alias="q")
    taker_buy_base: str = Field(..., alias="V")
    taker_buy_quote: str = Field(..., alias="Q")
    ignore: str = Field(..., alias="B")
