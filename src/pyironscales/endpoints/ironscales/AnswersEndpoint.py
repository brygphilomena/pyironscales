from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.endpoints.ironscales.AnswersIdEndpoint import AnswersIdEndpoint
from pyironscales.endpoints.ironscales.AnswersSearchEndpoint import AnswersSearchEndpoint


class AnswersEndpoint(
    IronscalesEndpoint,
):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "answers", parent_endpoint=parent_endpoint)
        self.search = self._register_child_endpoint(AnswersSearchEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> AnswersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized AnswersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            AnswersIdEndpoint: The initialized AnswersIdEndpoint object.
        """
        child = AnswersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
