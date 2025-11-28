from django.db import models

# Create your models here.
# class Student(models.Model):
#     firstname=models.CharField(max_length=50)
#     lastname=models.CharField(max_length=50)
#     qualification=models.CharField(max_length=40)
#     fees=models.FloatField()
#     class Meta:
#         db_table="student_details"
      

# class Employee(models.Model):
#     Employee_name=models.CharField(max_length=40)
#     Designation=models.CharField(max_length=30)
#     Joining_date=models.DateField()
#     Salary=models.FloatField()
#     class Meta:
#         db_table="Employee_details"

# class State(models.Model):
#     StateName=models.CharField(max_length=30)
#     StateCode=models.IntegerField()
#     class Meta:
#         db_table="State_details"
#         ordering=("StateName",)

# class City(models.Model):
#     CityName=models.CharField(max_length=30)
#     CityCode=models.IntegerField()
#     state=models.ForeignKey(State,related_name="cities",on_delete=models.CASCADE)
#     class Meta:
#         db_table="City_details"
#         ordering=("CityName",)        

# class ProductModel(models.Model):
#     productName=models.CharField(max_length=50)
#     rate=models.FloatField()
#     gst=models.FloatField()
#     stockQuantity=models.IntegerField()
#     description=models.TextField()
#     photo=models.ImageField(default="abc.png",blank=True)
#     productvideo=models.FileField(default="abc.mp4",blank=True)
#     class Meta:
#         db_table="tblproducts"
# -------------------------------------------------------------------------------------------------------------------------------------------------

class Topics(models.Model):
    Topic_id=models.IntegerField()
    Topic_name=models.CharField(max_length=50)
    class Meta:
        db_table="tblTopics"
        ordering=("Topic_id",) 
    def __str__(self):
        return self.Topic_name
    
class TopicContent(models.Model):
    ContentName=models.CharField(max_length=100)
    Topic=models.ForeignKey(Topics,related_name="topics", on_delete=models.CASCADE)
    videofile=models.FileField(default="abc.mp4",blank=True)   
    class Meta:
        db_table="tbltopic_contents"
        ordering=("Topic",)
    def __str__(self):
        return self.ContentName    

class Users(models.Model):
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=20)
    qualification=models.CharField(max_length=30)
    email_address=models.CharField(max_length=30)
    mobile_number=models.CharField(max_length=14)
    password=models.CharField(max_length=20)
    class Meta:
        db_table="tblUsers"
        ordering=("user_id",)
    def __str__(self):
        return self.user_name

class TopicContentComments(models.Model):
    User=models.ForeignKey(Users,related_name="comments",on_delete=models.CASCADE)
    Content=models.ForeignKey(TopicContent,related_name="comments",on_delete=models.CASCADE)
    CommentDate=models.DateTimeField()
    CommentMessage=models.CharField(max_length=400) 
    class Meta:
        db_table="tblcontent_comments"
        ordering=("User",)
    def __str__(self):
        return self.Content



