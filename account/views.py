from django.utils import timezone
from rest_framework import generics, views, status, permissions
from rest_framework.response import Response

from account import models, serializers


class RegisterApiView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterVerifyApiView(generics.GenericAPIView):
    serializer_class = serializers.RegisterVerifySerializer

    def post(self, request):
        serializer = serializers.RegisterVerifySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phone_number = serializer.data['phone_number']
            code = serializer.data['code']
            try:
                user = models.User.objects.get(phone_number=phone_number)
                otp_code = models.UserOtpCode.objects.get(code=code)
            except models.User.DoesNotExist and models.UserOtpCode.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if otp_code.expires_at > timezone.now() and otp_code.is_used == False:
                user.is_active = True
                otp_code.is_used = True
                user.save()
                otp_code.save()
                return Response({'success': True, 'message': 'User is activated'}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'success': False, 'messages': 'User is not activated, Code is incorrect'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

