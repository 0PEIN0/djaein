class DataLoader(object):

    def model_specific_operations(self,
                                  model,
                                  model_def,
                                  single_entry,
                                  single_instance):
        try:
            for after_creation in model_def['after_creation']:
                data_qs = model.objects.filter(
                    **after_creation['query'])
                for item in data_qs:
                    for key, value in after_creation['update'].items():
                        if hasattr(value, '__class__') and hasattr(value, 'objects'):
                            if hasattr(value, 'count') is False:
                                setattr(item, key, value)
                            else:
                                if value.count() == 1:
                                    setattr(item, key, value.first())
                                else:
                                    many_to_many = getattr(item, key)
                                    many_to_many.set(value)
                        elif hasattr(value, '__class__'):
                            if hasattr(value, 'count') is True:
                                many_to_many = getattr(item, key)
                                if hasattr(many_to_many, 'set'):
                                    many_to_many.set(value)
                            else:
                                setattr(item, key, value)
                        else:
                            setattr(item, key, value)
                    item.save()
        except KeyError as ex:
            pass
        if model.__name__ == 'User':
            single_instance.set_password(single_entry['password'])
            single_instance.save()

    def insert_initial_data(self,
                            schema):
        res = []
        for model_def in schema:
            model = None
            try:
                model = model_def['model']
            except KeyError as ex:
                continue
            try:
                created_by = model_def['created_by']
            except KeyError as ex:
                created_by = None
            data = None
            try:
                data = model_def['data']
            except KeyError as ex:
                continue
            instance_list = []
            for single_entry in data:
                for key, value in single_entry.items():
                    if hasattr(value, 'objects') is True:
                        single_entry[key] = value.objects.all().first()
                single_instance = None
                if model.objects.filter(**single_entry).count() > 1:
                    # more than 1 item
                    model.objects.filter(**single_entry).delete()
                elif model.objects.filter(**single_entry).count() is 0:
                    if created_by is not None:
                        single_entry['created_by'] = created_by
                    # no item
                    try:
                        single_instance = model.objects.create(**single_entry)
                        self.model_specific_operations(model=model,
                                                       model_def=model_def,
                                                       single_entry=single_entry,
                                                       single_instance=single_instance)
                    except Exception as ex:
                        pass
                else:
                    single_instance = model.objects.filter(
                        **single_entry).first()
                    # exactly 1 item
                    self.model_specific_operations(model=model,
                                                   model_def=model_def,
                                                   single_entry=single_entry,
                                                   single_instance=single_instance)
                instance_list.append(single_instance)
            res.append(instance_list)
            print("Model : ", model.__name__)
            print("Created : ", instance_list)
        return res
