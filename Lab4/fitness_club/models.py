from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=30)
    groups = models.ManyToManyField(Group)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    instructors = models.ManyToManyField(Instructor)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return f"Lesson {self.id}"


class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"Payment {self.id}"

