from functools import partial
from Jetronics.importedpage import *

# Create your views here.

class StatusView(ListAPIView):
    serializer_class = StatusSerializer
    def get_queryset(self):
        id = self.request.GET.get("id","")
        allstatus = StatusModel.objects.all()
        if id:
            allstatus = allstatus.filter(id=id)
        return allstatus

    def post(self,request):
        try:
            id = self.request.data['id']
        except:
            id=""

        if id:
            statusdata = StatusModel.objects.filter(id=id)
            if statusdata.count():
                statusdata = statusdata.first()
            else:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : "No Record Found"
                })

            serializer = StatusSerializer(statusdata,data=self.request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Data Succesfully Updated"
            })

        else:
            mandatory = ['name','colour']
            data = Validate(self.request.data,mandatory)

            if data == True:
                serializer = StatusSerializer(data=self.request.data,partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return Response({
                    "Status" : status.HTTP_200_OK,
                    "Message" : "Succesfully Created"
                })
            else:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : data
                })

    def delete(self,request):
        try:
            id = self.request.GET.get('id')
        except:
            id=""
       
        if id:
      
            data = StatusModel.objects.filter(id=id)
            if data.count():
                
                data.delete()
     
                return Response({
                    "Status" : status.HTTP_200_OK,
                    "Message" : "Data Succesfully Deleted"
                })
            else:
                return Response({
                    "Status" : status.HTTP_404_NOT_FOUND,
                    "Message" : "Record Not Found"
                })
   
        else:
        
            return Response({
                    "Status" : False,
                    "Message" : "Provide Valid Information"
                }) 