thonimport requests
from requests.adapters import HTTPAdapter, Retry
from utils.logger import get_logger

logger = get_logger(__name__)

class HttpClient:
    def __init__(self, proxy=None):
        self.session = requests.Session()
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        self.session.mount("https://", HTTPAdapter(max_retries=retries))
        self.proxy = proxy

    def get(self, url, **kwargs):
        logger.debug(f"GET request to {url}")
        try:
            response = self.session.get(url, proxies=self.proxy, timeout=10, **kwargs)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"HTTP request failed: {e}")
            return None