from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

class TipCalculator(BoxLayout):      # KV file then is tip_calculator.kv
    tip_amount = StringProperty("")
    total_bill = StringProperty("")

    # Constants for service levels and tip rates
    SERVICE_LEVELS = ["Poor", "OK", "Good", "Great"]
    TIP_RATES = [0.05, 0.10, 0.15, 0.20]

    def calculate_tip(self):
        # Get selected service level index and bill amount
        service_level = self.ids.service_spinner.text
        try:
            bill_amount = float(self.ids.amount_box.text)
            quality_index = self.SERVICE_LEVELS.index(service_level)
            tip_rate = self.TIP_RATES[quality_index]
        except (ValueError, IndexError):
            self.tip_amount = "Invalid input"
            self.total_bill = ""
            return

        # Perform calculations
        tip_amount = bill_amount * tip_rate
        total_bill = bill_amount + tip_amount

        # Update labels with calculated values
        self.tip_amount = f"${tip_amount:.2f}"
        self.total_bill = f"${total_bill:.2f}"

class TipCalculatorApp(App):
    def build(self):
        Builder.load_file('tip_calculator.kv')
        return TipCalculator()

if __name__ == "__main__":
    TipCalculatorApp().run()
