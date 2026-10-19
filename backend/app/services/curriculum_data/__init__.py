from app.services.curriculum_data.days_phase1 import get_phase1_days
from app.services.curriculum_data.days_phase2 import get_phase2_days
from app.services.curriculum_data.days_phase3 import get_phase3_days
from app.services.curriculum_data.days_phase4 import get_phase4_days
from app.services.curriculum_data.phases_and_weeks import PHASES, WEEKS


def get_all_curriculum_data():
    all_days = []
    all_days.extend(get_phase1_days())
    all_days.extend(get_phase2_days())
    all_days.extend(get_phase3_days())
    all_days.extend(get_phase4_days())

    # Format IDs: e.g. day-001 to day-112
    formatted_lessons = []
    all_quizzes = []

    for d in all_days:
        day_num = d["day_number"]
        lesson_id = f"day-{day_num:03d}"

        lesson_entry = dict(d)
        lesson_entry["id"] = lesson_id

        # Extract quizzes and attach lesson_id
        quizzes = lesson_entry.pop("quiz_questions", [])
        for q in quizzes:
            q_copy = dict(q)
            q_copy["lesson_id"] = lesson_id
            q_copy["day_number"] = day_num
            all_quizzes.append(q_copy)

        formatted_lessons.append(lesson_entry)

    # Sort lessons by day_number
    formatted_lessons.sort(key=lambda x: x["day_number"])

    return {"phases": PHASES, "weeks": WEEKS, "lessons": formatted_lessons, "quizzes": all_quizzes}
