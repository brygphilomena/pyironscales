from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.interfaces import (
    IGettable,
)
from pyironscales.models.ironscales import EscalatedEmails
from pyironscales.types import (
    JSON,
    IronscalesRequestParams,
)


class EmailsIdEndpoint(
    IronscalesEndpoint,
    IGettable[EscalatedEmails, IronscalesRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, EscalatedEmails)

    def get(
        self,
        data: JSON | None = None,
        params: IronscalesRequestParams | None = None,
    ) -> EscalatedEmails:
        """
        Performs a GET request against the /emails/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EscalatedEmails: The parsed response data.
        """
        return self._parse_one(
            EscalatedEmails,
            super()._make_request("GET", data=data, params=params).json(),
        )
