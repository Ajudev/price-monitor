from rest_framework.response import Response
from rest_framework import status


class ExceptionMixin:
    """
    Mixin which will capture any exception and return response with the error message
    """

    def handle_exception(self, exc):
        data = {}
        if hasattr(exc, 'status_code'):
            if exc.status_code == 401:
                data['message'] = 'Invalid Authentication Credentials'
                resp_status = status.HTTP_401_UNAUTHORIZED
            elif exc.status_code == 405:
                data['message'] = f"{exc.args[0]} Method not Allowed"
                resp_status = status.HTTP_405_METHOD_NOT_ALLOWED
            elif exc.status_code == 400:
                data['message'] = 'Bad Request'
                data['error'] = exc.args
                resp_status = status.HTTP_400_BAD_REQUEST
            else:
                data['message'] = 'Internal Server Error'
                data['error'] = exc.args
                resp_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            data['message'] = 'Internal Server Error'
            data['error'] = exc.args
            resp_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data, status=resp_status)