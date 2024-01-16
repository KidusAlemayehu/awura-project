from django.db import models

class InternshipRole(models.Model):
    ROLE_CHOICES = [
        ('UI/UX', 'UI/UX'),
        ('Backend Development using Django', 'Backend Development using Django'),
        ('Devops', 'Devops'),
        ('Frontend Development', 'Frontend Development'),
        ('Mobile application Development in Flutter', 'Mobile application Development in Flutter'),
    ]

    role_name = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return self.role_name
    

class InternshipRequest(models.Model):
    role = models.ForeignKey(InternshipRole, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name