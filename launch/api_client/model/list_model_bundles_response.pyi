# coding: utf-8

"""
    launch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401
from launch_client import schemas  # noqa: F401

class ListModelBundlesResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Response object for listing Model Bundles.
    """

    class MetaOapg:
        required = {
            "model_bundles",
        }

        class properties:
            class model_bundles(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["ModelBundleResponse"]:
                        return ModelBundleResponse
                def __new__(
                    cls,
                    arg: typing.Union[
                        typing.Tuple["ModelBundleResponse"],
                        typing.List["ModelBundleResponse"],
                    ],
                    _configuration: typing.Optional[
                        schemas.Configuration
                    ] = None,
                ) -> "model_bundles":
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
                def __getitem__(self, i: int) -> "ModelBundleResponse":
                    return super().__getitem__(i)
            __annotations__ = {
                "model_bundles": model_bundles,
            }
    model_bundles: MetaOapg.properties.model_bundles

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["model_bundles"]
    ) -> MetaOapg.properties.model_bundles: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "model_bundles",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["model_bundles"]
    ) -> MetaOapg.properties.model_bundles: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "model_bundles",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)
    def __new__(
        cls,
        *args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        model_bundles: typing.Union[
            MetaOapg.properties.model_bundles,
            list,
            tuple,
        ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[
            schemas.AnyTypeSchema,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            None,
            list,
            tuple,
            bytes,
        ],
    ) -> "ListModelBundlesResponse":
        return super().__new__(
            cls,
            *args,
            model_bundles=model_bundles,
            _configuration=_configuration,
            **kwargs,
        )

from launch_client.model.model_bundle_response import ModelBundleResponse
