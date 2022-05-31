from Jetronics.importedpage import *

# Create your views here.

class UserView(ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = Mypagination
    def get_queryset(self): 
         
        user = UserDetailsModel.objects.all().order_by('-id')
        return user
       
    def post(self,request):  
        print(self.request.data)      
        user_obj = ""  
        try:      
            id = self.request.data["id"]
        except:
            id = ""   
        if id:
           
            if id.isdigit():
                
                try:
                    user = UserDetailsModel.objects.filter(id=id)
                    if user.count():
                        user = user.first()
                    else:
                        return Response({
                            "Status" : status.HTTP_404_NOT_FOUND,
                            "Message" : "User Not Found"
                        })

                    serializer = UserSerializer(user,data=request.data,partial=True)
                    serializer.is_valid(raise_exception=True)
                    try:
                        password = self.request.data['password']
                    except:
                        password = ""
                   
                    if password  :
                        msg="User details and password updated Succesfully"
                        user_obj = serializer.save(password=make_password(password))
                    
                    else:
                        msg="User details updated Succesfully"
                        user_obj = serializer.save()
                    
    
                    
                    return Response({
                            "Status":status.HTTP_200_OK,
                            "Message":msg
                        })

                except Exception as e:
                    print(f"Excepction occured {e}")

                    return  Response({
                        "Status":status.HTTP_400_BAD_REQUEST,
                        "Message":f"Excepction occured {e}"
                    })
            else:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : "Please Provide Valid User"
                })
        else:
            mandatory = ['username','password','mobile','address','gender','dob']
            data = Validate(self.request.data,mandatory)
            if data == True:
        
                
                try:      
                    
                    serializer = UserSerializer(data=request.data, partial=True)
                    serializer.is_valid(raise_exception=True)
                
                    msg = "Created New User"
                    user_obj = serializer.save(password=make_password(self.request.data['password']))

                    return Response({
                        "Status":status.HTTP_200_OK,
                        "Message":msg
                    })

                except Exception as e:
                    print(f"Excepction occured {e}")

                    if user_obj:
                        user_obj.delete()

                    return  Response({
                        "Status":status.HTTP_400_BAD_REQUEST,
                        "Message":f"Excepction occured {e}"
                    })
            
            else:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : data
                })


    def delete(self,request):
        id = self.request.POST.get('id','[]')
       
        if id:
            try:
                
                id = json.loads(id)
                objects = UserDetailsModel.objects.filter(id__in=id)

                if objects.count():

                    objects.delete()

                    return Response({"Status":status.HTTP_200_OK,"Message":"deleted successfully"})

                else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No records with given id" })

            except:
                return Response({
                    "Status" : status.HTTP_400_BAD_REQUEST,
                    "Message" : "Something Went Wrong"
                })
        else:
            return Response({
                "Status" : status.HTTP_400_BAD_REQUEST,
                "Message" : "Something Went Wrong"
            })  

       
class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        try:
            test = serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            data = UserDetailsModel.objects.get(id=user.pk)
            data.last_login = datetime.datetime.now()
            data.save()
            token, created = Token.objects.get_or_create(user=user)
          
            return Response({
                "Status":status.HTTP_200_OK,
                'token': "Token "+token.key,
                'user_id': user.pk,
                'username': user.username,
                
            })
        except Exception as e:
            return Response({
                "Status":status.HTTP_400_BAD_REQUEST,
                "Message":"Incorrect Username or Password",
            })

class  LoginedUser(ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        print(self.request.data)
        id = self.request.user.id
        user = UserDetailsModel.objects.filter(id=id)
        return user


class LogoutView(ListAPIView):
   
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        datas = Token.objects.get(user=self.request.user.id)
        datas.delete()
        return Response({
            "Status":True,
            "Data":"Succesfully Logout"
        })







