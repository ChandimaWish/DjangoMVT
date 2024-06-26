# Generated by Django 5.0.4 on 2024-04-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('StudentID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='StudentID')),
                ('school_name', models.CharField(max_length=255, verbose_name='school_name')),
                ('year', models.DateField(verbose_name='year')),
                ('First_Name', models.CharField(max_length=150, verbose_name='First Name')),
                ('Last_Name', models.CharField(max_length=150, verbose_name='Last Name')),
                ('Year_Level', models.CharField(max_length=50, verbose_name='Year Level')),
                ('Class', models.CharField(max_length=50, verbose_name='Class')),
                ('Subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('Answers', models.CharField(max_length=255, verbose_name='Answers')),
                ('Correct_Answers', models.CharField(max_length=255, verbose_name='Correct Answers')),
                ('Question_Number', models.IntegerField(verbose_name='Question Number')),
                ('Subject_Contents', models.CharField(max_length=255, verbose_name='Subject Contents')),
                ('Assessment_Areas', models.CharField(max_length=255, verbose_name='Assessment Areas')),
                ('sydney_correct_count_percentage', models.FloatField(verbose_name='sydney_correct_count_percentage')),
                ('sydney_average_score', models.FloatField(verbose_name='sydney_average_score')),
                ('sydney_participants', models.IntegerField(verbose_name='sydney_participants')),
                ('student_score', models.FloatField(verbose_name='student_score')),
                ('student_total_assessed', models.IntegerField(verbose_name='student_total_assessed')),
                ('student_area_assessed_score', models.FloatField(verbose_name='student_area_assessed_score')),
                ('total_area_assessed_score', models.FloatField(verbose_name='total_area_assessed_score')),
                ('participant', models.IntegerField(verbose_name='participant')),
                ('correct_answer_percentage_per_class', models.FloatField(verbose_name='correct_answer_percentage_per_class')),
                ('average_score', models.FloatField(verbose_name='average_score')),
                ('school_percentile', models.IntegerField(verbose_name='school_percentile')),
                ('sydney_percentile', models.IntegerField(verbose_name='sydney_percentile')),
                ('strength_status', models.CharField(max_length=255, verbose_name='strength_status')),
                ('high_distinct_count', models.IntegerField(verbose_name='high_distinct_count')),
                ('distinct_count', models.IntegerField(verbose_name='distinct_count')),
                ('credit_count', models.IntegerField(verbose_name='credit_count')),
                ('participant_count', models.IntegerField(verbose_name='participant_count')),
                ('award', models.CharField(max_length=255, verbose_name='award')),
            ],
        ),
    ]
