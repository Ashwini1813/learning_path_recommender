import pandas as pd

class LearningPathRecommender:
    def __init__(self, data_path):
        self.courses = pd.read_csv(data_path)

    def recommend_path(self, goal, level):
        filtered = self.courses[
            (self.courses["category"] == goal) &
            (self.courses["level"].isin(self._levels_up_to(level)))
        ].sort_values("order")

        return filtered[["course_name", "level"]]

    def skill_gap(self, user_skills, goal):
        goal_courses = self.courses[self.courses["category"] == goal]

        required_skills = set()
        for skills in goal_courses["skills"]:
            for s in skills.split(";"):
                required_skills.add(s.strip())

        missing = required_skills - set(user_skills)
        return list(missing)

    def _levels_up_to(self, level):
        order = ["Beginner", "Intermediate", "Advanced"]
        idx = order.index(level)
        return order[:idx + 1]
