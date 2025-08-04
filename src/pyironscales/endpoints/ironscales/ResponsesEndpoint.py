from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.endpoints.ironscales.ResponsesIdEndpoint import ResponsesIdEndpoint
from pyironscales.endpoints.ironscales.ResponsesSearchEndpoint import ResponsesSearchEndpoint
from pyironscales.endpoints.ironscales.ResponsesCreateOrUpdateEndpoint import ResponsesCreateOrUpdateEndpoint


class ResponsesEndpoint(
    IronscalesEndpoint,
):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "responses", parent_endpoint=parent_endpoint)
        self.search = self._register_child_endpoint(ResponsesSearchEndpoint(client, parent_endpoint=self))
        self.createorupdate = self._register_child_endpoint(ResponsesCreateOrUpdateEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ResponsesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ResponsesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ResponsesIdEndpoint: The initialized ResponsesIdEndpoint object.
        """
        child = ResponsesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
