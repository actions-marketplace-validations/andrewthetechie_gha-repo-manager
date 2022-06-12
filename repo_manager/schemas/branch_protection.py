from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel  # pylint: disable=E0611
from pydantic import conint
from pydantic import Field
from pydantic import HttpUrl  # pylint: disable=E0611

OptBool = Optional[bool]
OptStr = Optional[str]


class RestrictionOptions(BaseModel):
    apps: Optional[List[str]] = Field(None, description="List of App names that cannot push to this branch")
    users: Optional[List[str]] = Field(
        None, description="List of users who cannot push to this branch, only available to orgs"
    )
    teams: Optional[List[str]] = Field(
        None, description="List of teams who cannot push to this branch, only available to orgs"
    )


class StatusChecksOptions(BaseModel):
    strict: OptBool = Field(None, description="Require branches to be up to date before merging.")
    checks: Optional[List[str]] = Field(
        None, description="The list of status checks to require in order to merge into this branch"
    )


class DismissalOptions(BaseModel):
    users: Optional[List[str]] = Field(
        None, description="List of users who can dismiss pull request reviews, only available to orgs"
    )
    teams: Optional[List[str]] = Field(
        None, description="List of teams who can dismiss pull request reviews, only available to orgs"
    )


class PROptions(BaseModel):
    required_approving_review_count: Optional[conint(ge=1, le=6)] = Field(
        None, description="The number of approvals required. (1-6)"
    )
    dismiss_stale_reviews: OptBool = Field(
        None, description="Dismiss approved reviews automatically when a new commit is pushed."
    )
    require_code_owner_reviews: OptBool = Field(None, description="Blocks merge until code owners have reviewed.")
    dismissal_restrictions: Optional[DismissalOptions] = Field(
        None, description="Options related to PR dismissal. Only available to Orgs."
    )


class ProtectionOptions(BaseModel):
    required_pull_request_reviews: Optional[PROptions] = Field(None, description="Options related to PR reviews")
    required_status_checks: Optional[StatusChecksOptions] = Field(
        None, description="Options related to required status checks"
    )
    enforce_admins: OptBool = Field(
        None,
        description="Enforce all configured restrictions for administrators. Set to true to enforce required status checks for repository administrators. Set to null to disable.",
    )
    required_linear_history: OptBool = Field(
        None, description="Prevent merge commits from being pushed to matching branches"
    )
    restrictions: Optional[RestrictionOptions] = Field(
        None, description="Options related to restricting who can push to this branch"
    )


class BranchProtection(BaseModel):
    name: OptStr = Field(None, description="Name of the branch")
    protection: Optional[ProtectionOptions] = Field(None, description="Protection options for the branch")
