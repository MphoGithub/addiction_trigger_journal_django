import random
from django.shortcuts import render,redirect, get_object_or_404
from .models import Trigger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TriggerForm

# Create your views here.
def index(request):
   quotes = [
       #Dr Gabor Mate Quotes
        """Not all addictions are rooted in abuse or trauma, 
        but I do believe they can all be traced to painful experience. 
        A hurt is at the centre of all addictive behaviours. 
        It is present in the gambler, the Internet addict, 
        the compulsive shopper and the workaholic. 
        The wound may not be as deep and the ache not as excruciating, and it may even be entirely hidden—but it’s there. As we’ll see, the effects of early stress or adverse experiences directly shape both the psychology and the 
        neurobiology of addiction in the brain.- Dr Gabor Mate""",
        """It is impossible to understand addiction 
        without asking what relief the addict finds, 
        or hopes to find, in the drug or the addictive behaviour.- Dr Gabor Mate""",
        "Passion creates, addiction consumes.- Dr Gabor Mate",  
        
   ]
   
   quote = random.choice(quotes)
   return render(request,'triggers/index.html',{'quote':quote})

@login_required
def add_trigger(request):
    if request.method == 'POST':
        form = TriggerForm(request.POST)
        
        if form.is_valid():
            trigger = form.save(commit=False) #Dont save to db before add user who created the trigger
            trigger.user = request.user #Link trigger to user
            trigger.save()
            messages.success(request,"Trigger added!")
            return redirect('view_triggers')
    else:
        form = TriggerForm()
    context = {'form':form}
    return render(request,'triggers/add_trigger.html',context)

@login_required
def view_triggers(request):
    triggers = Trigger.objects.filter(user=request.user).order_by('-date_logged')
    return render(request,'triggers/view_triggers.html',{'triggers':triggers})

@login_required
def edit_trigger(request,trigger_id):
    trigger = get_object_or_404(Trigger,id=trigger_id,user=request.user) #Fetch Trigger object from db
    
    if request.method == 'POST':
        form = TriggerForm(request.POST,instance = trigger)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trigger updated successfully.')
            return redirect('view_triggers')
    
    else:
        form = TriggerForm(instance=trigger)
    return render(request, 'triggers/add_trigger.html', {'form': form, 'edit': True, 'trigger':trigger})

@login_required
def delete_trigger(request, trigger_id):
    trigger = get_object_or_404(Trigger, id=trigger_id, user=request.user)
    if request.method == 'POST':
        trigger.delete()
        messages.success(request, 'Trigger deleted successfully.')
        return redirect('view_triggers')
    return render(request, 'triggers/delete_trigger.html', {'trigger': trigger})