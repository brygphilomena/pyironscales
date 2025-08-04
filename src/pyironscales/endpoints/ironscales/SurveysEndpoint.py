from pyironscales.endpoints.base.base_endpoint import Endpoint
from pyironscales.endpoints.ironscales.SurveysIdEndpoint import SurveysIdEndpoint
from pyironscales.interfaces import (
    IGettable,
)
from pyironscales.models.ironscales import Survey
from pyironscales.types import (
    JSON,
    RequestParams,
)


class SurveysEndpoint(
    Endpoint,
    IGettable[Survey, RequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        Endpoint.__init__(self, client, "surveys", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Survey)

    def id(self, id: int) -> SurveysIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SurveysIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SurveysIdEndpoint: The initialized SurveysIdEndpoint object.
        """
        child = SurveysIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def get(
        self,
        data: JSON | None = None,
        params: RequestParams | None = None,
    ) -> Survey:
        """
        Performs a GET request against the /surveys endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        print("get")
        return self._parse_many(
            Survey,
            super()._make_request("GET", data=data, params=params).json().get('surveys', {}),
        )
