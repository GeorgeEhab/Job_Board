#### views of data ,function return data as a json response
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

## Function Based View ##
@api_view(['GET'])
def job_list_api(request):
    # print(request) #<rest_framework.request.Request: GET '/jobs/api/list'>
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many=True).data  # convert data to json
    return Response({'data':data})

@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = Job.objects.get(id = id)
    data = JobSerializer(job_detail).data  # convert data to json
    return Response({'data':data})

########################################################
## Generic(Class based) View ##
from rest_framework import generics

class JobList(generics.ListCreateAPIView):
    # model = Job
    queryset = Job.objects.all()
    serializer_class = JobSerializer


    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = JobSerializer(queryset, many=True)
    #     return Response(serializer.data)

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'

