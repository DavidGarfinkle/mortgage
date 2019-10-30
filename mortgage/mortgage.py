import numpy as np
import dataclasses as dc
import typeguard as tg
from decimal import Decimal

class Dollar(float):
    def __str__(self):
        return '${:,.2f}'.format(self)

@dc.dataclass
@tg.typechecked
class Mortgage:
    price: Dollar
    downpayment: Dollar 
    insurance: Dollar = 0
    amortization: int
    interest: float

    def __post_init__(self):
        self.insurance = self.cmhc_insurance(self.price, self.downpayment)

    def cmhc_insurance(price: Dollar, downpayment: Dollar) -> float:
        ltv = (price - downpayment) / price
        assert ltv > 0
        assert ltv <= 1
        
        if ltv >= 0.95:
            return 0.04
        elif ltv >= 0.90:
            return 0.031
        elif ltv >= 0.85:
            return 0.028
        elif ltv >= 0.80:
            return 0.024
        else:
            return 0

@dc.dataclass
@tg.typechecked
class RealEstateInvestment:
    mtg: Mortgage
    property_tax: Dollar
    school_tax: Dollar
    condo_fees: Dollar
    insurance: Dollar
    maintenance: Dollar
    welcome_tax: Dollar
    notary: Dollar
    title_insurance: Dollar
    inspection: Dollar
    repair: Dollar

