def guardrails(text: str) -> str:
    """Simple guardrail to prevent harmful/off-topic responses."""
    blocked = ["אלימות", "פשע", "שנאה"]
    for word in blocked:
        if word in text:
            return "⚠️ תוכן לא מאושר"
    return text
