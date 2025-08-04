from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.interfaces import (
    IPostable,
)
from pyironscales.models.ironscales import SurveyEmail
from pyironscales.types import (
    JSON,
    IronscalesRequestParams,
)


class SurveysIdEmailEndpoint(
    IronscalesEndpoint,
    IPostable[SurveyEmail, IronscalesRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "email", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, SurveyEmail)


    def post(self, data: JSON | None = None, params: IronscalesRequestParams | None = None) -> SurveyEmail:
        """
        Performs a POST request against the /surveys/{id}/email endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyEmail: The parsed response data.
        """
        return self._parse_one(SurveyEmail, super()._make_request("POST", data=data, params=params).json())
