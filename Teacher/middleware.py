__author__ = 'ouakira'


class AddTeacher(object):

    def process_request(self, request):

        print "request_uri: %s", request.get_raw_uri()

        name = request.POST.get('name', None)
        time_0 = request.POST.get('time_0', None)
        teacher = request.user
        print "teacher: %s name: %s, time: %s" % (teacher, name, time_0)

        print dir(request)
