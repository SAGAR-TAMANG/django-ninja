from ninja import NinjaAPI, Schema, ModelSchema
from library.models import Library
from django.shortcuts import get_object_or_404

api = NinjaAPI()

# class LibrarySchema(Schema):
#   id: int
#   name: str

# We can instead use Model Schema so that the schema can be automatically creted from the model
  
class LibrarySchema(ModelSchema):
  class Meta:
    model = Library
    # fields = "__all__"
    fields = ['id', 'name']

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

@api.post("/library", response=LibrarySchema)
def create_library(request, payload: LibrarySchema):
  library = Library.objects.create(
    id= payload.id,
    name= payload.name,
  )
  # library = Library.objects.create(
  #   **payload.dict()
  # )
  return library

@api.delete("/library/{id}")
def delete_book(request, id: int):
  library = get_object_or_404(Library, id=id)
  library.delete()
  return {'success': True}

@api.patch("/library/{id}", response=LibrarySchema)
def update_book(request, id: int, payload: LibrarySchema):
  library = get_object_or_404(Library, id=id)

  for attr, value in payload.dict(exclude_unset=True).items():
    setattr(library, attr, value)
  
  library.save()
  return library 