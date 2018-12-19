# -*- coding: utf-8 -*-
import copy


def check_actual_include_expected(expected, actual):
    def check_base_value(expected, actual):
        if expected != actual:
            raise

    def check_list_value(expected, actual):
        assert isinstance(expected, (list, tuple))
        if not isinstance(actual, (list, tuple)):
            raise

        if len(expected) != len(actual):
            raise

        for i in range(len(expected)):
            if isinstance(expected[i], (list, tuple)):
                check_list_value(expected[i], actual[i])
            elif isinstance(expected[i], dict):
                check_dict_value(expected[i], actual[i])

            return check_base_value(expected[i], actual[i])

    def check_dict_value(expected, actual):
        assert isinstance(expected, dict)
        if not isinstance(actual, dict):
            raise

        # containing relationship
        if set(expected.keys()) & set(actual.keys()) != set(expected.keys()):
            raise

        for key, val in expected.items():

            # recursion
            if isinstance(val, dict):
                check_dict_value(val, actual=actual[key])
            # if list or tuple iter
            elif isinstance(val, (list, tuple)):
                check_list_value(val, actual[key])

            return check_base_value(val, actual[key])

    # do not change origin value
    expected = copy.deepcopy(expected)
    actual = copy.deepcopy(actual)
    if isinstance(expected, (list, tuple)):
        check_list_value(expected, actual)
    elif isinstance(expected, dict):
        check_dict_value(expected, actual)

    check_base_value(expected, actual)
