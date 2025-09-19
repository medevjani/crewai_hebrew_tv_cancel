class ClientAgent:
    def __init__(self):
        self.request = "שלום, אני רוצה לבטל את המנוי לטלוויזיה שלי."

    def speak(self) -> str:
        return self.request
