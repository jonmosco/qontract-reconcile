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

from reconcile.gql_definitions.fragments.jumphost_common_fields import (
    CommonJumphostFields,
)
from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
fragment CommonJumphostFields on ClusterJumpHost_v1 {
  hostname
  knownHosts
  user
  port
  remotePort
  identity {
    ... VaultSecret
  }
}

fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query TerraformCloudflareResources {
  namespaces: namespaces_v1 {
    name
    clusterAdmin
    cluster {
      name
      serverUrl
      insecureSkipTLSVerify
      jumpHost {
        ... CommonJumphostFields
      }
      automationToken {
        ... VaultSecret
      }
      clusterAdminAutomationToken {
        ... VaultSecret
      }
      spec {
        region
      }
      internal
      disable {
        integrations
        e2eTests
      }
    }
    managedExternalResources
    externalResources {
      ... on NamespaceTerraformProviderResourceCloudflare_v1 {
        provider
        provisioner {
          name
        }
        resources {
          provider
          ... on NamespaceTerraformResourceCloudflareWorkerScript_v1
          {
            identifier
            name
            content_from_github {
              repo
              path
              ref
            }
            vars {
              name
              text
            }
          }
          ... on NamespaceTerraformResourceCloudflareZone_v1
          {
            identifier
            zone
            plan
            type
            settings
            argo {
              smart_routing
              tiered_caching
            }
            cache_reserve {
              enabled
            }
            records {
              identifier
              name
              type
              ttl
              value
              proxied
            }
            workers {
              identifier
              pattern
              script_name
            }
            certificates {
              identifier
              type
              hosts
              validation_method
              validity_days
              certificate_authority
              cloudflare_branding
              wait_for_active_status
            }
          }
        }
      }
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterSpecV1(ConfiguredBaseModel):
    region: str = Field(..., alias="region")


class DisableClusterAutomationsV1(ConfiguredBaseModel):
    integrations: Optional[list[str]] = Field(..., alias="integrations")
    e2e_tests: Optional[list[str]] = Field(..., alias="e2eTests")


class ClusterV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    server_url: str = Field(..., alias="serverUrl")
    insecure_skip_tls_verify: Optional[bool] = Field(..., alias="insecureSkipTLSVerify")
    jump_host: Optional[CommonJumphostFields] = Field(..., alias="jumpHost")
    automation_token: Optional[VaultSecret] = Field(..., alias="automationToken")
    cluster_admin_automation_token: Optional[VaultSecret] = Field(
        ..., alias="clusterAdminAutomationToken"
    )
    spec: Optional[ClusterSpecV1] = Field(..., alias="spec")
    internal: Optional[bool] = Field(..., alias="internal")
    disable: Optional[DisableClusterAutomationsV1] = Field(..., alias="disable")


class NamespaceExternalResourceV1(ConfiguredBaseModel):
    ...


class CloudflareAccountV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")


class NamespaceTerraformResourceCloudflareV1(ConfiguredBaseModel):
    provider: str = Field(..., alias="provider")


class CloudflareZoneWorkerScriptContentFromGithubV1(ConfiguredBaseModel):
    repo: str = Field(..., alias="repo")
    path: str = Field(..., alias="path")
    ref: str = Field(..., alias="ref")


class CloudflareZoneWorkerScriptVarsV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    text: str = Field(..., alias="text")


class NamespaceTerraformResourceCloudflareWorkerScriptV1(
    NamespaceTerraformResourceCloudflareV1
):
    identifier: str = Field(..., alias="identifier")
    name: str = Field(..., alias="name")
    content_from_github: Optional[
        CloudflareZoneWorkerScriptContentFromGithubV1
    ] = Field(..., alias="content_from_github")
    vars: Optional[list[CloudflareZoneWorkerScriptVarsV1]] = Field(..., alias="vars")


class CloudflareZoneArgoV1(ConfiguredBaseModel):
    smart_routing: Optional[bool] = Field(..., alias="smart_routing")
    tiered_caching: Optional[bool] = Field(..., alias="tiered_caching")


class CloudflareZoneCacheReserveV1(ConfiguredBaseModel):
    enabled: Optional[bool] = Field(..., alias="enabled")


class CloudflareDnsRecordV1(ConfiguredBaseModel):
    identifier: str = Field(..., alias="identifier")
    name: str = Field(..., alias="name")
    q_type: str = Field(..., alias="type")
    ttl: int = Field(..., alias="ttl")
    value: Optional[str] = Field(..., alias="value")
    proxied: Optional[bool] = Field(..., alias="proxied")


class CloudflareZoneWorkerV1(ConfiguredBaseModel):
    identifier: str = Field(..., alias="identifier")
    pattern: str = Field(..., alias="pattern")
    script_name: str = Field(..., alias="script_name")


class CloudflareZoneCertificateV1(ConfiguredBaseModel):
    identifier: str = Field(..., alias="identifier")
    q_type: str = Field(..., alias="type")
    hosts: list[str] = Field(..., alias="hosts")
    validation_method: str = Field(..., alias="validation_method")
    validity_days: int = Field(..., alias="validity_days")
    certificate_authority: str = Field(..., alias="certificate_authority")
    cloudflare_branding: Optional[bool] = Field(..., alias="cloudflare_branding")
    wait_for_active_status: Optional[bool] = Field(..., alias="wait_for_active_status")


class NamespaceTerraformResourceCloudflareZoneV1(
    NamespaceTerraformResourceCloudflareV1
):
    identifier: str = Field(..., alias="identifier")
    zone: str = Field(..., alias="zone")
    plan: Optional[str] = Field(..., alias="plan")
    q_type: Optional[str] = Field(..., alias="type")
    settings: Optional[Json] = Field(..., alias="settings")
    argo: Optional[CloudflareZoneArgoV1] = Field(..., alias="argo")
    cache_reserve: Optional[CloudflareZoneCacheReserveV1] = Field(
        ..., alias="cache_reserve"
    )
    records: Optional[list[CloudflareDnsRecordV1]] = Field(..., alias="records")
    workers: Optional[list[CloudflareZoneWorkerV1]] = Field(..., alias="workers")
    certificates: Optional[list[CloudflareZoneCertificateV1]] = Field(
        ..., alias="certificates"
    )


class NamespaceTerraformProviderResourceCloudflareV1(NamespaceExternalResourceV1):
    provider: str = Field(..., alias="provider")
    provisioner: CloudflareAccountV1 = Field(..., alias="provisioner")
    resources: list[
        Union[
            NamespaceTerraformResourceCloudflareZoneV1,
            NamespaceTerraformResourceCloudflareWorkerScriptV1,
            NamespaceTerraformResourceCloudflareV1,
        ]
    ] = Field(..., alias="resources")


class NamespaceV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    cluster_admin: Optional[bool] = Field(..., alias="clusterAdmin")
    cluster: ClusterV1 = Field(..., alias="cluster")
    managed_external_resources: Optional[bool] = Field(
        ..., alias="managedExternalResources"
    )
    external_resources: Optional[
        list[
            Union[
                NamespaceTerraformProviderResourceCloudflareV1,
                NamespaceExternalResourceV1,
            ]
        ]
    ] = Field(..., alias="externalResources")


class TerraformCloudflareResourcesQueryData(ConfiguredBaseModel):
    namespaces: Optional[list[NamespaceV1]] = Field(..., alias="namespaces")


def query(query_func: Callable, **kwargs: Any) -> TerraformCloudflareResourcesQueryData:
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
        TerraformCloudflareResourcesQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return TerraformCloudflareResourcesQueryData(**raw_data)
