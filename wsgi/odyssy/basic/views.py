from django.shortcuts import render

from announcement.models import Announcement
from events.models import Event


def index(request):
    """ Index page of the Website """
    latest_announcement = Announcement.get_latest_announcements(5)
    events_list = Event.get_latest_events(3)
    context = {
        'latest_announcement': latest_announcement,
        'events': events_list,
    }
    return render(request, 'basic/index.html', context)