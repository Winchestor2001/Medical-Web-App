from django.db import models
from django.contrib.auth.models import User


class Neighborhood(models.Model):
    slug = models.SlugField(help_text="Buerga xechnarsa yozmang")
    name = models.CharField(max_length=255)
    population = models.BigIntegerField()

    def __str__(self):
        return "{} - {}".format(self.name, self.population)


class Street(models.Model):
    slug = models.SlugField(help_text="Buerga xechnarsa yozmang")
    name = models.CharField(max_length=255)
    population = models.BigIntegerField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.population)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    def __str__(self):
        return "{}".format(self.full_name)


class Staff(models.Model):
    CHOISES = (
        ("Врач", "Врач"),
        ("Оилавий хамшира", "Оилавий хамшира"),
        ("Умумий амалий хамшира", "Умумий амалий хамшира"),
        ("Доя", "Доя"),
        ("Болалар хамшира", "Болалар хамшира"),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    rank = models.CharField(max_length=255, choices=CHOISES)

    def __str__(self):
        return "{} - {}".format(self.full_name, self.rank)


class Address(models.Model):
    addres_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    

    def __str__(self):
        return "{} - {}".format(self.full_name, self.phone_number)


class Work(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    staff = models.ManyToManyField(Staff)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    street = models.ManyToManyField(Street)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.doctor, self.date)
