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


class ListFineTunesResponse(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "jobs",
        }

        class properties:
            class jobs(schemas.ListSchema):
                class MetaOapg:
                    @staticmethod
                    def items() -> typing.Type["GetFineTuneResponse"]:
                        return GetFineTuneResponse

                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple["GetFineTuneResponse"],
                        typing.List["GetFineTuneResponse"],
                    ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> "jobs":
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> "GetFineTuneResponse":
                    return super().__getitem__(i)

            __annotations__ = {
                "jobs": jobs,
            }

    jobs: MetaOapg.properties.jobs

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobs"]) -> MetaOapg.properties.jobs:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "jobs",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobs"]) -> MetaOapg.properties.jobs:
        ...

    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "jobs",
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
        jobs: typing.Union[
            MetaOapg.properties.jobs,
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
    ) -> "ListFineTunesResponse":
        return super().__new__(
            cls,
            *_args,
            jobs=jobs,
            _configuration=_configuration,
            **kwargs,
        )


from launch.api_client.model.get_fine_tune_response import GetFineTuneResponse
