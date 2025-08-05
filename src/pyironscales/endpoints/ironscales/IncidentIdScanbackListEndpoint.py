from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.interfaces import (
    IGettable,
)
from pyironscales.models.ironscales import ScanbackIncidents
from pyironscales.types import (
    JSON,
    IronscalesRequestParams,
)


class IncidentIdScanbackListEndpoint(
    IronscalesEndpoint,
    IGettable[ScanbackIncidents, IronscalesRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "scanback-list/", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ScanbackIncidents)

    def get(
        self,
        data: JSON | None = None,
        params: IronscalesRequestParams | None = None,
    ) -> ScanbackIncidents:
        """
        Performs a GET request against the /incident/{id}/scanback-list endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScanbackIncidents: The parsed response data.
        """
        return self._parse_many(
            ScanbackIncidents,
            super()._make_request("GET", data=data, params=params).json().get('incidents', {}),
        )
