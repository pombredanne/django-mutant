from decimal import Decimal

from django.utils.translation import ugettext_lazy as _

from ...test.testcases import FieldDefinitionTestMixin
from ...tests.models.utils import BaseModelDefinitionTestCase

from .models import (BigIntegerFieldDefinition, DecimalFieldDefinition,
    FloatFieldDefinition, IntegerFieldDefinition,
    PositiveIntegerFieldDefinition, PositiveSmallIntegerFieldDefinition,
    SmallIntegerFieldDefinition)


class NumericFieldDefinitionTestMixin(FieldDefinitionTestMixin):
    field_definition_category = _(u'Numeric')

class SmallIntegerFieldDefinitionTest(NumericFieldDefinitionTestMixin,
                                      BaseModelDefinitionTestCase):
    field_definition_cls = SmallIntegerFieldDefinition
    field_defintion_init_kwargs = {'default': 0}
    field_values = (-134, 245)

class PositiveSmallIntegerFieldDefinitionTest(NumericFieldDefinitionTestMixin,
                                              BaseModelDefinitionTestCase):
    field_definition_cls = PositiveSmallIntegerFieldDefinition
    field_defintion_init_kwargs = {'default': 0}
    field_values = (135, 346)

class IntegerFieldDefinitionTest(NumericFieldDefinitionTestMixin,
                                 BaseModelDefinitionTestCase):
    field_definition_cls = IntegerFieldDefinition
    field_defintion_init_kwargs = {'default': 0}
    field_values = (44323423, -4223423)

class PositiveIntegerFieldDefinitionTest(NumericFieldDefinitionTestMixin,
                                         BaseModelDefinitionTestCase):
    field_definition_cls = PositiveIntegerFieldDefinition
    field_defintion_init_kwargs = {'default': 0}
    field_values = (44323423, 443234234)
    
class BigIntegerFieldDefinitionTest(NumericFieldDefinitionTestMixin,
                                    BaseModelDefinitionTestCase):
    field_definition_cls = BigIntegerFieldDefinition
    field_defintion_init_kwargs = {'default': 0}
    field_values = (443234234324, 443234234998)

class FloatFieldDefinitionTest(NumericFieldDefinitionTestMixin,
                               BaseModelDefinitionTestCase):
    field_definition_cls = FloatFieldDefinition
    field_defintion_init_kwargs = {'default': 0}
    field_values = (1234567.84950, 18360935.1854195)

class DecimalFieldDefinitionTest(NumericFieldDefinitionTestMixin,
                                 BaseModelDefinitionTestCase):
    field_definition_cls = DecimalFieldDefinition
    field_defintion_init_kwargs = {
        'default': 0,
        'max_digits': 15,
        'decimal_places': 7
    }
    field_values = (
        Decimal('1234567.84950'),
        Decimal('18360935.1854195'),
    )
