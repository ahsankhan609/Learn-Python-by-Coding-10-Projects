"""
Website Status Checker - Advanced Version
Checks website status, response time, SSL certificate info, and more.
Supports batch checking, redirects, and detailed reporting.
"""

import json
import socket
import ssl
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, List, Tuple
from urllib.parse import urlparse

import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict


@dataclass
class WebsiteStatus:
    """Data class to hold website status information"""
    url: str
    is_online: bool
    status_code: Optional[int] = None
    response_time: Optional[float] = None
    content_type: Optional[str] = None
    server: Optional[str] = None
    title: Optional[str] = None
    ssl_valid: Optional[bool] = None
    redirect_url: Optional[str] = None
    error_message: Optional[str] = None
    checked_at: str = None

    def __post_init__(self):
        if self.checked_at is None:
            self.checked_at = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'url': self.url,
            'is_online': self.is_online,
            'status_code': self.status_code,
            'response_time': f"{self.response_time:.2f}s" if self.response_time else None,
            'content_type': self.content_type,
            'server': self.server,
            'title': self.title,
            'ssl_valid': self.ssl_valid,
            'redirect_url': self.redirect_url,
            'error_message': self.error_message,
            'checked_at': self.checked_at
        }


def validate_url(url: str) -> Tuple[bool, str]:
    """
    Validate URL format
    Returns: (is_valid, normalized_url)
    """
    if not url:
        return False, "URL cannot be empty"

    # Add https:// if no scheme provided
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        result = urlparse(url)
        if not result.netloc:
            return False, "Invalid URL format"
        return True, url
    except Exception as e:
        return False, str(e)


def check_ssl_certificate(hostname: str) -> bool:
    """
    Check if SSL certificate is valid
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                return True
    except Exception:
        return False


def extract_title(html_content: str) -> Optional[str]:
    """
    Extract page title from HTML content
    """
    try:
        start = html_content.lower().find('<title>')
        end = html_content.lower().find('</title>')
        if start != -1 and end != -1:
            return html_content[start + 7:end].strip()
    except Exception:
        pass
    return None


def check_website_status(
        website_url: str,
        timeout: int = 10,
        allow_redirects: bool = True
) -> WebsiteStatus:
    """
    Check website status and gather detailed information

    Args:
        website_url: URL to check
        timeout: Request timeout in seconds
        allow_redirects: Follow redirects or not

    Returns:
        WebsiteStatus object with all collected information
    """

    # Validate URL
    is_valid, normalized_url = validate_url(website_url)
    if not is_valid:
        return WebsiteStatus(
            url=website_url,
            is_online=False,
            error_message=f"Invalid URL: {normalized_url}"
        )

    try:
        response: Response = requests.get(
            normalized_url,
            timeout=timeout,
            allow_redirects=allow_redirects,
            verify=True
        )

        # Extract information
        status_code: int = response.status_code
        headers: CaseInsensitiveDict = CaseInsensitiveDict(response.headers)
        content_type: str = headers.get('Content-Type', 'Unknown')
        server: str = headers.get('Server', 'Unknown')
        response_time: float = response.elapsed.total_seconds()

        # Extract page title
        title = None
        if 'text/html' in content_type:
            title = extract_title(response.text)

        # Check SSL certificate
        hostname = urlparse(normalized_url).netloc
        ssl_valid = check_ssl_certificate(hostname)

        # Determine if online
        is_online = 200 <= status_code < 400

        # Check for redirects
        redirect_url = None
        if response.history:
            redirect_url = response.url

        return WebsiteStatus(
            url=normalized_url,
            is_online=is_online,
            status_code=status_code,
            response_time=response_time,
            content_type=content_type,
            server=server,
            title=title,
            ssl_valid=ssl_valid,
            redirect_url=redirect_url
        )

    except requests.Timeout:
        return WebsiteStatus(
            url=normalized_url,
            is_online=False,
            error_message=f"Request timeout after {timeout} seconds"
        )
    except requests.ConnectionError as e:
        return WebsiteStatus(
            url=normalized_url,
            is_online=False,
            error_message=f"Connection error: {str(e)}"
        )
    except RequestException as e:
        return WebsiteStatus(
            url=normalized_url,
            is_online=False,
            error_message=f"Request error: {str(e)}"
        )
    except Exception as e:
        return WebsiteStatus(
            url=normalized_url,
            is_online=False,
            error_message=f"Unexpected error: {str(e)}"
        )


def check_multiple_websites(urls: List[str]) -> List[WebsiteStatus]:
    """
    Check status of multiple websites

    Args:
        urls: List of website URLs

    Returns:
        List of WebsiteStatus objects
    """
    results = []
    for url in urls:
        print(f"Checking {url}...", end=" ")
        status = check_website_status(url)
        results.append(status)
        print(f"{'✓ Online' if status.is_online else '✗ Offline'}")
    return results


def print_status(status: WebsiteStatus) -> None:
    """Pretty print website status"""
    status_indicator = "✓ ONLINE" if status.is_online else "✗ OFFLINE"

    print("\n" + "=" * 60)
    print(f"Website Status Check - {status_indicator}")
    print("=" * 60)
    print(f"URL: {status.url}")
    print(f"Checked at: {status.checked_at}")

    if status.is_online:
        print(f"Status Code: {status.status_code}")
        print(f"Response Time: {status.response_time:.2f} seconds")
        print(f"Content Type: {status.content_type}")
        print(f"Server: {status.server}")
        if status.title:
            print(f"Page Title: {status.title}")
        if status.redirect_url:
            print(f"Redirected to: {status.redirect_url}")
        print(f"SSL Certificate Valid: {'Yes ✓' if status.ssl_valid else 'No ✗'}")
    else:
        print(f"Error: {status.error_message}")

    print("=" * 60 + "\n")


def export_results(results: List[WebsiteStatus], filename: str = "website_status.json") -> None:
    """Export results to JSON file"""
    data = [result.to_dict() for result in results]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Results exported to {filename}")


def main() -> None:
    # Single website check
    print("Single Website Check:")
    status = check_website_status('https://indently.io')
    print_status(status)

    # Multiple websites check
    print("\nMultiple Websites Check:")
    urls = [
        'https://google.com',
        'https://github.com',
        'https://invalid-website-12345.com'
    ]

    results = check_multiple_websites(urls)

    # Export results
    export_results(results, 'my_report.json')

    # Summary statistics
    online_count = sum(1 for r in results if r.is_online)
    print(f"\nSummary: {online_count}/{len(results)} websites are online")


if __name__ == '__main__':
    main()
