from django.db import models


class Bow(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    bow = models.ForeignKey(Bow, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase of {self.bow.name} on {self.purchase_date}"


class TimeStatistics(models.Model):
    time_gained = models.PositiveIntegerField(default=0)
    time_spent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Statistics for {self.player_identifier}: Time Gained={self.time_gained}, Time Spent={self.time_spent}"
