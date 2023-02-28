import logging
from collections.abc import (
    Iterable,
    Sequence,
)
from typing import Any

from reconcile.utils.glitchtip import (
    GlitchtipClient,
    Organization,
    Project,
    Team,
    User,
)

import reconcile.openshift_base as ob
from reconcile.utils.oc_map import OCMap
from reconcile.utils.openshift_resource import OpenshiftResource as OR
from reconcile.utils.openshift_resource import ResourceInventory


def get_glitchtip_key(oc_map: OCMap, name: str) -> dict[str, Any]:
    """Get a connection token secret from the site's namespace."""
    oc = oc_map.get_cluster(site.cluster.name)
    return oc.get(site.namespace.name, "Secret", name, allow_not_found=True)


def create_glitchtip_key(
    oc_map: OCMap,
    connected_site: SkupperSite,
    dry_run: bool,
    integration: str,
    integration_version: str,
) -> None:
    """Create a DSN project key in the site's namespace."""
    oc = oc_map.get_cluster(connected_site.cluster.name)
    logging.info(f"{connected_site}: Creating new connection token for {site}")
    sc = get_site_controller(connected_site)
    if not dry_run:
        oc.apply(
            connected_site.namespace.name,
            resource=OR(
                body=sc.site_token(
                    connected_site.unique_token_name(site), site.token_labels
                ),
                integration=integration,
                integration_version=integration_version,
            ),
        )
        
def reconcile(
    self,
    current: Sequence[Organization],
    desired: Iterable[Organization],
) -> None:
    for desired_org in desired:
        if desired_org not in current:
            logging.info(
                ["create_organization", desired_org.name, self.client.host]
            )
            if not self.dry_run:
                current_org = self.client.create_organization(name=desired_org.name)
            else:
                # dry-run mode - use empty Org and go ahead
                current_org = Organization(name=desired_org.name)
        else:
            current_org = current[current.index(desired_org)]

        organization_slug = current_org.slug
        organization_users = self._reconcile_users(
            organization_slug=organization_slug,
            current_users=current_org.users,
            desired_users=desired_org.users,
        )
        organization_teams = self._reconcile_teams(
            organization_slug=organization_slug,
            organization_users=organization_users,
            current_teams=current_org.teams,
            desired_teams=desired_org.teams,
        )
        self._reconcile_projects(
            organization_slug=organization_slug,
            organization_teams=organization_teams,
            current_projects=current_org.projects,
            desired_projects=desired_org.projects,
        )
