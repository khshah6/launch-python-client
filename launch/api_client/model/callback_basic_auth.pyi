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
from launch_client import schemas  # noqa: F401

class CallbackBasicAuth(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "password",
            "kind",
            "username",
        }

        class properties:
            class kind(schemas.EnumBase, schemas.StrSchema):
                @schemas.classproperty
                def BASIC(cls):
                    return cls("basic")
            password = schemas.StrSchema
            username = schemas.StrSchema
            __annotations__ = {
                "kind": kind,
                "password": password,
                "username": username,
            }
    password: MetaOapg.properties.password
    kind: MetaOapg.properties.kind
    username: MetaOapg.properties.username

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["password"]
    ) -> MetaOapg.properties.password: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["username"]
    ) -> MetaOapg.properties.username: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "kind",
                "password",
                "username",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["kind"]
    ) -> MetaOapg.properties.kind: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["password"]
    ) -> MetaOapg.properties.password: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["username"]
    ) -> MetaOapg.properties.username: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "kind",
                "password",
                "username",
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
        password: typing.Union[
            MetaOapg.properties.password,
            str,
        ],
        kind: typing.Union[
            MetaOapg.properties.kind,
            str,
        ],
        username: typing.Union[
            MetaOapg.properties.username,
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
    ) -> "CallbackBasicAuth":
        return super().__new__(
            cls,
            *_args,
            password=password,
            kind=kind,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )
