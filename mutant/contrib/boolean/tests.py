
from django.utils.translation import ugettext_lazy as _

from ...test.testcases import FieldDefinitionTestMixin
from ...tests.models.utils import BaseModelDefinitionTestCase

from .models import BooleanFieldDefinition, NullBooleanFieldDefinition


class BooleanFieldDefinitionTestMixin(FieldDefinitionTestMixin):
    field_definition_category = _(u'Boolean')

class BooleanFieldDefinitionTest(BooleanFieldDefinitionTestMixin,
                                 BaseModelDefinitionTestCase):
    field_definition_cls = BooleanFieldDefinition
    field_defintion_init_kwargs = {'default': True}
    field_values = (True, False)

class NullBooleanFieldDefinitionTest(BooleanFieldDefinitionTestMixin,
                                     BaseModelDefinitionTestCase):
    field_definition_cls = NullBooleanFieldDefinition
    field_values = (True, None)
