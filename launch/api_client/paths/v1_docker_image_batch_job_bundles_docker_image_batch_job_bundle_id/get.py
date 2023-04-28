# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from dataclasses import dataclass
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401
import urllib3
from urllib3._collections import HTTPHeaderDict

from launch.api_client import schemas  # noqa: F401
from launch.api_client import api_client, exceptions
from launch.api_client.model.docker_image_batch_job_bundle_v1_response import (
    DockerImageBatchJobBundleV1Response,
)
from launch.api_client.model.http_validation_error import HTTPValidationError

from . import path

# Path params
DockerImageBatchJobBundleIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    "RequestRequiredPathParams",
    {
        "docker_image_batch_job_bundle_id": typing.Union[
            DockerImageBatchJobBundleIdSchema,
            str,
        ],
    },
)
RequestOptionalPathParams = typing_extensions.TypedDict("RequestOptionalPathParams", {}, total=False)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_docker_image_batch_job_bundle_id = api_client.PathParameter(
    name="docker_image_batch_job_bundle_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DockerImageBatchJobBundleIdSchema,
    required=True,
)
_auth = [
    "HTTPBasic",
]
SchemaFor200ResponseBodyApplicationJson = DockerImageBatchJobBundleV1Response


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[SchemaFor200ResponseBodyApplicationJson,]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        "application/json": api_client.MediaType(schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationError


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[SchemaFor422ResponseBodyApplicationJson,]
    headers: schemas.Unset = schemas.unset


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    content={
        "application/json": api_client.MediaType(schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    "200": _response_for_200,
    "422": _response_for_422,
}
_all_accept_content_types = ("application/json",)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def _get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def _get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[ApiResponseFor200, api_client.ApiResponseWithoutDeserialization,]:
        ...

    def _get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get_oapg(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Get Docker Image Batch Job Model Bundle
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (request_path_docker_image_batch_job_bundle_id,):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace("{%s}" % k, v)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add("Accept", accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method="get".upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(status=response.status, reason=response.reason, api_response=api_response)

        return api_response


class GetDockerImageBatchJobModelBundleV1DockerImageBatchJobBundlesDockerImageBatchJobBundleIdGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[ApiResponseFor200, api_client.ApiResponseWithoutDeserialization,]:
        ...

    def get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get_oapg(
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[ApiResponseFor200,]:
        ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[ApiResponseFor200, api_client.ApiResponseWithoutDeserialization,]:
        ...

    def get(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_docker_image_batch_job_model_bundle_v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id_get_oapg(
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization,
        )
