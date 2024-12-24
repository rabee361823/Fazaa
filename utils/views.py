

from django.views.generic import ListView

class CustomListBaseView(ListView):
    """Base view that adds specified field verbose names to the context"""
    context_fields = []
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field_names'] = [
            self.model._meta.get_field(field).verbose_name
            for field in self.context_fields
        ]
        return context

# Usage example:
# class MyListView(FieldListBaseView):
#     model = MyModel
#     context_fields = ['field1', 'field2', 'field3']