def generate_visual(concept: str) -> dict:
    visual = f"""
Draw a simple diagram of {concept} with labels.

Example: Water Cycle - Clouds → Rain → River → Sun.
"""
    return {"status": "success", "report": visual.strip()}
