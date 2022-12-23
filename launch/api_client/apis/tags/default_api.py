# coding: utf-8

"""
    launch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from launch_client.paths.healthcheck.get import HealthcheckHealthcheckGet
from launch_client.paths.healthz.get import HealthcheckHealthzGet
from launch_client.paths.readyz.get import HealthcheckReadyzGet
from launch_client.paths.v1_async_tasks.post import (
    CreateAsyncInferenceTaskV1AsyncTasksPost,
)
from launch_client.paths.v1_async_tasks_task_id.get import (
    GetAsyncInferenceTaskV1AsyncTasksTaskIdGet,
)
from launch_client.paths.v1_model_bundles.get import (
    ListModelBundlesV1ModelBundlesGet,
)
from launch_client.paths.v1_model_bundles.post import (
    CreateModelBundleV1ModelBundlesPost,
)
from launch_client.paths.v1_model_bundles_latest.get import (
    GetLatestModelBundleV1ModelBundlesLatestGet,
)
from launch_client.paths.v1_model_bundles_model_bundle_id.get import (
    GetModelBundleV1ModelBundlesModelBundleIdGet,
)
from launch_client.paths.v1_model_endpoints.get import (
    ListModelEndpointsV1ModelEndpointsGet,
)
from launch_client.paths.v1_model_endpoints.post import (
    CreateModelEndpointV1ModelEndpointsPost,
)
from launch_client.paths.v1_model_endpoints_model_endpoint_id.delete import (
    DeleteModelEndpointV1ModelEndpointsModelEndpointIdDelete,
)
from launch_client.paths.v1_model_endpoints_model_endpoint_id.get import (
    GetModelEndpointV1ModelEndpointsModelEndpointIdGet,
)
from launch_client.paths.v1_model_endpoints_model_endpoint_id.put import (
    UpdateModelEndpointV1ModelEndpointsModelEndpointIdPut,
)
from launch_client.paths.v1_sync_tasks.post import (
    CreateSyncInferenceTaskV1SyncTasksPost,
)


class DefaultApi(
    CreateAsyncInferenceTaskV1AsyncTasksPost,
    CreateModelBundleV1ModelBundlesPost,
    CreateModelEndpointV1ModelEndpointsPost,
    CreateSyncInferenceTaskV1SyncTasksPost,
    DeleteModelEndpointV1ModelEndpointsModelEndpointIdDelete,
    GetAsyncInferenceTaskV1AsyncTasksTaskIdGet,
    GetLatestModelBundleV1ModelBundlesLatestGet,
    GetModelBundleV1ModelBundlesModelBundleIdGet,
    GetModelEndpointV1ModelEndpointsModelEndpointIdGet,
    HealthcheckHealthcheckGet,
    HealthcheckHealthzGet,
    HealthcheckReadyzGet,
    ListModelBundlesV1ModelBundlesGet,
    ListModelEndpointsV1ModelEndpointsGet,
    UpdateModelEndpointV1ModelEndpointsModelEndpointIdPut,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    pass
