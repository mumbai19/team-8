# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    theme = models.CharField(max_length=255)
    activity_name = models.CharField(max_length=255)
    activity_description = models.CharField(max_length=255)
    mentor = models.ForeignKey('Mentor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'activity'


class Attendance(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING)
    mentor = models.ForeignKey('Mentor', models.DO_NOTHING)
    attendance_date = models.DateField()
    present = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attendance'
        unique_together = (('student', 'mentor'),)


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'course'


class Evaluate(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING)
    mentor = models.ForeignKey('Mentor', models.DO_NOTHING)
    assessment_name = models.CharField(max_length=255)
    assesment_month = models.CharField(max_length=255)
    assessment_level = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'evaluate'
        unique_together = (('student', 'mentor'),)


class Mentor(models.Model):
    user = models.OneToOneField(User)
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mentor'


class Saving(models.Model):
    saving_id = models.AutoField(primary_key=True)
    savings = models.IntegerField()
    student = models.ForeignKey('Student', models.DO_NOTHING)
    saving_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'saving'


class Stars(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING)
    mentor = models.ForeignKey(Mentor, models.DO_NOTHING)
    attribute = models.CharField(max_length=255)
    no_stars = models.IntegerField()
    star_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'stars'
        unique_together = (('student', 'mentor'),)


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    parent_name = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.IntegerField()
    standard = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mentor = models.ForeignKey(Mentor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student'
