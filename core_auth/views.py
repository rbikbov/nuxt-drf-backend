from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import get_user
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

UserModel = get_user_model()


@api_view(['GET',])
@permission_classes((AllowAny, ))
def checkExists(request):
    # user = UserModel.objects.get(id=3)
    # print(user._meta.get_fields())
    # print(get_user(request))
    if request.method == 'GET':
        username = request.GET.get('username')
        email = request.GET.get('email')
        valid = True
        message = None

        if username and UserModel.objects.filter(username=username).exists():
            valid = False
            message = 'Пользователь "%s" уже существует.' % username

        if email and UserModel.objects.filter(email=email).exists():
            valid = False
            message = 'Пользователь с e-mail адресом "%s" уже зарегистрирован.' % email

        response = Response({'valid': valid, 'message': message})
        response['Access-Control-Allow-Credentials'] = 'true'
        return response


# отправка токена при подтверждении email
# class CustomVerifyEmailView(VerifyEmailView):
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.kwargs['key'] = serializer.validated_data['key']
#         confirmation = self.get_object()
#         confirmation.confirm(self.request)
#         token = TokenModel.objects.get(user_id=confirmation.email_address.user)
#         return Response({'key': token.key}, status=status.HTTP_200_OK)