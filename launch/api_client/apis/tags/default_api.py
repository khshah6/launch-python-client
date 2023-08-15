# coding: utf-8

"""
    launch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from launch.api_client.paths.healthcheck.get import HealthcheckHealthcheckGet
from launch.api_client.paths.healthz.get import HealthcheckHealthzGet
from launch.api_client.paths.readyz.get import HealthcheckReadyzGet
from launch.api_client.paths.v1_async_tasks.post import CreateAsyncInferenceTaskV1AsyncTasksPost
from launch.api_client.paths.v1_async_tasks_task_id.get import (
    GetAsyncInferenceTaskV1AsyncTasksTaskIdGet,
)
from launch.api_client.paths.v1_batch_jobs.post import CreateBatchJobV1BatchJobsPost
from launch.api_client.paths.v1_batch_jobs_batch_job_id.get import GetBatchJobV1BatchJobsBatchJobIdGet
from launch.api_client.paths.v1_batch_jobs_batch_job_id.put import (
    UpdateBatchJobV1BatchJobsBatchJobIdPut,
)
from launch.api_client.paths.v1_docker_image_batch_job_bundles.get import (
    ListDockerImageBatchJobModelBundlesV1DockerImageBatchJobBundlesGet,
)
from launch.api_client.paths.v1_docker_image_batch_job_bundles.post import (
    CreateDockerImageBatchJobBundleV1DockerImageBatchJobBundlesPost,
)
from launch.api_client.paths.v1_docker_image_batch_job_bundles_docker_image_batch_job_bundle_id.get import (
    GetDockerImageBatchJobModelBundleV1DockerImageBatchJobBundlesDockerImageBatchJobBundleIdGet,
)
from launch.api_client.paths.v1_docker_image_batch_job_bundles_latest.get import (
    GetLatestDockerImageBatchJobBundleV1DockerImageBatchJobBundlesLatestGet,
)
from launch.api_client.paths.v1_docker_image_batch_jobs.get import (
    ListDockerImageBatchJobsV1DockerImageBatchJobsGet,
)
from launch.api_client.paths.v1_docker_image_batch_jobs.post import (
    CreateDockerImageBatchJobV1DockerImageBatchJobsPost,
)
from launch.api_client.paths.v1_docker_image_batch_jobs_batch_job_id.get import (
    GetDockerImageBatchJobV1DockerImageBatchJobsBatchJobIdGet,
)
from launch.api_client.paths.v1_docker_image_batch_jobs_batch_job_id.put import (
    UpdateDockerImageBatchJobV1DockerImageBatchJobsBatchJobIdPut,
)
from launch.api_client.paths.v1_files.get import ListFilesV1FilesGet
from launch.api_client.paths.v1_files.post import UploadFileV1FilesPost
from launch.api_client.paths.v1_files_file_id.delete import DeleteFileV1FilesFileIdDelete
from launch.api_client.paths.v1_files_file_id.get import GetFileV1FilesFileIdGet
from launch.api_client.paths.v1_files_file_id_content.get import GetFileContentV1FilesFileIdContentGet
from launch.api_client.paths.v1_llm_completions_stream.post import (
    CreateCompletionStreamTaskV1LlmCompletionsStreamPost,
)
from launch.api_client.paths.v1_llm_completions_sync.post import (
    CreateCompletionSyncTaskV1LlmCompletionsSyncPost,
)
from launch.api_client.paths.v1_llm_fine_tunes.get import ListFineTunesV1LlmFineTunesGet
from launch.api_client.paths.v1_llm_fine_tunes.post import CreateFineTuneV1LlmFineTunesPost
from launch.api_client.paths.v1_llm_fine_tunes_fine_tune_id.get import (
    GetFineTuneV1LlmFineTunesFineTuneIdGet,
)
from launch.api_client.paths.v1_llm_fine_tunes_fine_tune_id_cancel.put import (
    CancelFineTuneV1LlmFineTunesFineTuneIdCancelPut,
)
from launch.api_client.paths.v1_llm_fine_tunes_fine_tune_id_events.get import (
    GetFineTuneEventsV1LlmFineTunesFineTuneIdEventsGet,
)
from launch.api_client.paths.v1_llm_model_endpoints.get import ListModelEndpointsV1LlmModelEndpointsGet
from launch.api_client.paths.v1_llm_model_endpoints.post import (
    CreateModelEndpointV1LlmModelEndpointsPost,
)
from launch.api_client.paths.v1_llm_model_endpoints_download.post import (
    DownloadModelEndpointV1LlmModelEndpointsDownloadPost,
)
from launch.api_client.paths.v1_llm_model_endpoints_model_endpoint_name.get import (
    GetModelEndpointV1LlmModelEndpointsModelEndpointNameGet,
)
from launch.api_client.paths.v1_model_bundles.get import ListModelBundlesV1ModelBundlesGet
from launch.api_client.paths.v1_model_bundles.post import CreateModelBundleV1ModelBundlesPost
from launch.api_client.paths.v1_model_bundles_clone_with_changes.post import (
    CloneModelBundleWithChangesV1ModelBundlesCloneWithChangesPost,
)
from launch.api_client.paths.v1_model_bundles_latest.get import (
    GetLatestModelBundleV1ModelBundlesLatestGet,
)
from launch.api_client.paths.v1_model_bundles_model_bundle_id.get import (
    GetModelBundleV1ModelBundlesModelBundleIdGet,
)
from launch.api_client.paths.v1_model_endpoints.get import ListModelEndpointsV1ModelEndpointsGet
from launch.api_client.paths.v1_model_endpoints.post import CreateModelEndpointV1ModelEndpointsPost
from launch.api_client.paths.v1_model_endpoints_api.get import (
    GetModelEndpointsApiV1ModelEndpointsApiGet,
)
from launch.api_client.paths.v1_model_endpoints_model_endpoint_id.delete import (
    DeleteModelEndpointV1ModelEndpointsModelEndpointIdDelete,
)
from launch.api_client.paths.v1_model_endpoints_model_endpoint_id.get import (
    GetModelEndpointV1ModelEndpointsModelEndpointIdGet,
)
from launch.api_client.paths.v1_model_endpoints_model_endpoint_id.put import (
    UpdateModelEndpointV1ModelEndpointsModelEndpointIdPut,
)
from launch.api_client.paths.v1_model_endpoints_schema_json.get import (
    GetModelEndpointsSchemaV1ModelEndpointsSchemaJsonGet,
)
from launch.api_client.paths.v1_streaming_tasks.post import (
    CreateStreamingInferenceTaskV1StreamingTasksPost,
)
from launch.api_client.paths.v1_sync_tasks.post import CreateSyncInferenceTaskV1SyncTasksPost
from launch.api_client.paths.v1_triggers.get import ListTriggersV1TriggersGet
from launch.api_client.paths.v1_triggers.post import CreateTriggerV1TriggersPost
from launch.api_client.paths.v1_triggers_trigger_id.delete import DeleteTriggerV1TriggersTriggerIdDelete
from launch.api_client.paths.v1_triggers_trigger_id.get import GetTriggerV1TriggersTriggerIdGet
from launch.api_client.paths.v1_triggers_trigger_id.put import UpdateTriggerV1TriggersTriggerIdPut
from launch.api_client.paths.v2_model_bundles.get import ListModelBundlesV2ModelBundlesGet
from launch.api_client.paths.v2_model_bundles.post import CreateModelBundleV2ModelBundlesPost
from launch.api_client.paths.v2_model_bundles_clone_with_changes.post import (
    CloneModelBundleWithChangesV2ModelBundlesCloneWithChangesPost,
)
from launch.api_client.paths.v2_model_bundles_latest.get import (
    GetLatestModelBundleV2ModelBundlesLatestGet,
)
from launch.api_client.paths.v2_model_bundles_model_bundle_id.get import (
    GetModelBundleV2ModelBundlesModelBundleIdGet,
)


class DefaultApi(
    CancelFineTuneV1LlmFineTunesFineTuneIdCancelPut,
    CloneModelBundleWithChangesV1ModelBundlesCloneWithChangesPost,
    CloneModelBundleWithChangesV2ModelBundlesCloneWithChangesPost,
    CreateAsyncInferenceTaskV1AsyncTasksPost,
    CreateBatchJobV1BatchJobsPost,
    CreateCompletionStreamTaskV1LlmCompletionsStreamPost,
    CreateCompletionSyncTaskV1LlmCompletionsSyncPost,
    CreateDockerImageBatchJobBundleV1DockerImageBatchJobBundlesPost,
    CreateDockerImageBatchJobV1DockerImageBatchJobsPost,
    CreateFineTuneV1LlmFineTunesPost,
    CreateModelBundleV1ModelBundlesPost,
    CreateModelBundleV2ModelBundlesPost,
    CreateModelEndpointV1LlmModelEndpointsPost,
    CreateModelEndpointV1ModelEndpointsPost,
    CreateStreamingInferenceTaskV1StreamingTasksPost,
    CreateSyncInferenceTaskV1SyncTasksPost,
    CreateTriggerV1TriggersPost,
    DeleteFileV1FilesFileIdDelete,
    DeleteModelEndpointV1ModelEndpointsModelEndpointIdDelete,
    DeleteTriggerV1TriggersTriggerIdDelete,
    DownloadModelEndpointV1LlmModelEndpointsDownloadPost,
    GetAsyncInferenceTaskV1AsyncTasksTaskIdGet,
    GetBatchJobV1BatchJobsBatchJobIdGet,
    GetDockerImageBatchJobModelBundleV1DockerImageBatchJobBundlesDockerImageBatchJobBundleIdGet,
    GetDockerImageBatchJobV1DockerImageBatchJobsBatchJobIdGet,
    GetFileContentV1FilesFileIdContentGet,
    GetFileV1FilesFileIdGet,
    GetFineTuneEventsV1LlmFineTunesFineTuneIdEventsGet,
    GetFineTuneV1LlmFineTunesFineTuneIdGet,
    GetLatestDockerImageBatchJobBundleV1DockerImageBatchJobBundlesLatestGet,
    GetLatestModelBundleV1ModelBundlesLatestGet,
    GetLatestModelBundleV2ModelBundlesLatestGet,
    GetModelBundleV1ModelBundlesModelBundleIdGet,
    GetModelBundleV2ModelBundlesModelBundleIdGet,
    GetModelEndpointV1LlmModelEndpointsModelEndpointNameGet,
    GetModelEndpointV1ModelEndpointsModelEndpointIdGet,
    GetModelEndpointsApiV1ModelEndpointsApiGet,
    GetModelEndpointsSchemaV1ModelEndpointsSchemaJsonGet,
    GetTriggerV1TriggersTriggerIdGet,
    HealthcheckHealthcheckGet,
    HealthcheckHealthzGet,
    HealthcheckReadyzGet,
    ListDockerImageBatchJobModelBundlesV1DockerImageBatchJobBundlesGet,
    ListDockerImageBatchJobsV1DockerImageBatchJobsGet,
    ListFilesV1FilesGet,
    ListFineTunesV1LlmFineTunesGet,
    ListModelBundlesV1ModelBundlesGet,
    ListModelBundlesV2ModelBundlesGet,
    ListModelEndpointsV1LlmModelEndpointsGet,
    ListModelEndpointsV1ModelEndpointsGet,
    ListTriggersV1TriggersGet,
    UpdateBatchJobV1BatchJobsBatchJobIdPut,
    UpdateDockerImageBatchJobV1DockerImageBatchJobsBatchJobIdPut,
    UpdateModelEndpointV1ModelEndpointsModelEndpointIdPut,
    UpdateTriggerV1TriggersTriggerIdPut,
    UploadFileV1FilesPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    pass
