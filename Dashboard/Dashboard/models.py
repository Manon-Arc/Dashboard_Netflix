"""
models.py - unused
"""

# from django.db import models
#
#
# class Data(models.Model):
#     Age = models.IntegerField()
#     Gender = models.CharField(max_length=100)
#     Marital_Status = models.CharField(max_length=100)
#     Occupation = models.CharField(max_length=100)
#     Monthly_Income = models.CharField(max_length=100)
#     Educational_Qualifications = models.CharField(max_length=100)
#     Family_Size = models.IntegerField()
#     Latitude = models.FloatField()
#     Longitude = models.FloatField()
#     Postal_Code = models.IntegerField()
#     Output = models.BooleanField()
#     Feedback = models.CharField(max_length=100)
#     M = models.BooleanField()
#
#     @classmethod
#     def Average(cls, column):
#         return cls.objects.aggregate(avg=models.Avg(column))["avg"]
#
#     @classmethod
#     def Sum(cls, column):
#         return cls.objects.aggregate(sum=models.Sum(column))["sum"]
#
#     @classmethod
#     def Count(cls, column):
#         return cls.objects.aggregate(count=models.Count(column))["count"]
#
#     @classmethod
#     def Min(cls, column):
#         return cls.objects.aggregate(min=models.Min(column))["min"]
#
#     @classmethod
#     def Max(cls, column):
#         return cls.objects.aggregate(max=models.Max(column))["max"]
#
#     @classmethod
#     def Median(cls, column):
#
#         count = Data.Count(column)
#         values = sorted(column)
#
#         if count % 2 == 1:
#             return values[count // 2]
#         else:
#             mid = count // 2
#             return (values[mid - 1] + values[mid]) / 2.0
#
#     @classmethod
#     def Ratio_conditional(cls, column, value, ope=None):
#         if ope == "sup":
#             column = f"{column}__gt"
#         elif ope == "inf":
#             column = f"{column}__lt"
#
#         all_data = Data.objects.all()
#
#         filtered_data = all_data.filter(**{column: value})
#         print(str(filtered_data.query))
#         count = filtered_data.count()
#
#         return round(count / all_data.count(), 2)
#
#     def __str__(self):
#         return f"{self.Gender} - {self.Age}"
#
#     class Meta:
#         db_table = "data"
