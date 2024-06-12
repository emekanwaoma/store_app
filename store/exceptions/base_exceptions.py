from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import (
    AuthenticationFailed,
    ValidationError,
)
from rest_framework.views import Response, exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler \
    # first to get the standard error response.
    response = exception_handler(exc, context)

    # reverting authentication status code to 401 \
    # instead of 403 permisssion denied
    if isinstance(exc, AuthenticationFailed):
        response.status_code = status.HTTP_401_UNAUTHORIZED

    if isinstance(exc, ValidationError):
        response.data["code"] = "4001"

    # if there is an IntegrityError and the error response hasn't already been generated
    if isinstance(exc, IntegrityError):
        response = Response(
            {"message": str(exc), "code": "4002"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # if there is an ASSERTION_ERROR and the error \
    # response hasn't already been generated

    if isinstance(exc, AssertionError) and not response:
        response = Response({"message": str(exc)}, status=status.HTTP_400_BAD_REQUEST)

    # Handle all other exceptions
    if not response:
        response = Response(
            {"message": "An error occurred: " + str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response
