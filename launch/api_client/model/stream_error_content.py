# coding: utf-8

"""
    launch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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


class StreamErrorContent(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "error",
            "timestamp",
        }

        class properties:
            error = schemas.StrSchema
            timestamp = schemas.StrSchema
            __annotations__ = {
                "error": error,
                "timestamp": timestamp,
            }

    error: MetaOapg.properties.error
    timestamp: MetaOapg.properties.timestamp

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["timestamp"]
    ) -> MetaOapg.properties.timestamp:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "error",
                "timestamp",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["timestamp"]
    ) -> MetaOapg.properties.timestamp:
        ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "error",
                "timestamp",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        error: typing.Union[
            MetaOapg.properties.error,
            str,
        ],
        timestamp: typing.Union[
            MetaOapg.properties.timestamp,
            str,
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
    ) -> "StreamErrorContent":
        return super().__new__(
            cls,
            *_args,
            error=error,
            timestamp=timestamp,
            _configuration=_configuration,
            **kwargs,
        )
