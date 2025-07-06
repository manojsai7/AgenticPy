from google.adk.agents import Agent
from multi_tool_agent.lesson_tools import generate_lesson_plan
from multi_tool_agent.worksheet_tools import generate_worksheets
from multi_tool_agent.visual_tools import generate_visual

root_agent = Agent(
    name="sahayak_teacher_assistant",
    model="gemini-1.5-flash",
    description="Multi-tool agent for teachers in multi-grade classrooms.",
    instruction="""
You are Sahayak, an AI assistant that helps teachers by providing:
1. Localized lesson plans
2. Differentiated worksheets
3. Simple visual aids
""",
    tools=[
        generate_lesson_plan,
        generate_worksheets,
        generate_visual
    ],
)










#'''change of alt code'''



# from google.adk.agents import Agent

# def generate_lesson_plan(topic: str, grade: str, language: str = "English") -> dict:
#     """Generates a simple localized lesson plan."""
#     lesson = f"""
# Title: Understanding {topic} for Grade {grade} (Language: {language})

# Explanation:
# A short, engaging story or explanation about {topic} tailored for Grade {grade} in {language}.

# Suggested Activities:
# 1. Simple discussion or storytelling.
# 2. Quick drawing activity related to {topic}.
# 3. Group question-answer session.
# """
#     return {"status": "success", "report": lesson.strip()}

# def generate_worksheets(concept: str) -> dict:
#     """Generates sample worksheets for multiple grade levels."""
#     worksheet = f"""
# Grade 2:
# 1. What is {concept}?
# 2. Draw a picture of {concept}.
# 3. True or False: {concept} is important.

# Grade 4:
# 1. Explain {concept} in your own words.
# 2. Give two examples of {concept}.
# 3. Match the following related to {concept}.
# """
#     return {"status": "success", "report": worksheet.strip()}

# def generate_visual(concept: str) -> dict:
#     """Suggests simple visual for blackboard explanation."""
#     visual = f"""
# Visual Suggestion:
# Draw a simple diagram representing {concept}, such as a labeled flowchart or symbol. Example: For 'Water Cycle', show clouds, rain, rivers, and sun arrows.

# Caption: Visual representation of {concept}.
# """
#     return {"status": "success", "report": visual.strip()}


# root_agent = Agent(
#     name="sahayak_teacher_assistant",
#     model="gemini-1.5-pro",
#     description=(
#         "An AI teaching assistant for multi-grade classrooms to generate lesson plans, worksheets, and visual aids."
#     ),
#     instruction=(
#         "You are Sahayak, an AI assistant that helps teachers by creating localized lessons, worksheets, visuals, and student assessments."
#     ),
#     tools=[generate_lesson_plan, generate_worksheets, generate_visual],
# )
