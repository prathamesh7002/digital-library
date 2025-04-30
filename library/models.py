from django.db import models

class Book(models.Model):
    SUBJECT_CHOICES = [
        ('compiler_design', 'Compiler Design'),
        ('web_programming', 'Web Programming'),
        ('data_structure', 'Data Structure'),
        ('digital_technique', 'Digital Technique and Microprocessor'),
        ('computer_hardware', 'Computer Hardware'),
        ('mechanics', 'Mechanics'),
        ('machine_learning', 'Machine Learning'),
        ('data_analytics', 'Data Analytics'),
        ('software_engineering', 'Software Engineering'),
        ('maths1', 'Mathematics 1'),
        ('maths2', 'Mathematics 2'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('introduction_to_ai', 'Introduction to AI'),
        ('rdbms', 'RDBMS'),
        ('computer_network', 'Computer Network'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    file = models.FileField(upload_to='books/')  # PDF or e-book file
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title