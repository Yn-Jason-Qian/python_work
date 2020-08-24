from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from s_blogs.forms import TopicForm, EntryForm
from s_blogs.models import Topic


def index(request):
    return render(request, 's_blogs/index.html')


def topics(request):
    all_topics = Topic.objects.all()
    context = {"topics": all_topics}
    return render(request, "s_blogs/topics.html", context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "s_blogs/topic.html", context)


def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('s_blogs:topics'))
    else:
        form = TopicForm()

    context = {'form': form}
    return render(request, 's_blogs/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse("s_blogs:topic", args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, "s_blogs/new_entry.html", context)