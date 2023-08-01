from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from learning_logs.forms import TopicForm, EntryForm
from learning_logs.models import Topic, Entry


# Create your views here.
def index(request):
    """Página de Inicio para Learning Log."""
    return render(request, 'learning_logs/index.html')


@login_required
def getTopics(request):
    """Mostrar todos los tópicos."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def getTopic(request, topic_id):
    """Despliega la información de un topic."""
    topic = Topic.objects.get(id=topic_id)
    # Solo se puede visualizar los datos del usuario dueño de los datos
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'learning_logs/topic.html', context)


@login_required
def newTopic(request):
    """Agregar un nuevo topic."""

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:getTopics')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/newTopic.html', context)


@login_required
def newEntry(request, topic_id):
    """Agregar una nueva entrada."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Crea un formulario en blanco
        form = EntryForm()
    else:
        # Se hace submit, se procesa los datos
        form = EntryForm(data=request.POST)
        if form.is_valid():
            newEntry = form.save(commit=False)
            newEntry.topic = topic
            newEntry.save()
            return redirect('learning_logs:getTopic', topic_id=topic_id)

    # Se despliega un formulario en blanco
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/newEntry.html', context)


@login_required
def editEntry(request, entry_id):
    """Modificar una entrada."""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Se cargan el formulario con los datos de la entrada
        form = EntryForm(instance=entry)
    else:
        # Se hace submit, se procesa los datos
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:getTopic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/editEntry.html', context)


@login_required
def removeEntry(request, entry_id):
    """Remover una entrada."""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    entry.delete()
    return redirect('learning_logs:getTopic', topic_id=topic.id)

def handler404(request, *args, **argv):
    """Método para manejar los errores 404"""
    response = render('learning_logs/404.html', {})
    response.status_code = 404
    return response
