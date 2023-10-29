#!/usr/bin/env python3
""" Parameterize a unit test
"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    a test class, TestAccessNestedMap,
    which inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """Test access_nested_map method.
            Nested_map(Dict): a dictonary
            path(List, tuple, set): keys to get value in nested dict
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in the nested map")
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception_message):
        """
        tests the access_nested_map function for exceptions.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_message)
