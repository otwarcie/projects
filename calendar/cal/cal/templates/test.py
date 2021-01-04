def add_meeting(request):
    add_meeting_form = AddMeetingForm(request.POST or None)
    site = Site.objects.get(user=request.user.id)

    if request.method == "POST":
        if add_meeting_form.is_valid():
            obj = add_meeting_form.save(commit=False)
            obj.site = site
            obj.save()

            # create an instance of 'MeetingArrival' object
            meeting_arrival_obj = MeetingArrival(meeting=obj, visitor=<your_visitor_object_here>, arrival_status=True)
            meeting_arrival_obj.save() # save the object in the db



beatles.members.add(john, through_defaults={'date_joined': date(1960, 8, 1)})
beatles.members.create(name="George Harrison", through_defaults={'date_joined': date(1960, 8, 1)})
beatles.members.set([john, paul, ringo, george], through_defaults={'date_joined': date(1960, 8, 1)})
