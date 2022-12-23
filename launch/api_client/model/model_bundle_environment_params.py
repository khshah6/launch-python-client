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


class ModelBundleEnvironmentParams(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
        Ref: https://openapi-generator.tech

        Do not edit the class manually.

        This is the entity-layer class for the Model Bundle environment parameters. Being an
    entity-layer class, it should be a plain data object.
    """

    class MetaOapg:
        required = {
            "framework_type",
        }

        class properties:
            @staticmethod
            def framework_type() -> typing.Type["ModelBundleFramework"]:
                return ModelBundleFramework

            ecr_repo = schemas.StrSchema
            image_tag = schemas.StrSchema
            pytorch_image_tag = schemas.StrSchema
            tensorflow_version = schemas.StrSchema
            __annotations__ = {
                "framework_type": framework_type,
                "ecr_repo": ecr_repo,
                "image_tag": image_tag,
                "pytorch_image_tag": pytorch_image_tag,
                "tensorflow_version": tensorflow_version,
            }

    framework_type: "ModelBundleFramework"

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["framework_type"]
    ) -> "ModelBundleFramework":
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["ecr_repo"]
    ) -> MetaOapg.properties.ecr_repo:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["image_tag"]
    ) -> MetaOapg.properties.image_tag:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["pytorch_image_tag"]
    ) -> MetaOapg.properties.pytorch_image_tag:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["tensorflow_version"]
    ) -> MetaOapg.properties.tensorflow_version:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "framework_type",
                "ecr_repo",
                "image_tag",
                "pytorch_image_tag",
                "tensorflow_version",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["framework_type"]
    ) -> "ModelBundleFramework":
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["ecr_repo"]
    ) -> typing.Union[MetaOapg.properties.ecr_repo, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["image_tag"]
    ) -> typing.Union[MetaOapg.properties.image_tag, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["pytorch_image_tag"]
    ) -> typing.Union[MetaOapg.properties.pytorch_image_tag, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["tensorflow_version"]
    ) -> typing.Union[MetaOapg.properties.tensorflow_version, schemas.Unset]:
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
                "framework_type",
                "ecr_repo",
                "image_tag",
                "pytorch_image_tag",
                "tensorflow_version",
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
        framework_type: "ModelBundleFramework",
        ecr_repo: typing.Union[
            MetaOapg.properties.ecr_repo, str, schemas.Unset
        ] = schemas.unset,
        image_tag: typing.Union[
            MetaOapg.properties.image_tag, str, schemas.Unset
        ] = schemas.unset,
        pytorch_image_tag: typing.Union[
            MetaOapg.properties.pytorch_image_tag, str, schemas.Unset
        ] = schemas.unset,
        tensorflow_version: typing.Union[
            MetaOapg.properties.tensorflow_version, str, schemas.Unset
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
    ) -> "ModelBundleEnvironmentParams":
        return super().__new__(
            cls,
            *args,
            framework_type=framework_type,
            ecr_repo=ecr_repo,
            image_tag=image_tag,
            pytorch_image_tag=pytorch_image_tag,
            tensorflow_version=tensorflow_version,
            _configuration=_configuration,
            **kwargs,
        )


from launch.api_client.model.model_bundle_framework import ModelBundleFramework
