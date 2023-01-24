from django.shortcuts import render

# Create your views here.

#
# class GetLoginToken(APIView):
#     def post(self, request):
#         user = User.objects.filter(username=request.data.get("username")).first()
#         password = request.data.get("password")
#         user_type = None
#         try:
#             user_type = user.user_type.name.upper()
#         except:
#             pass
#
#         if user is not None and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             context = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'user_type':user_type,
#             }
#             return Response(context, status.HTTP_200_OK)
#         else:
#             context = {
#                 "detail": "No active account found with the given credentials"
#             }
#             return Response(context,status.HTTP_401_UNAUTHORIZED)

