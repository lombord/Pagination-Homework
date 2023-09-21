"""IMPORTANT:Use only after first migration"""

from random import randrange as rd, sample, choice as ch
from base_app.models import Language, Company, Vacancy


langs = ["Javascript", "Python", "Go", "Java", "Kotlin", "PHP", "C#", "Swift",
         "R", "Ruby", "C and C++", "Matlab", "TypeScript", "Scala", "SQL"]

companies = ["Yotz", "Edgepulse", "Katz", "Kanoodle", "Mydo",
             "Centimia", "Skippad", "Gigashots", "Myworks", "Yoveo",]


langObjs = [Language.objects.create(name=l) for l in langs]

compObjs = [Company.objects.create(name=c) for c in companies]


stats = 'junior', 'middle', 'senior'


lorem = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
"""


def get_lorem(len_=50):
    assert len(lorem) > len_, "Invalid len length"
    start = rd(len(lorem)-len_)
    return lorem[start:start+len_]


for i in range(1000):
    v = Vacancy.objects.create(
        title=get_lorem(),
        company=ch(compObjs),
        status=ch(stats),
        description=get_lorem(250),
        salary=rd(100, 5001))
    v.languages.set(sample(langObjs, k=rd(1, 8)))

    v.save()
