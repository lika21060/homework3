from django.shortcuts import render
import random

def get_random_students():
    names = ['lika', 'ana', 'Mari', 'lizi', 'nia', 'sofo', 'tata']
    surnames = ['asanidze', 'gorgodze', 'sxiladze', 'xarashvili', 'nikolaishvili', 'mamukishvili', 'xunwelia', ]
    
    students = []
    for _ in range(100):
        student = {
            'name': random.choice(names),
            'surname': random.choice(surnames),
            'gpa': round(random.uniform(1.0, 4.0), 2),
            'course': random.randint(1, 4)
        }
        students.append(student)
    return students


def main_page_view(request):
    students = get_random_students()
    selected_student = random.choice(students)
    return render(request, 'main_page.html', {'student': selected_student})

def students_page_view(request):
    students = get_random_students()
    return render(request, 'students_page.html', {'students': students})