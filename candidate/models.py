from address.models import Address, Contact
from django.db import models
from django.contrib.auth.models import User


class AddressForCandidate(Address):
    candidate = models.OneToOneField('Candidate', on_delete=models.CASCADE, related_name="candidate_address")

    def __str__(self):
        return str(self.candidate)


class ContactForCandidate(Contact):
    candidate = models.OneToOneField('Candidate', on_delete=models.CASCADE, related_name="candidate_contact")

    def __str__(self):
        return str(self.candidate)


class Candidate(models.Model):
    SEX = (
        ('Female', 'Female'),
        ('Male', 'Male'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=SEX)
    annual_salary = models.PositiveIntegerField()
    issued_date = models.DateField()
    joining_date = models.DateField()
    designation = models.CharField(max_length=255)
    reporting_officer = models.CharField(max_length=255)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
