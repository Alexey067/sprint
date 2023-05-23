from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PerevalAddedSerializer


@api_view(['POST'])
def submitData(request):
    serializer = PerevalAddedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_pereval_by_id(request, id):
    try:
        pereval = PerevalAdded.objects.get(id=id)
        serializer = PerevalAddedSerializer(pereval)
        return Response(serializer.data)
    except PerevalAdded.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def edit_pereval(request, id):
    try:
        pereval = PerevalAdded.objects.get(id=id)
        if pereval.status != "new":
            return Response({'state': 0, 'message': 'Запись не может быть отредактирована, она не новая'})
        serializer = PerevalAddedSerializer(pereval, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'state': 1})
        return Response({'state': 0, 'message': serializer.errors})
    except PerevalAdded.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_pereval_by_user_email(request):
    email = request.query_params.get('useremail', None)
    if email:
        perevals = PerevalAdded.objects.filter(useremail=email)
        serializer = PerevalAddedSerializer(perevals, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
