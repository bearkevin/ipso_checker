from typing import Dict

USERAGENT: str = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'
REQUEST_HEADERS: dict[str, str] = {"User-Agent": USERAGENT}

APPLE_IPSW_XML: str = 'http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wa/com.apple.jingle.appserver.client.MZITunesClientCheck/version'

macOS_IPSW_XML: str = 'https://mesu.apple.com/assets/macos/com_apple_macOSIPSW/com_apple_macOSIPSW.xml'