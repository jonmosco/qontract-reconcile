"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.deplopy_resources import DeployResourcesFields


DEFINITION = """
fragment DeployResourcesFields on DeployResources_v1 {
  requests {
    cpu
    memory
  }
  limits {
    cpu
    memory
  }
}

query ExternalResourcesSettings {
    settings: external_resources_settings_v1 {
        state_dynamodb_account {
            name
        }
        state_dynamodb_table
        state_dynamodb_region
        workers_cluster {
            name
        }
        workers_namespace {
            name
        }
        tf_state_bucket
        tf_state_region
        tf_state_dynamodb_table
        vault_secrets_path
        outputs_secret_image
        outputs_secret_version
        module_default_resources {
          ... DeployResourcesFields
        }
    }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class AWSAccountV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class ClusterV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class NamespaceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class ExternalResourcesSettingsV1(ConfiguredBaseModel):
    state_dynamodb_account: AWSAccountV1 = Field(..., alias="state_dynamodb_account")
    state_dynamodb_table: str = Field(..., alias="state_dynamodb_table")
    state_dynamodb_region: str = Field(..., alias="state_dynamodb_region")
    workers_cluster: ClusterV1 = Field(..., alias="workers_cluster")
    workers_namespace: NamespaceV1 = Field(..., alias="workers_namespace")
    tf_state_bucket: Optional[str] = Field(..., alias="tf_state_bucket")
    tf_state_region: Optional[str] = Field(..., alias="tf_state_region")
    tf_state_dynamodb_table: Optional[str] = Field(..., alias="tf_state_dynamodb_table")
    vault_secrets_path: str = Field(..., alias="vault_secrets_path")
    outputs_secret_image: str = Field(..., alias="outputs_secret_image")
    outputs_secret_version: str = Field(..., alias="outputs_secret_version")
    module_default_resources: DeployResourcesFields = Field(..., alias="module_default_resources")


class ExternalResourcesSettingsQueryData(ConfiguredBaseModel):
    settings: Optional[list[ExternalResourcesSettingsV1]] = Field(..., alias="settings")


def query(query_func: Callable, **kwargs: Any) -> ExternalResourcesSettingsQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        ExternalResourcesSettingsQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return ExternalResourcesSettingsQueryData(**raw_data)
