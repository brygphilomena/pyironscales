from pyironscales.endpoints.base.base_endpoint import Endpoint
from pyironscales.endpoints.ironscales.SurveysIdEmailEndpoint import SurveysIdEmailEndpoint


class SurveysIdEndpoint(
    Endpoint,
):
    def __init__(self, client, parent_endpoint=None) -> None:
        Endpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        self.email = self._register_child_endpoint(SurveysIdEmailEndpoint(client, parent_endpoint=self))
