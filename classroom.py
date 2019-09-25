class Assignment:
    def __init__(self, assignment_name, github_url=""):
        self.name = assignment_name
        self.github_url = github_url
        self.completed = False
        self.grade = None
    def mark_done(self, grade):
        self.grade = grade
        self.completed = True

class Student:
    def __init__(self, student_name=""):
        self.name = student_name
        self.pending_homeworks = []
        self.completed_homeworks = []
    def complete_homework(self, homework_name, homework_grade):
        for item in self.pending_homeworks:
            if item.name == homework_name:
                new_item = item
                self.pending_homeworks.remove(item)
                new_item.mark_done(homework_grade)
                self.completed_homeworks.append(new_item)
                return True
        return False
    def print_outstanding_homeworks(self):
        if self.pending_homeworks:
            print(f"{self.name} still needs to turn in:")
            for item in self.pending_homeworks:
                print(f"{item.name}\n")
        else:
            print(f"{self.name} has no outstanding homeworks!")
    def assign_homework(self, new_assignment):
        self.pending_homeworks.append(new_assignment)
    

class SeiClass:
    def __init__(self, class_name=""):
        self.name = class_name
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def assign_homework(self, homework):
        for student in self.students:
            new_hw = Assignment(homework.name, homework.github_url)
            student.assign_homework(new_hw)
    def print_avg_grade(self, homework):
        total_grade = 0
        grade_count = 0
        for student in self.students:
            for hw in student.completed_homeworks:
                if hw.name == homework:
                    grade_count += 1
                    total_grade += hw.grade
        print (total_grade / grade_count)


# l = ['a', "b", "c"]
# print(f"{l}")

henry = Student('Henry')
sarah = Student('Sarah')
mike = Student('Mike')

sei26 = SeiClass('sei26')
sei26.add_student(henry)
sei26.add_student(sarah)
sei26.add_student(mike)

assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')

sei26.assign_homework(assignment1)

henry.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

henry.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
mike.print_outstanding_homeworks()

sei26.print_avg_grade("Bounty Hunters")