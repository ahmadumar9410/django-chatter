from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Contact, Message
from django.contrib import messages
# Create your views here.


def home(request):
    username = request.user.get_username()
    userContact = Contact.objects.filter(username=username)
    friendList = None
    if len(userContact) > 0:
        friendList = userContact[0].friends.all()
    showcasename = retunShowCaseName(request)
    if request.method == 'POST':
        reply = request.POST['reply']
        message = Message.objects.create(
            from_username=username, to_username='ahmad', message=reply)
        message.save()
        messages.success(request, 'Message successfully set')
        print('we some how reached here')
        return redirect("/dashboard/")
    # for user in userContact:
    #     print(user.friends)
    print()

    return render(request, 'index.html',
                  context={'showcasename': showcasename,
                           'friendList': friendList
                           })


def chat(request, slug):
    username = request.user.get_username()
    print("Calling Here")
    userContact = Contact.objects.filter(username=username)
    friendList = None
    if len(userContact) > 0:
        friendList = userContact[0].friends.all()
    showcasename = retunShowCaseName(request)
    if request.method == 'POST':
        reply = request.POST['reply']
        message = Message.objects.create(
            from_username=username, to_username=slug, message=reply)
        message.save()
        messages.success(request, 'Message successfully sent')
        print('we some how reached here')
        return redirect("/dashboard/"+slug)
    messages1 = returnMessages(username, slug)
    # for user in userContact:
    #     print(user.friends)
    print(messages1)

    return render(request, 'index.html',
                  context={'showcasename': showcasename,
                           'messages': messages1,
                           'friendList': friendList
                           })


def returnMessages(username, reciever_username):
    """
    messageManagement of dashboard is handled here
    """
    messageyousent = Message.objects.filter(
        from_username=username, to_username=reciever_username)
    messageyourecieved = Message.objects.filter(
        to_username=username, from_username=reciever_username)
    messages = messageyousent.union(messageyourecieved).order_by('time_stamp')
    return messages


def retunShowCaseName(request):

    if request.user.get_full_name() == '':
        showcasename = request.user.get_username()
    else:
        showcasename = request.user.get_full_name()

    return showcasename


def messageSendingProcedure(request, username, to_username):
    if request.method == 'POST':
        reply = request.POST['reply']
        message = Message.objects.create(
            from_username=username, to_username=to_username, message=reply)
        message.save()
        messages.success(request, 'Message successfully set')
        print('we some how reached here')
        return redirect("/login/")
