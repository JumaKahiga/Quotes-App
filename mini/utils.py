import random

def get_random_object(MyModel):
   return random.randrange(1, MyModel.objects.all().count())