from pyironscales.endpoints.base.base_endpoint import Endpoint
from pyironscales.interfaces import (
    IPostable,
    IPaginateable,
)
from pyironscales.models.ironscales import Response
from pyironscales.responses.paginated_response import PaginatedResponse
from pyironscales.types import (
    JSON,
    RequestParams,
)


class ResponsesSearchEndpoint(
    Endpoint,
    IPostable[Response, RequestParams],
    IPaginateable[Response, RequestParams],

):
    def __init__(self, client, parent_endpoint=None) -> None:
        Endpoint.__init__(self, client, "search", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Response)
        IPaginateable.__init__(self, Response)

    def paginated(
        self,
        page: int,
        limit: int,
        params: RequestParams | None = None,
    ) -> PaginatedResponse[Response]:
        """
        Performs a POST request against the /responses/search endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Response]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("POST", params=params),
            Response,
            self,
            "responses",
            page,
            limit,
            params,
        )


    #TODO: How do I paginate a post?
    def post(self, data: JSON | None = None, params: RequestParams | None = None) -> Response:
        """
        Performs a POST request against the /responses/search endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        return self._parse_many(Response, super()._make_request("POST", data=data, params=params).json().get('responses', {}))
