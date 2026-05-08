import re


body_text = open("sample.txt", "r", encoding="utf-8").read()


salary_match = re.search(
    r"Mức lương\s+([^\n]+)",
    body_text
)

experience_match = re.search(
    r"Kinh nghiệm\s+([^\n]+)",
    body_text
)

if salary_match:
    print(salary_match.group(1))

if experience_match:
    print(experience_match.group(1))
