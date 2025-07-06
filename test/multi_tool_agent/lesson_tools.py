def generate_lesson_plan(topic: str, grade: str, language: str = "English") -> dict:
    lesson = f"""
Title: {topic} for Grade {grade} ({language})

Explanation:
Simple explanation of {topic} in {language}.

Activities:
1. Storytelling or drawing
2. Quick Q&A
3. Group discussion
"""
    return {"status": "success", "report": lesson.strip()}
