from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.interfaces import (
    IGettable,
)
from pyironscales.models.ironscales import CompanyMailboxes
from pyironscales.types import (
    JSON,
    IronscalesRequestParams,
)


class CompanyIdAutoSyncMailboxesEndpoint(
    IronscalesEndpoint,
    IGettable[CompanyMailboxes, IronscalesRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "mailboxes/", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, CompanyMailboxes)

    def get(
        self,
        data: JSON | None = None,
        params: IronscalesRequestParams | None = None,
    ) -> CompanyMailboxes:
        """
        Performs a GET request against the /company/{id}/auto-sync/mailboxes/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyMailboxes: The parsed response data.
        """
        return self._parse_many(
            CompanyMailboxes,
            super()._make_request("GET", data=data, params=params).json().get('emails', {}),
        )
