from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.interfaces import (
    IGettable,
)
from pyironscales.models.ironscales import Incidents
from pyironscales.types import (
    JSON,
    IronscalesRequestParams,
)


class IncidentIdListEndpoint(
    IronscalesEndpoint,
    IGettable[Incidents, IronscalesRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "list/", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Incidents)

    def get(
        self,
        data: JSON | None = None,
        params: IronscalesRequestParams | None = None,
    ) -> Incidents:
        """
        Performs a GET request against the /incident/{id}/list/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Incidents: The parsed response data.
        """
        return self._parse_many(
            Incidents,
            super()._make_request("GET", data=data, params=params).json().get('incidents', {}),
        )
