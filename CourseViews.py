from django.shortcuts import render
from django.utils import timezone
from MyORM.models import *
from MyORM.Youtube.CourseForm import *

def TopicView(request):
    if(request.method=="GET"):
       topiclist=Topics.objects.all()
       topic_form=TopicForm()
       return render(request,"Topics.html",{"stopic":topic_form,"Topicss":topiclist})
    if(request.method=="POST"):
       topic=TopicForm(request.POST,request.FILES)
       if(topic.is_valid()):
           topic.save()
           topiclist=Topics.objects.all()
           topic_form=TopicForm()
       return render(request,"Topics.html",{"stopic":topic_form,"msg":"Topic added Successfully...","Topicss":topiclist})

# def GetTopicView(request):
#        topiclist=Topics.objects.all()
#        return render(request,"ListTopics.html",{"Topics":topiclist})
 
# def ViewContentView(request):
#         tid=request.GET["topic_id"]
#         topic=Topics.objects.get(id=tid)
#         contents=TopicContent.objects.filter(Topic=topic)
#         print(contents)
#         return render(request,"ViewContents.html",{"contents":contents})

# def PlayVideoView(request):
#     cid=request.GET["content_id"]

#     content =TopicContent.objects.get(id=cid)
#     contents=TopicContent.objects.filter(Topic=content.Topic)
     
#     return render(request,"PlayContentVideo.html",{"c":content,"contents":contents})


def UserView(request):
    if(request.method=="GET"):
       userlist=Users.objects.all()
       user_form=UsersForm()
       return render(request,"Users.html",{"suser":user_form,"Users":userlist})
    if(request.method=="POST"):
       user=UsersForm(request.POST,request.FILES)
       if(user.is_valid()):
           user.save()
           user_form=UsersForm()
           userlist=Users.objects.all()
       return render(request,"Users.html",{"suser":user_form,"msg":"User added Successfully...","Users":userlist})

def TopicContentView(request):
    if(request.method=="GET"):
       topiccontentlist=TopicContent.objects.all()
       topiccontent_form=TopicContentForm()
       return render(request,"TopicContents.html",{"tcontent":topiccontent_form,"TopicContent":topiccontentlist})
    if(request.method=="POST"):
       topiccontent_form=TopicContentForm(request.POST,request.FILES)
       if(topiccontent_form.is_valid()):
           topiccontent_form.save()
           topiccontent_form=TopicContentForm()
           topiccontentlist=TopicContent.objects.all()
       return render(request,"TopicContents.html",{"tcontent":topiccontent_form,"msg":"Topic content added Successfully...","TopicContent":topiccontentlist})

def TopicContentCommentsView(request):
    if(request.method=="GET"):
       tcclist=TopicContentComments.objects.all()
       tccform=TopicContentCommentsForm()
       return render(request,"TopicContentComments.html",{"tcontentcomment":tccform,"TopicContentComments":tcclist})
    if(request.method=="POST"):
       tccform=TopicContentCommentsForm(request.POST,request.FILES)
       tcclist = TopicContentComments.objects.all() 
       if(tccform.is_valid()):
           tccform.save()
           tccform=TopicContentCommentsForm()
        #    tcclist=TopicContentComments.objects.all()
       return render(request,"TopicContentComments.html",{"tcontentcomment":tccform,"msg":"Topic content comments added Successfully...","TopicContentComments":tcclist})


def LoginView(request):
    if(request.method=="GET"):
        login_from=LoginForm()
        return render(request,"Login.html",{"loginf":login_from})
    if(request.method=="POST"):
        u_name=request.POST["user_name"]
        u_password=request.POST["password"]

        data=Users.objects.filter(user_name=u_name,password=u_password)
        if data.exists():
                return render(request,"Topics.html",{"msg":"User login Successfully"})
        else:
                login_from=LoginForm()
                return render(request,"Users.html",{"loginf":login_from,"msg":"User login Failed"})

def getcontentView(request):
   tid=request.GET["topic_id"]
   topic=Topics.objects.get(id=tid)
   contents=TopicContent.objects.filter(Topic=topic)
   return render(request,"Topicsandrelcontent.html",{"contents":contents})

def displayvideoView(request):
    cid=request.GET["content_id"]
    content=TopicContent.objects.get(id=cid)
    contents=TopicContent.objects.filter(Topic=content.Topic)
    return render(request,"Topicsandrelcontent.html",{"c":content,"contents":contents})

def displaycomments(request):
    cid=request.GET["content_id"]
    content=TopicContent.objects.get(id=cid)
    contents=TopicContent.objects.filter(Topic=content.Topic)
    comments=TopicContentComments.objects.filter(Content=content).order_by('-CommentDate')   
    if(request.method=="POST"):
        form=TopicContentCommentsForm(request.POST)
        if(form.is_valid()):
            comment=form.save()
            comment.Content=content
            comment.User=Users.objects.first()
            comment.CommentDate=timezone.now()   
            comment.save()
            return render(request,"displayvideo?content_id={cid}")
    form=TopicContentCommentsForm()
    return render(request,"Topicsandrelcontent.html",{"c":content,"comm":comments,"comment_form":form})

        