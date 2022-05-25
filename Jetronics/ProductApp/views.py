from asyncio import constants
from Jetronics.importedpage import *



class ProductCategoryViewalluser(ListAPIView):
    serializer_class = ProductCategorySerializer
    def get_queryset(self):
        id = self.request.GET.get("id","")
        datas = ProductCategory.objects.all()
        if id:
            datas = datas.filter(id=id)
        return datas
        

       

class ProductCategoryViewAdmin(ListAPIView):
    serializer_class = ProductCategorySerializer  
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = Mypagination
    def get_queryset(self): 
        name = self.request.GET.get("name","")
        
        datas = ProductCategory.objects.all()
        if name:
            datas = datas.filter(name__icontains = name)
        
        return datas
      
    def post(self,request):
        id= ""
        try:
            id = self.request.data['id']
        except:
            id=""
        print(id)
        if id:
            statuses = ProductCategory.objects.filter(id=id)
            if statuses.count():
                statuses = statuses.first()
            else:
                return Response({
                    "Status" : status.HTTP_404_NOT_FOUND,
                    "Message" : "The Record Was Not Found"
                })
            mandatory = ['name']
            data = Validate(self.request.data,mandatory)
            if data == True:
                serializerdata = ProductCategorySerializer(statuses,data=self.request.data,partial=True)
                serializerdata.is_valid(raise_exception=True)
                serializerdata.save()
                return Response({
                    "Status" : status.HTTP_200_OK,
                    "Message" : "Succesfully Updated"
                })
            else:   
                return Response({
                        "Status" : status.HTTP_400_BAD_REQUEST,
                        "Message" : data
                })
        else:
            mandatory = ['name']
            data = Validate(self.request.data,mandatory)
            if data == True:
                serializerdata = ProductCategorySerializer(data=self.request.data,partial=True)
                serializerdata.is_valid(raise_exception=True)
                serializerdata.save()
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
        # id = self.request.POST.get("id","[]")
        id = self.request.data['id']
   
        # print(id)
        
        
        if id:
            # id= json.loads(id)
            data = ProductCategory.objects.filter(id=id)
            if data.count():
                data = data.delete()
                
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

    

class ProductView(ListAPIView):
    
    serializer_class = ProductSerializer
    pagination_class = Mypagination

    def get_queryset(self):
        
        id = self.request.GET.get("id","")
        name = self.request.GET.get("name","")
        status = self.request.GET.get("status","")
        category = self.request.GET.get("category","")

        allproduct = ProductModel.objects.all().order_by('-id')
        
        if id:
            allproduct = allproduct.filter(id=id)
        
        if name:
            allproduct = allproduct.filter(title__icontains = name)

        if status:
            allproduct = allproduct.filter(status = status)

        if category:
            allproduct = allproduct.filter(category = category)
        
        return allproduct


    def post(self,request):
        try:
            id = self.request.data["id"]
        except:
            id = ""
       
        try:
            category = self.request.data["category"]
        except:
            category = ""

        if id:

            product = ProductModel.objects.filter(id=id)
            if product.count():
                product = product.first()
            else:
                return Response({
                    "Status" : status.HTTP_404_NOT_FOUND,
                    "Message" : "Product Not Exist"
                })

            categorys = ProductCategory.objects.filter(id=category)
            if category:
                if categorys.count():
                    category = categorys.first()
                else:
                    return Response({
                        "Status" : status.HTTP_404_NOT_FOUND,
                        "Message" : "Category Does Not Exist"
                    })
            else:
                category = product.category

            serializer = ProductSerializer(product,data=self.request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(category=category)

            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "update"
            })
        else:
            mandatory = ['category','brand','price','quantity','title','description','status','product_image','code','rank']
            data = Validate(self.request.data,mandatory)
            if data == True:
                try:
                    category = self.request.POST.get("category","")                   
                    categorys = ProductCategory.objects.filter(id=category)
                    if categorys.count():
                        categorys = categorys.first()
                    else:
                        return Response({
                            "Status" : status.HTTP_404_NOT_FOUND,
                            "Message" : "The Record Was Not Found"
                        })

                    serializer = ProductSerializer(data=self.request.data,partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    productid = serializer.data['id']

                   
                    for imagefile in request.FILES.getlist('images'):
                        serializer = MoreProductImageSerializer(data={'productimage':imagefile,'image_id':productid})
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                    
                    else:
                        pass
                
                    return Response({
                        "Status" : status.HTTP_200_OK,
                        "Message" : "Product Succesfully Created"
                    })
                except Exception as e:
                    return Response({
                        "Status" : status.HTTP_400_BAD_REQUEST,
                        "Message" : "Something Went Wrong"
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
            # id= json.loads(id)
            data = ProductModel.objects.filter(id=id)
            if data.count():
                
                for product in data:
                    moreimage = MoreProductImage.objects.filter(image_id=product.id)
                    for images in moreimage:
                        images.delete()
                    
                    product.delete()
     
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



class MoreImageView(ListAPIView):
    def get(self,request):
        id = self.request.GET.get("id","")
        images = MoreProductImage.objects.filter(image_id=id)

        serializer = MoreProductImageSerializer(images,many=True)
        return Response({
            "Status" : status.HTTP_200_OK,
            "Message" : serializer.data
        })

    def post (self,request):
        
        try:
            productid = self.request.data['productid']
        except:
            return Response({
                "Status" : status.HTTP_400_BAD_REQUEST,
                "Message" : "Something went wrong"
            })

        for imagefile in request.FILES.getlist('images'):
            serializer = MoreProductImageSerializer(data={'productimage':imagefile,'image_id':productid})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response({
            "Status" : status.HTTP_200_OK,
            "Message" : "Succesfully Added"
        })


    def delete(self,request):
        id = self.request.GET.get("id","")
        print(id)
        images = MoreProductImage.objects.get(id=id)

        images.delete();
        return Response({
            "Status" : status.HTTP_200_OK,
            "Message" :"Succesfully Deleted"
        })



class StatusUpdateView(ListAPIView):
    
    def post(self,request):
        try:
            id = self.request.data['id']
        except:
            id=""
        
        if id:
            product = ProductModel.objects.filter(id=id)
            if product.count():
                product = product.first()
            else:
                return Response({
                    "Status" : status.HTTP_404_NOT_FOUND,
                    "Message" : "Record Not Found"
                })

            statusnew = product.status
            if statusnew == "Enable":
                product.status = "Disable"
                product.save()
            else:
                product.status = "Enable"
                product.save()

            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Succesfully changed"
            })

        else:
            return Response({
                "Status" : status.HTTP_200_OK,
                "Message" : "Something Went Wrong"
            })



class ProductUser(ListAPIView):
    serializer_class = ProductSerializeruserView
    def get_queryset(self):
        category = self.request.GET.get("category","")
        id = self.request.GET.get("id","")
        allproduct = ProductModel.objects.all()
        EnableProduct = allproduct.filter(status="Enable")
        if category:
            EnableProduct = allproduct.filter(status="Enable",category = category)
        if id:
            self.serializer_class = ProductSerializer
            EnableProduct = allproduct.filter(id=id)
        return EnableProduct