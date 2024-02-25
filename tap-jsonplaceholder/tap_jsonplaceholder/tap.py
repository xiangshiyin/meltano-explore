"""jsonplaceholder tap class."""

from typing import List

from singer_sdk import Tap, Stream

from singer_sdk import typing as th  # JSON schema typing helpers

from tap_jsonplaceholder.streams import jsonplaceholderStream, CommentsStream


STREAM_TYPES = [CommentsStream]


class Tapjsonplaceholder(Tap):
    """jsonplaceholder tap class."""

    name = "tap-jsonplaceholder"

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""

        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
