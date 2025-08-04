import typing
from datetime import datetime, timedelta, timezone

from pyironscales.clients.base_client import IronscalesClient
from pyironscales.config import Config

if typing.TYPE_CHECKING:
    from pyironscales.endpoints.ironscales.SurveysEndpoint import SurveysEndpoint
    from pyironscales.endpoints.ironscales.AnswersEndpoint import AnswersEndpoint
    from pyironscales.endpoints.ironscales.CustomersEndpoint import CustomersEndpoint
    from pyironscales.endpoints.ironscales.QuestionsEndpoint import QuestionsEndpoint
    from pyironscales.endpoints.ironscales.TeamMembersEndpoint import TeamMembersEndpoint
    from pyironscales.endpoints.ironscales.ResponsesEndpoint import ResponsesEndpoint


class IronscalesAPIClient(IronscalesClient):
    """
    Ironscales API client. Handles the connection to the Ironscales API
    and the configuration of all the available endpoints.
    """

    def __init__(
        self,
        privatekey: str,
        scope: str,
    ) -> None:
        """
        Initializes the client with the given credentials.

        Parameters:
            privatekey (str): Your Ironscales API private key.
        """
        self.privatekey: str = privatekey
        self.scope: list = scope
        self.token_expiry_time: datetime = datetime.now(tz=timezone.utc)

        # Grab first access token
        self.access_token: str = self._get_access_token()

    # Initializing endpoints
    @property
    def surveys(self) -> "SurveysEndpoint":
        from pyironscales.endpoints.ironscales.SurveysEndpoint import SurveysEndpoint

        return SurveysEndpoint(self)

    def _get_url(self) -> str:
        """
        Generates and returns the URL for the Ironscales API endpoints based on the company url and codebase.
        Logs in an obtains an access token.
        Returns:
            str: API URL.
        """
        return f"https://appapi.ironscales.com/appapi"

    def _get_access_token(self) -> str:
        """
        Performs a request to the ConnectWise Automate API to obtain an access token.
        """
        auth_response = self._make_request(
            "POST",
            f"{self._get_url()}/get-token/",
            data={
                "key": self.privatekey,
                "scopes": self.scope
                },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json"
                },
        )
        auth_resp_json = auth_response.json()
        token = auth_resp_json["jwt"]
        expires_in_sec = auth_resp_json["expires_in"]
        self.token_expiry_time = datetime.now(tz=timezone.utc) + timedelta(seconds=expires_in_sec)
        return token

    def _refresh_access_token_if_necessary(self):
        if datetime.now(tz=timezone.utc) > self.token_expiry_time:
            self.access_token = self._get_access_token()

    def _get_headers(self) -> dict[str, str]:
        """
        Generates and returns the headers required for making API requests. The access token is refreshed if necessary before returning.

        Returns:
            dict[str, str]: Dictionary of headers including Content-Type, Client ID, and Authorization.
        """
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.access_token}",
        }
