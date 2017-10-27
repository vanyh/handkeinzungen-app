from django import template
from django.contrib.contenttypes.models import ContentType
from webpage.metadata import PROJECT_METADATA as PM

register = template.Library()


@register.simple_tag
def create_object_count(app='vocabs'):

    """fetches all models of the passed in app and returns a
    dict containg the name of each class and the number of instances"""

    models = ContentType.objects.filter(app_label=app)
    result = []
    for x in models:
        modelname = x.name
        modelname = modelname.replace(" ", "").lower()
        try:
            fetched_model = ContentType.objects.get(app_label=app, model=modelname).model_class()
            item = {
                'name': modelname.title(),
                'count': fetched_model.objects.count()
            }
            result.append(item)
        except:
            item = {
                'name': x,
                'count': "Some error occured"
            }
            result.append(item)
    return result


@register.simple_tag
def projects_metadata(key):
    return PM[key]
