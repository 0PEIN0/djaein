from rest_framework.renderers import JSONRenderer


class BaseJsonRenderer(JSONRenderer):

    def render(self,
               data,
               accepted_media_type=None,
               renderer_context=None):
        response = super(BaseJsonRenderer, self).render(
            data, accepted_media_type, renderer_context)
        return response
