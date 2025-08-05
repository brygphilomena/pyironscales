from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.interfaces import (
    IGettable,
)
from pyironscales.models.ironscales import IncidentDetails
from pyironscales.types import (
    JSON,
    IronscalesRequestParams,
)

class MitigationsIdIncidentsDetailsEndpoint(
    IronscalesEndpoint,
    IGettable[IncidentDetails, IronscalesRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "details/", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, IncidentDetails)

    def get(
        self,
        data: JSON | None = None,
        params: IronscalesRequestParams | None = None,
    ) -> IncidentDetails:
        """
        Performs a GET request against the /mitigations/{id}/incidents/details/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            IncidentDetails: The parsed response data.
        """
        return self._parse_many(
            IncidentDetails,
            super()._make_request("GET", data=data, params=params).json().get('incidents', {}),
        )
