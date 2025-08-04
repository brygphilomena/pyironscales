from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.interfaces import (
    IPostable,
    IPaginateable,
)
from pyironscales.models.ironscales import Answer
from pyironscales.responses.paginated_response import PaginatedResponse
from pyironscales.types import (
    JSON,
    IronscalesRequestParams,
)


class AnswersSearchEndpoint(
    IronscalesEndpoint,
    IPostable[Answer, IronscalesRequestParams],
    IPaginateable[Answer, IronscalesRequestParams],

):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "search", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Answer)
        IPaginateable.__init__(self, Answer)

    def paginated(
        self,
        page: int,
        limit: int,
        params: IronscalesRequestParams | None = None,
    ) -> PaginatedResponse[Answer]:
        """
        Performs a POST request against the /answers/search endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            limit (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Answer]: The initialized PaginatedResponse object.
        """
        if params:
            params["page[number]"] = page
            params["page[size]"] = limit
        else:
            params = {"page[number]": page, "page[size]": limit}
        return PaginatedResponse(
            super()._make_request("POST", params=params),
            Answer,
            self,
            "answers",
            page,
            limit,
            params,
        )

    def post(self, data: JSON | None = None, params: IronscalesRequestParams | None = None) -> Answer:
        """
        Performs a POST request against the /answers/search endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        return self._parse_many(Answer, super()._make_request("POST", data=data, params=params).json().get('answers', {}))
