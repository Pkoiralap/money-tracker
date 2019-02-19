from django.db import models

class Transaction(models.Model):
    type = models.CharField(max_length=20, choices=[('income', 'Income'), ('expenditure', 'Expenditure')])
    money = models.FloatField(max_length=20)
    date = models.DateTimeField(auto_created=True)
    giving_party = models.CharField(max_length=100)
    receiving_party = models.CharField(max_length=100)

    def __str__(self):
        return self.giving_party + ' to ' + self.recieving_party + ' type: ' + self.type + ' :' + str(self.money)