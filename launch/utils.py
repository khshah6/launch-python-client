from typing import Any, Dict


def trim_kwargs(kwargs_dict: Dict[Any, Any]):
    """
    Returns a copy of kwargs_dict with None values removed
    """
    dict_copy = {}
    for k, v in kwargs_dict.items():
        if v is not None:
            dict_copy[k] = v
    return dict_copy
