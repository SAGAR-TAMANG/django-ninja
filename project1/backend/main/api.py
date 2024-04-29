from ninja import NinjaAPI, Schema
from library.models import Library
from django.shortcuts import get_object_or_404

api = NinjaAPI()

class LibrarySchema(Schema):
  id: int
  name: str

@api.get("hello/")
def helloworld(request):
  return {"message": "Hello World"} 

@api.get("/library/{id}", response=LibrarySchema)
def library_detail(request, id: int):
  library_obj = get_object_or_404(Library, id=id)  
  return library_obj

@api.get("/library", response=list[LibrarySchema])
def library_list(request):
  return Library.objects.all()