from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.interfaces import (
    IPostable,
)
from pyironscales.models.ironscales import Response
from pyironscales.types import (
    JSON,
    IronscalesRequestParams,
)


class ResponsesCreateOrUpdateEndpoint(
    IronscalesEndpoint,
    IPostable[Response, IronscalesRequestParams],

):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "create-or-update", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Response)

    def post(self, data: JSON | None = None, params: IronscalesRequestParams | None = None) -> Response:
        """
        Performs a POST request against the /responses/create-or-update endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        return self._parse_one(Response, super()._make_request("POST", data=data, params=params).json())
