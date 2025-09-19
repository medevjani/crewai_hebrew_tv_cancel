from crewai.tools import tool

@tool("guardrails_tool")
def guardrails_tool(text: str) -> str:
    """Simple guardrail to prevent unsafe/off-topic responses."""
    blocked = ["אלימות", "פשע", "שנאה"]
    for word in blocked:
        if word in text:
            return "⚠️ תוכן לא מאושר"
    return text
