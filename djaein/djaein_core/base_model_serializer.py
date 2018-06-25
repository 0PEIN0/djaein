from rest_framework.serializers import ModelSerializer


class BaseModelSerializer(ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(BaseModelSerializer, self).__init__(*args, **kwargs)
