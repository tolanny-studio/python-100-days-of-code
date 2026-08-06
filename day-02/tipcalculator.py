class TipCalculator:
    def __init__(self, total_bill, percentage_tip, bill_splitters):
        self.__total_bill = total_bill
        self.__percentage_tip = percentage_tip
        self.__bill_splitters = bill_splitters
        self.__payment = 0

    def calculate_payment(self) -> str:
        self.__payment = (
            (self.__total_bill + ((self.__percentage_tip / 100) * self.__total_bill))
        ) / self.__bill_splitters

        payment_ = round(self.__payment, 2)
        return str(payment_)

    def __str__(self):
        return f"\nEach person should pay ${self.calculate_payment()}"
