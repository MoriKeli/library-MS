from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BookSerializer
from staff.models import Book

class BookView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all().order_by('catalogue', 'author-')
        serializer = BookSerializer(books, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class BookDetails(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(ref_no=pk)
        
        except Book.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = BookSerializer(article)
        
        return Response(serializer.data, status.HTTP_302_FOUND)
    
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status.HTTP_204_NO_CONTENT)
        