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

from launch.api_client import schemas  # noqa: F401


class EndpointPredictRequest(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "return_pickled",
        }

        class properties:
            return_pickled = schemas.BoolSchema
            args = schemas.AnyTypeSchema
            cloudpickle = schemas.StrSchema
            url = schemas.StrSchema
            __annotations__ = {
                "return_pickled": return_pickled,
                "args": args,
                "cloudpickle": cloudpickle,
                "url": url,
            }

    return_pickled: MetaOapg.properties.return_pickled

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["return_pickled"]
    ) -> MetaOapg.properties.return_pickled:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["args"]
    ) -> MetaOapg.properties.args:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["cloudpickle"]
    ) -> MetaOapg.properties.cloudpickle:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["url"]
    ) -> MetaOapg.properties.url:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "return_pickled",
                "args",
                "cloudpickle",
                "url",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["return_pickled"]
    ) -> MetaOapg.properties.return_pickled:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["args"]
    ) -> typing.Union[MetaOapg.properties.args, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["cloudpickle"]
    ) -> typing.Union[MetaOapg.properties.cloudpickle, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["url"]
    ) -> typing.Union[MetaOapg.properties.url, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "return_pickled",
                "args",
                "cloudpickle",
                "url",
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
        return_pickled: typing.Union[
            MetaOapg.properties.return_pickled,
            bool,
        ],
        args: typing.Union[
            MetaOapg.properties.args,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader,
            schemas.Unset,
        ] = schemas.unset,
        cloudpickle: typing.Union[
            MetaOapg.properties.cloudpickle, str, schemas.Unset
        ] = schemas.unset,
        url: typing.Union[
            MetaOapg.properties.url, str, schemas.Unset
        ] = schemas.unset,
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
    ) -> "EndpointPredictRequest":
        return super().__new__(
            cls,
            *args,
            return_pickled=return_pickled,
            args=args,
            cloudpickle=cloudpickle,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )
