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

class GetLLMModelEndpointV1Response(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "inference_framework",
            "name",
            "id",
            "source",
            "status",
        }

        class properties:
            id = schemas.StrSchema

            @staticmethod
            def inference_framework() -> typing.Type["LLMInferenceFramework"]:
                return LLMInferenceFramework
            name = schemas.StrSchema

            @staticmethod
            def source() -> typing.Type["LLMSource"]:
                return LLMSource
            @staticmethod
            def status() -> typing.Type["ModelEndpointStatus"]:
                return ModelEndpointStatus
            inference_framework_image_tag = schemas.StrSchema
            model_name = schemas.StrSchema
            num_shards = schemas.IntSchema

            @staticmethod
            def quantize() -> typing.Type["Quantization"]:
                return Quantization
            @staticmethod
            def spec() -> typing.Type["GetModelEndpointV1Response"]:
                return GetModelEndpointV1Response
            __annotations__ = {
                "id": id,
                "inference_framework": inference_framework,
                "name": name,
                "source": source,
                "status": status,
                "inference_framework_image_tag": inference_framework_image_tag,
                "model_name": model_name,
                "num_shards": num_shards,
                "quantize": quantize,
                "spec": spec,
            }
    inference_framework: "LLMInferenceFramework"
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    source: "LLMSource"
    status: "ModelEndpointStatus"

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["inference_framework"]
    ) -> "LLMInferenceFramework": ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> "LLMSource": ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> "ModelEndpointStatus": ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["inference_framework_image_tag"]
    ) -> MetaOapg.properties.inference_framework_image_tag: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["model_name"]
    ) -> MetaOapg.properties.model_name: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["num_shards"]
    ) -> MetaOapg.properties.num_shards: ...
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantize"]) -> "Quantization": ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["spec"]
    ) -> "GetModelEndpointV1Response": ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "id",
                "inference_framework",
                "name",
                "source",
                "status",
                "inference_framework_image_tag",
                "model_name",
                "num_shards",
                "quantize",
                "spec",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["inference_framework"]
    ) -> "LLMInferenceFramework": ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name: ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> "LLMSource": ...
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> "ModelEndpointStatus": ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["inference_framework_image_tag"]
    ) -> typing.Union[MetaOapg.properties.inference_framework_image_tag, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["model_name"]
    ) -> typing.Union[MetaOapg.properties.model_name, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["num_shards"]
    ) -> typing.Union[MetaOapg.properties.num_shards, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["quantize"]
    ) -> typing.Union["Quantization", schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["spec"]
    ) -> typing.Union["GetModelEndpointV1Response", schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "id",
                "inference_framework",
                "name",
                "source",
                "status",
                "inference_framework_image_tag",
                "model_name",
                "num_shards",
                "quantize",
                "spec",
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
        inference_framework: "LLMInferenceFramework",
        name: typing.Union[
            MetaOapg.properties.name,
            str,
        ],
        id: typing.Union[
            MetaOapg.properties.id,
            str,
        ],
        source: "LLMSource",
        status: "ModelEndpointStatus",
        inference_framework_image_tag: typing.Union[
            MetaOapg.properties.inference_framework_image_tag, str, schemas.Unset
        ] = schemas.unset,
        model_name: typing.Union[
            MetaOapg.properties.model_name, str, schemas.Unset
        ] = schemas.unset,
        num_shards: typing.Union[
            MetaOapg.properties.num_shards, decimal.Decimal, int, schemas.Unset
        ] = schemas.unset,
        quantize: typing.Union["Quantization", schemas.Unset] = schemas.unset,
        spec: typing.Union["GetModelEndpointV1Response", schemas.Unset] = schemas.unset,
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
    ) -> "GetLLMModelEndpointV1Response":
        return super().__new__(
            cls,
            *_args,
            inference_framework=inference_framework,
            name=name,
            id=id,
            source=source,
            status=status,
            inference_framework_image_tag=inference_framework_image_tag,
            model_name=model_name,
            num_shards=num_shards,
            quantize=quantize,
            spec=spec,
            _configuration=_configuration,
            **kwargs,
        )

from launch_client.model.get_model_endpoint_v1_response import GetModelEndpointV1Response
from launch_client.model.llm_inference_framework import LLMInferenceFramework
from launch_client.model.llm_source import LLMSource
from launch_client.model.model_endpoint_status import ModelEndpointStatus
from launch_client.model.quantization import Quantization
