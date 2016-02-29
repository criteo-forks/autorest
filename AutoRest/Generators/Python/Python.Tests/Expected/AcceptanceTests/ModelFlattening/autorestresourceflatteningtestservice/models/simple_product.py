# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .base_product import BaseProduct


class SimpleProduct(BaseProduct):
    """
    The product documentation.

    :param str base_product_id: Unique identifier representing a specific
     product for a given latitude & longitude. For example, uberX in San
     Francisco will have a different product_id than uberX in Los Angeles.
    :param str base_product_description: Description of product.
    :param str max_product_display_name: Display name of product.
    :param str max_product_capacity: Capacity of product. For example, 4
     people. Default value: "Large" .
    :param str odatavalue: URL value.
    """

    _required = ['max_product_display_name', 'max_product_capacity']

    _attribute_map = {
        'max_product_display_name': {'key': 'details.max_product_display_name', 'type': 'str'},
        'max_product_capacity': {'key': 'details.max_product_capacity', 'type': 'str'},
        'odatavalue': {'key': 'details.max_product_image.@odata\\.value', 'type': 'str'},
    }

    def __init__(self, base_product_id, max_product_display_name, max_product_capacity, base_product_description=None, odatavalue=None):
        super(SimpleProduct, self).__init__(base_product_id=base_product_id, base_product_description=base_product_description)
        self.max_product_display_name = max_product_display_name
        self.max_product_capacity = max_product_capacity
        self.odatavalue = odatavalue