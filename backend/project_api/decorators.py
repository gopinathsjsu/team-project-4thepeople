from abc import ABC, abstractmethod


# Dynamic pricing - Strategy
class Strategy(ABC):
    @abstractmethod
    def pricingScheme(self):
        pass


class weekdayPricing(Strategy):
    def pricingScheme(self):
        print("weekday no inc in price")
        percentageIncrease = 0
        return percentageIncrease


class weekendPricing(Strategy):
    def pricingScheme(self):
        print("weekend rise in price")
        percentageIncrease = 5
        return percentageIncrease


class holidayPricing(Strategy):
    def pricingScheme(self):
        print("holiday rise in price")
        percentageIncrease = 10
        return percentageIncrease


class Default(Strategy):
    def pricingScheme(self) -> int:
        return 0


class DynamicPricing():
    strategy: Strategy

    def setStrategy(self, strategy: Strategy = None) -> None:
        self.strategy = strategy

    def executeStrategy(self) -> int:
        result = self.strategy.pricingScheme()
        return result;
