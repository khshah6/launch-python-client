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


class CallbackmTLSAuth(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "kind",
            "cert",
            "key",
        }

        class properties:
            cert = schemas.StrSchema
            key = schemas.StrSchema

            class kind(schemas.EnumBase, schemas.StrSchema):
                class MetaOapg:
                    enum_value_to_name = {
                        "mtls": "MTLS",
                    }

                @schemas.classproperty
                def MTLS(cls):
                    return cls("mtls")

            __annotations__ = {
                "cert": cert,
                "key": key,
                "kind": kind,
            }

    kind: MetaOapg.properties.kind
    cert: MetaOapg.properties.cert
    key: MetaOapg.properties.key

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cert"]) -> MetaOapg.properties.cert:
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key:
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "cert",
                "key",
                "kind",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cert"]) -> MetaOapg.properties.cert:
        ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key:
        ...

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind:
        ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "cert",
                "key",
                "kind",
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
        kind: typing.Union[
            MetaOapg.properties.kind,
            str,
        ],
        cert: typing.Union[
            MetaOapg.properties.cert,
            str,
        ],
        key: typing.Union[
            MetaOapg.properties.key,
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
    ) -> "CallbackmTLSAuth":
        return super().__new__(
            cls,
            *_args,
            kind=kind,
            cert=cert,
            key=key,
            _configuration=_configuration,
            **kwargs,
        )
