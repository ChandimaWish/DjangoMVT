from django.db import models

from django.utils.translation import gettext as _

class StudentDetails(models.Model):


    school_name = models.CharField(_("school_name"), max_length=255)
    year= models.DateField(_("year"))
    StudentID = models.IntegerField(_("StudentID"), auto_created=True, primary_key=True)
    First_Name = models.CharField(_("First Name"), max_length=150)
    Last_Name = models.CharField(_("Last Name"), max_length=150)
    Year_Level = models.CharField(_("Year Level"), max_length=50)
    Class = models.CharField(_("Class"), max_length=50)
    Subject = models.CharField(_("Subject"), max_length=50)
    Answers = models.CharField(_("Answers"), max_length=255)
    Correct_Answers =  models.CharField(_("Correct Answers"), max_length=255)
    Question_Number = models.IntegerField(_("Question Number"))
    Subject_Contents = models.CharField(_("Subject Contents"), max_length=255)
    Assessment_Areas = models.CharField(_("Assessment Areas"), max_length=255)
    sydney_correct_count_percentage = models.FloatField(_("sydney_correct_count_percentage"))
    sydney_average_score = models.FloatField(_("sydney_average_score"))
    sydney_participants = models.IntegerField(_("sydney_participants"))
    student_score  = models.FloatField(_("student_score"))
    student_total_assessed  = models.IntegerField(_("student_total_assessed"))
    student_area_assessed_score  = models.FloatField(_("student_area_assessed_score"))
    total_area_assessed_score  = models.FloatField(_("total_area_assessed_score"))
    participant  = models.IntegerField(_("participant"))
    correct_answer_percentage_per_class  = models.FloatField(_("correct_answer_percentage_per_class"))
    average_score  = models.FloatField(_("average_score"))
    school_percentile  = models.IntegerField(_("school_percentile"))
    sydney_percentile  = models.IntegerField(_("sydney_percentile"))
    strength_status = models.CharField(_("strength_status"), max_length=255)
    high_distinct_count = models.IntegerField(_("high_distinct_count"))
    distinct_count = models.IntegerField(_("distinct_count"))
    credit_count = models.IntegerField(_("credit_count"))
    participant_count = models.IntegerField(_("participant_count"))
    award = models.CharField(_("award"), max_length=255)












