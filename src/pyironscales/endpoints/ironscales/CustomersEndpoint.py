from pyironscales.endpoints.base.base_endpoint import IronscalesEndpoint
from pyironscales.endpoints.ironscales.CustomersIdEndpoint import CustomersIdEndpoint
from pyironscales.endpoints.ironscales.CustomersBulkEndpoint import CustomersBulkEndpoint
from pyironscales.interfaces import (
    IPostable,
)
from pyironscales.models.ironscales import Customer
from pyironscales.types import (
    JSON,
    IronscalesRequestParams,
)


class CustomersEndpoint(
    IronscalesEndpoint,
    IPostable[Customer, IronscalesRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:
        IronscalesEndpoint.__init__(self, client, "customers", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, Customer)
        self.bulk = self._register_child_endpoint(CustomersBulkEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CustomersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CustomersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CustomersIdEndpoint: The initialized CustomersIdEndpoint object.
        """
        child = CustomersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def post(self, data: JSON | None = None, params: IronscalesRequestParams | None = None) -> Customer:
        """
        Performs a POST request against the /customers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Customer: The parsed response data.
        """
        return self._parse_one(Customer, super()._make_request("POST", data=data, params=params).json())
