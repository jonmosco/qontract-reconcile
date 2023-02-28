from collections.abc import Iterable, Sequence
from typing import Any, Optional

from reconcile import queries
from reconcile.glitchtip.reconciler import GlitchtipReconciler
from reconcile.gql_definitions.glitchtip.glitchtip_instance import (
    DEFINITION as GLITCHTIP_INSTANCE_DEFINITION,
)
from reconcile.gql_definitions.glitchtip.glitchtip_instance import (
    query as glitchtip_instance_query,
)
from reconcile.gql_definitions.glitchtip.glitchtip_project import (
    DEFINITION as GLITCHTIP_PROJECT_DEFINITION,
)
from reconcile.gql_definitions.glitchtip.glitchtip_project import (
    GlitchtipProjectsV1,
    RoleV1,
)
from reconcile.gql_definitions.glitchtip.glitchtip_project import (
    query as glitchtip_project_query,
)
from reconcile.gql_definitions.glitchtip.glitchtip_settings import (
    query as glitchtip_settings_query,
)
from reconcile.utils import gql
from reconcile.utils.glitchtip import (
    GlitchtipClient,
    Organization,
    Project,
    Team,
    User,
)
from reconcile.utils.secret_reader import SecretReader

from reconcile.utils.oc_map import (
    OCMap,
    init_oc_map_from_namespaces,
)


from reconcile.utils.openshift_resource import OpenshiftResource as OR
from reconcile.utils.openshift_resource import ResourceInventory
from reconcile.utils.secret_reader import create_secret_reader

QONTRACT_INTEGRATION = "glitchtip_project_dsn"


class GlitchtipException(Exception):
    pass

# all existing secrets from all namespaces that has the DSN
# add the secrets into the resource inventory which will be the current state
# resource inventory will be the object (what is in the cluster)
# fetching the DSNs
# Use an OC map on all the clusters
# return a relation of project and keys from the clusters
def fetch_current_dsn(
    glitchtip_client: GlitchtipClient, glitchtip_projects: Iterable[GlitchtipProjectsV1]
) -> list[[project_dsn]:
    projects_dsn = dict() 
    for project in glitchtip_projects:
        projects_dsn[f"{slugify(project.organization.name)-slugify(project.name)}"] = glitchtip_client.project_keys(
            organization_slug=slugify(project.organizatoin.name), project_slug=slugify(project.name)
        )

    ocm_map = OCMMap(
            clusters=clusters,
            integration=QONTRACT_INTEGRATION,
            settings=settings,
            init_addons=True,
        )

    return project_dsn


# input will be the resource inventory object
# what should be in the cluster
def fetch_desired_state(
    glitchtip_projects: Sequence[GlitchtipProjectsV1], mail_domain: str
) -> list[Organization]:
    # need to have as input: graphql query of projects in a namespace
    # merge together 


# create the secret object
def run(dry_run: bool, instance: Optional[str] = None) -> None:
    gqlapi = gql.get_api()
    secret_reader = SecretReader(queries.get_secret_reader_settings())
    read_timeout = 30
    max_retries = 3
    if _s := glitchtip_settings_query(query_func=gqlapi.query).settings:
        if _gs := _s[0].glitchtip:
            if _gs.read_timeout is not None:
                read_timeout = _gs.read_timeout
            if _gs.max_retries is not None:
                max_retries = _gs.max_retries

    glitchtip_instances = glitchtip_instance_query(query_func=gqlapi.query).instances
    glitchtip_projects = (
        glitchtip_project_query(query_func=gqlapi.query).glitchtip_projects or []
    )
    # iterate over projects and fetch the DSN.  Create project:key relationship

    for glitchtip_instance in glitchtip_instances:
        if instance and glitchtip_instance.name != instance:
            continue

        glitchtip_client = GlitchtipClient(
            host=glitchtip_instance.console_url,
            token=secret_reader.read_secret(glitchtip_instance.automation_token),
            read_timeout=read_timeout,
            max_retries=max_retries,
        )
