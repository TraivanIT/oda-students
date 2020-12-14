from django.db import models


class Teacher(models.Model):
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
    name = models.CharField(max_length=150)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    dateOfBirth = models.DateTimeField(null=True , blank=True)
    phoneNumber = models.CharField(max_length=100)
    email = models.EmailField()
    oneYearContract = models.BooleanField(default=False)
    collegeContract = models.BooleanField(default=False)
    masterContract = models.BooleanField(default=False)
    graduateCollege = models.BooleanField(default=False)
    image = models.ImageField(upload_to='teacher/images/')

    def __str__(self):
        return self.name


class SchoolName(models.Model):
    ODA_SCHOOL_NAMES = (

        ('1', 'ODA School 01',),
        ('2', 'ODA School 02',),
        ('3', 'ODA School 03',),
        ('4', 'ODA School 04',),
        ('5', 'ODA School 05',),
        ('6', 'ODA School 06',),
        ('7', 'ODA School 07',),
        ('8', 'ODA School Center',),
    )
    schoolName = models.CharField(
        max_length=1,
        choices=ODA_SCHOOL_NAMES
    )
    image = models.ImageField(upload_to='school/images/')
    description = models.TextField()

    def __str__(self):
        return self.schoolName


class Book(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='book/images/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Classes(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='class/images/')
    description = models.TextField()

    def __str__(self):
        return self.name



class Teaching(models.Model):
    teacherName = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    schoolName = models.ForeignKey(SchoolName, on_delete=models.CASCADE)
    className = models.ForeignKey(Classes, on_delete=models.CASCADE)
    bookName = models.ForeignKey(Book, on_delete=models.CASCADE)


class Student(models.Model):
    nameInKhmer = models.CharField(max_length=250)
    nameInEnglish = models.CharField(max_length=250)
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
    )
    dateOfBirth = models.DateField()
    enrollDate = models.DateField()
    phoneNumber = models.CharField(max_length=150)
    email = models.EmailField()

    FAMILY_SITUATION_CHOICES = (
        ('1', 'Poor'),
        ('2', 'Midle'),
        ('3', 'Rich'),

    )
    familySituation = models.CharField(
        max_length = 1,
        choices = FAMILY_SITUATION_CHOICES,
    )
    studyComputer = models.BooleanField(default=False)
    graduted = models.BooleanField(default=False)
    uniformProject = models.BooleanField(default=False)
    teacherName = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    schoolName = models.ForeignKey(SchoolName, on_delete=models.CASCADE)
    className = models.ForeignKey(Classes, on_delete=models.CASCADE)
    bookName = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student/images/')
    finishWithODA = models.DateField(null= True ,blank=True)
    haveJob = models.BooleanField( default=False)
    jobName = models.CharField(max_length=250, blank=True)
    jobDescription = models.TextField(blank=True)
    studentFeedback = models.TextField(blank=True)
