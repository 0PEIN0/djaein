class GenericApiViewHandler(object):

    def check_permission(self,
                         user):
        return True

    def ok(self,
           data,
           serializer,
           request,
           is_listing=False):
        pass
