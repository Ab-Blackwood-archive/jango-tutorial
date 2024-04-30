from django.db import models

# Create your models here.
class Student(models.Model):

    GRADES =(
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
    )
    
    GENDER =(
        ('M','M'),
        ('F','F'),
        ('NB','NB'),
    )
    
    CLUB =(
        ('none','none'),
        ('art','art'),
        ('photography','photography'),
        ('videogames','videogames'),
        ('woodworking','woodworking'),
        ('poetry','poetry'),
        ('debate','debate'),
        ('band','band'),
        ('robotics','robotics'),
        ('soccer','soccer'),
        ('chess','chess'),
        ('gardening','gardening'),
        ('theater','theater'),
    )

    firstname = models.CharField(max_length=200, null =True)
    lastname = models.CharField(max_length=200, null =True)
    middlename = models.CharField(max_length=200, null =True)
    gender = models.CharField(max_length=200, null =True, choices=GENDER)
    grade = models.CharField(max_length=200, null =True, choices=GRADES)
    club = models.CharField(max_length=200, null =True, choices=CLUB)

    def __str__(self): 
        return "" + str(self.lastname) + ", " + str(self.firstname) + " Grade " + str(self.grade) + " Club " + str(self.club)

class Teacher(models.Model):
    
    SUBJECTS =(
        ('English','English'),
        ('History','History'),
        ('Art','Art'),
        ('Music','Music'),
        ('Gym','Gym'),
        ('Math','Math'),
        ('Science','Science'),
        ('Elective','Elective'),
    )

    GENDER =(
        ('M','M'),
        ('F','F'),
        ('NB','NB'), 
    ) 

    CLUB =(
        ('none','none'),
        ('art','art'),
        ('photography','photography'),
        ('videogames','videogames'),
        ('woodworking','woodworking'),
        ('poetry','poetry'),
        ('debate','debate'),
        ('band','band'),
        ('robotics','robotics'),
        ('soccer','soccer'),
        ('chess','chess'),
        ('gardening','gardening'),
        ('theater','theater'),
    )
    
    
    firstname = models.CharField(max_length=200, null =True)
    lastname = models.CharField(max_length=200, null =True)
    middlename = models.CharField(max_length=200, null =True)
    gender = models.CharField(max_length=200, null =True, choices=GENDER)
    roomnum = models.CharField(max_length=500, null =True)
    subject = models.CharField(max_length=200, null =True, choices=SUBJECTS)
    club = models.CharField(max_length=200, null =True, choices=CLUB)

    def __str__(self): 
        return "" + str(self.lastname) + ", " + str(self.firstname) + " Subject-- " + str(self.subject) + ", Room Number " + str(self.roomnum)





