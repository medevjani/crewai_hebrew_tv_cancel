import litellm

class CustomerServiceAgent:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model

    def respond(self, client_text: str) -> str:
        """Generate a response as customer service agent."""
        prompt = f"""
        אתה נציג שירות לקוחות של חברת טלוויזיה.
        לקוח: {client_text}
        תשובה בעברית מנומסת:
        """
        response = litellm.completion(model=self.model, messages=[{"role":"user","content":prompt}])
        return response['choices'][0]['message']['content']
