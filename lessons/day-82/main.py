automation_plan = {
    "task": "Organize sample photos by year",
    "input": "A folder of copies of photos",
    "steps": ["Preview file dates", "Group copies by year", "Review the result"],
    "safety_check": "Keep originals unchanged until the preview is checked",
}
for key, value in automation_plan.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
