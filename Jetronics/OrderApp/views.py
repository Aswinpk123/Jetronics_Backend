
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

    def delete(self,request):
       
        id = self.request.GET.get("id","")
        
        if id:
            datas = MissingOrder.objects.filter(id=id)
            if datas.count():
                datas.first().delete()

            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Succesfully Deleted"
            })
        else:
            return Response({
                "Status" : status.HTTP_400_BAD_REQUEST,
                "Message" : "No ID FOUND"
            })


class OrderViews(ListAPIView):
    serializer_class = OrderSerializer
    pagination_class = Mypagination
    def get_queryset(self):

        id = self.request.GET.get("id","")
        statuscode = self.request.GET.get("statuscode","")
        userrandomid = self.request.GET.get("userrandomid","")
        productname = self.request.GET.get("productname","")
        allorder = OrderModel.objects.all()
        if id:
            allorder = allorder.filter(id=id)
        if userrandomid :
            allorder = allorder.filter(userrandomid=userrandomid)
        if statuscode:
            allorder = allorder.filter(status__statuscode = statuscode)
        if productname:
            allorder = allorder.filter(product_name__icontains = productname)

        return allorder

    
    
    def post(self,request):
        try:
            id = self.request.data['id']
        except:
            id =""
    
        if id:
            orderdata = OrderModel.objects.filter(id=id)
            if orderdata.count():
                orderdata = orderdata.first()
            else:
                return Response({
                    "Status" : status.HTTP_404_NOT_FOUND,
                    "Message" : "The Record Was Not Found"
                })

            serializer = OrderSerializer(orderdata,data=self.request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Succesfullly Updated"
            })
        else:
            mandatory = ['clientname','phone','city','address']
            data = Validate(self.request.data,mandatory)
            saved_data = {}
            if data==True:
                print("112355565",self.request.data)
                try:
                    settingsvalue = OrderSettingsModel.objects.get(key=1)
                    orderid = settingsvalue.value
                except:
                    settings = OrderSettingsModel.objects.create(value=1000,key=1)
                    orderid = settings.value



                alldata = self.request.data
                alldata['orderid'] = "JT" + str(orderid)
                statusvalue = StatusModel.objects.filter(statuscode=5)
                if statusvalue.count():
                    statusvalue = statusvalue.first()
                else:
                    return Response({"Status" : status.HTTP_404_NOT_FOUND,"Message" : "Order Status is Not Getting"})

                

                try:
                    serializer = OrderSerializer(data=alldata,partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save(status=statusvalue)
                    
                    saved_data = serializer.data

                    print(saved_data)

                    newsettingsvalue = OrderSettingsModel.objects.get(key=1)
                    newsettingsvalue.value = int(orderid) + 1
                    newsettingsvalue.save()
                except:
                    pass


                duplicatemissingorder = MissingOrder.objects.filter(product__id=saved_data['product_id'],clientname=saved_data['clientname'],phone=saved_data['phone'],city=saved_data['city'])
                if duplicatemissingorder.count():
                    duplicatemissingorder.first().delete()
                else:
                    pass
                
                
                missingorder = MissingOrder.objects.filter(userrandomid = saved_data['userrandomid'])
                if missingorder.count():
                    missingorder.first().delete()
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

    def delete(self,request):
        print(self.request.GET.get("id",""))
        id = self.request.GET.get("id","")
        if id:
            datas = OrderModel.objects.filter(id=id)
            if datas.count():
                datas.first().delete()

            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Succesfully Deleted"
            })
        else:
            return Response({
                "Status" : status.HTTP_400_BAD_REQUEST,
                "Message" : "No ID FOUND"
            })



class StatusChange(ListAPIView):
    def post(self,request):
        try:
            id = self.request.data['id']
        except:
            id = ""
        try:
            statuscode = self.request.data['statuscode']
        except:
            statuscode =""

        if id:
            order = OrderModel.objects.filter(id=id)
            if order.count():
                order = order.first()

            else:
                return Response({
                    "Status" : status.HTTP_404_NOT_FOUND,
                    "Message" : "Record Not Found"
                })

            if statuscode:
                statusdata = StatusModel.objects.filter(statuscode = statuscode)
                if statusdata.first():
                    statusdata = statusdata.first()
                else:
                    return Response({
                    "Status" : status.HTTP_404_NOT_FOUND,
                    "Message" : "Record Not Found"
                    })
            else:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : "No Status code is present"
                })


            serializer = OrderSerializer(order,data=self.request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(status=statusdata)


            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Succesfully Changed"
            })

        else:
            return Response({
                "Status" : status.HTTP_400_BAD_REQUEST,
                "Message" : "Something went wrong"
            })

class StatusChangeMultiply(ListAPIView) :

    
    def post(self,request):

        try:
            id = self.request.data['id']
        except:
            id=[]
        try:
            statuscode = self.request.data['statuscode']
        except:
            statuscode = 5

        if id:
            if statuscode:
                statusdata = StatusModel.objects.filter(statuscode = statuscode)
                if statusdata.count():
                    statusdata= statusdata.first()
            
            for x in id:
                orderdata = OrderModel.objects.filter(id=x).update(status = statusdata)
            
            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Status is succesfully Changed"
            })
        else:
            return Response({
                "Status" : status.HTTP_400_BAD_REQUEST,
                "Message" : "Product is not getting"
            })





class Getorderwithphone(ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        phone = self.request.GET.get("phone","")
        orders = OrderModel.objects.all()

        if phone:
            orders = orders.filter(phone=phone)

        return orders


class CsvReportView(ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        print(self.request.data)
        all = OrderModel.objects.all()
        return all
   
    def post(self,request):
        try:
            id = self.request.data['id']
        except:
            id = []

        print(id)
        if id :

            reportorder = OrderModel.objects.filter(id__in = id)

            serializer = OrderSerializer(reportorder,many=True)
            return Response({
                "Status" : "ok",
                "data" : serializer.data
            })
        else:
            reportorder = OrderModel.objects.all()

            serializer = OrderSerializer(reportorder,many=True)
            return Response({
                "Status" : "ok",
                "data" : serializer.data
            })
       
class MissingorderCsvReportView(ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        print(self.request.data)
        all = MissingOrder.objects.all()
        return all
   
    def post(self,request):
        try:
            id = self.request.data['id']
        except:
            id = []

        print(id)
        if id :

            reportorder = MissingOrder.objects.filter(id__in = id)

            serializer = MissingOrderSerializer(reportorder,many=True)
            return Response({
                "Status" : "ok",
                "data" : serializer.data
            })
        else:
            reportorder = MissingOrder.objects.all()

            serializer = MissingOrderSerializer(reportorder,many=True)
            return Response({
                "Status" : "ok",
                "data" : serializer.data
            })

class Getorderwithuser(ListAPIView):
    
    def get(self,request):
        orderid = self.request.GET.get("orderid","")
        if orderid: 
            orderwithid = OrderModel.objects.filter(orderid=orderid)
            if orderwithid.count():
                singledata = orderwithid.first()
                userrandomid = singledata.userrandomid
            
            print(userrandomid)
            orders = OrderModel.objects.filter(userrandomid=userrandomid)

            allserializer = OrderSerializer(orders,many=True)
            singleserializer = OrderSerializer(singledata)
        return Response({
            "Status" : status.HTTP_200_OK,
            "alldata" : allserializer.data,
            "singledata" : singleserializer.data
        })


class DeletMultipleMissingOrder(ListAPIView):

    def delete(self,request):

        try:
            ids  = self.request.data['ids']
        except:
            ids = []

        if ids:
            Missingorders = MissingOrder.objects.filter(id__in = ids)
            if Missingorders.count():
                Missingorders.delete()

            return Response({"Status":status.HTTP_200_OK,"Message":"Succesfully Deleted"})
        else:
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Bad Request"})


class allOrder(ListAPIView):
    serializer_class = MultipleorderSerializer
    def get_queryset(self):
        allorder = OrderModel.objects.all()
        return allorder