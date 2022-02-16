from django.db import models


Section = (
    ('General', 'General'),
    ('Django', 'Django'),
    ('Python', 'Python'),
    ('Database', 'Database'),
    ('Api', 'Api'),
    ('Aws', 'Aws'),
    ('Frontend', 'Frontend'),
    ('Extras', 'Extras'),
)


class allErrors(models.Model):
    serial_no = models.AutoField(primary_key=True)
    section = models.CharField(
        max_length=10, choices=Section, default='General')
    error_type = models.CharField(max_length=150, blank=False, null=False)
    solution = models.TextField(max_length=10000, blank=False, null=False)
    link = models.URLField(max_length=10000, blank=True)

    def __str__(self):
        return self.section + ' | ' + self.error_type
