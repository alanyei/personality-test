from import_export import resources
from .models import Result

class PersonResource(resources.ModelResource):
        class Meta:
                    model = Result
