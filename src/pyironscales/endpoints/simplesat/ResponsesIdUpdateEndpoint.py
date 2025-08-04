from pyironscales.endpoints.base.base_endpoint import Endpoint
from pyironscales.interfaces import (
    IPuttable,
)
from pyironscales.models.ironscales import Response
from pyironscales.types import (
    JSON,
    RequestParams,
)


class ResponsesIdUpdateEndpoint(
    Endpoint,
    IPuttable[Response, RequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        Endpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IPuttable.__init__(self, Response)

    def put(
        self,
        data: JSON | None = None,
        params: RequestParams | None = None,
    ) -> Response:
        """
        Performs a PUT request against the /responses/{id}/update endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Response: The parsed response data.
        """
        return self._parse_one(
            Response,
            super()._make_request("PUT", data=data, params=params).json(),
        )
