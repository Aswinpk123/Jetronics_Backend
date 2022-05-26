from functools import partial
from django.shortcuts import render
from Jetronics.importedpage import *

# Create your views here.

class MissingOrderView(ListAPIView):
    serializer_class=MissingOrderSerializer

    def get_queryset(self):
        id = self.request.GET.get("id","")
        allmissingorder = MissingOrder.objects.all()
        if id :
            allmissingorder = allmissingorder.filter(id=id)

        return allmissingorder

    
    def post(self,request):

        try:
            product = self.request.data['product']
        except:
            product =""

        if product:
            productdetails = ProductModel.objects.filter(id=product)
            if productdetails.count():
                productdetails = productdetails.first()
            else:
                return Response({
                    "Status" : status.HTTP_404_NOT_FOUND,
                    "Message" : "Record Not Found"
                })
            serializer = MissingOrderSerializer(data=self.request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(product=productdetails)

            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Data Created Succesfully"
            })
        else:
            serializer = MissingOrderSerializer(data=self.request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Data Created Succesfully"
            })



class OrderViews(ListAPIView):
    serializer_class = OrderSerializer
    pagination_class = Mypagination
    def get_queryset(self):
        id = self.request.GET.get("id","")
        userrandomid = self.request.GET.get("userrandomid","")
        allorder = OrderModel.objects.all()
        if id:
            allorder = allorder.filter(id=id)
        if userrandomid :
            allorder = allorder.filter(userrandomid=userrandomid)

        return allorder


    def post(self,request):
        try:
            id = self.request.data['id']
        except:
            id =""
        
        if id:
            pass
        else:
            mandatory = ['clientname','phone','city','quantity','address']
            data = True
            if data==True:
                try:
                    settingsvalue = OrderSettingsModel.objects.get(key=1)
                    orderid = settingsvalue.value
                except:
                    settings = OrderSettingsModel.objects.create(value=1000,key=1)
                    orderid = settings.value



                alldata = self.request.data
                alldata['orderid'] = "JT" + str(orderid)
                alldata['status'] = 5
                

                try:
                    serializer = OrderSerializer(data=alldata,partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    
                    saved_data = serializer.data


                    newsettingsvalue = OrderSettingsModel.objects.get(key=1)
                    newsettingsvalue.value = int(orderid) + 1
                    newsettingsvalue.save()
                except:
                    pass

                print(saved_data['id'])

                duplicatemissingorder = MissingOrder.objects.filter(product=saved_data['product_id'],clientname=saved_data['clientname'],phone=saved_data['phone'],city=saved_data['city'])
                if duplicatemissingorder.count():
                    duplicatemissingorder.first().delete()
                else:
                    pass


                return Response({
                    "Status" : status.HTTP_200_OK,
                    "Message" : "Order Placed Succesfully"
                })
            else:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : data
                })