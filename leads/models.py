from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    # models.CASCADE                    => IF AGENT IS DELETED, LEAD WILL BE DELETED
    # models.SET_NULL, null=True        => IF AGENT IS DELETED, AGENT WILL SET TO NULL
    # models.SET_DEFAULT, default=xxx   => IF AGENT IS DELETED, ASSIGN DEFAULT AGENT

    # SOURCE_CHOICES = (
    #     ('YouTube','YouTube')
    #     ('Google','Google')
    #     ('Newsletter','Newsletter')
    # )

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)