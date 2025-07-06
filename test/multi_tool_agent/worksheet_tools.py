def generate_worksheets(concept: str) -> dict:
    worksheet = f"""
Grade 2:
1. What is {concept}?
2. Draw it.

Grade 4:
1. Explain {concept}.
2. Give two examples.
"""
    return {"status": "success", "report": worksheet.strip()}
