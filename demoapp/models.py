from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Parents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)


class CombinedChanges(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_combine', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_combine')
    parents = models.ForeignKey(Parents, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.teacher.name} - {self.parents.name}"


class M_M_models(models.Model):
    student = models.ManyToManyField(Student, related_name='student_mm')
    teacher = models.ManyToManyField(Teacher, related_name='teacher_mm')
    parents = models.ManyToManyField(Parents, related_name='parents_mm', null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

