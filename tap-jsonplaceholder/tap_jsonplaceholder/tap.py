# """jsonplaceholder tap class."""

# from __future__ import annotations

# from typing import List
# from singer_sdk import Tap, Stream
# from singer_sdk import typing as th  # JSON schema typing helpers

# # TODO: Import your custom stream types here:
# # from tap_jsonplaceholder import streams
# from tap_jsonplaceholder.streams import jsonplaceholderStream, CommentsStream

# STREAM_TYPES = [CommentsStream]


# class Tapjsonplaceholder(Tap):
#     """jsonplaceholder tap class."""

#     name = "tap-jsonplaceholder"

#     # TODO: Update this section with the actual config values you expect:
#     config_jsonschema = th.PropertiesList(
#         th.Property(
#             "auth_token",
#             th.StringType,
#             required=True,
#             secret=True,  # Flag config as protected.
#             description="The token to authenticate against the API service",
#         ),
#         th.Property(
#             "project_ids",
#             th.ArrayType(th.StringType),
#             required=True,
#             description="Project IDs to replicate",
#         ),
#         th.Property(
#             "start_date",
#             th.DateTimeType,
#             description="The earliest record date to sync",
#         ),
#         th.Property(
#             "api_url",
#             th.StringType,
#             default="https://api.mysample.com",
#             description="The url for the API service",
#         ),
#     ).to_dict()

#     def discover_streams(self) -> list[Stream]:
#         """Return a list of discovered streams.

#         Returns:
#             A list of discovered streams.
#         """
#         # return [
#         #     streams.GroupsStream(self),
#         #     streams.UsersStream(self),
#         # ]
#         return [stream_class(tap=self) for stream_class in STREAM_TYPES]


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


if __name__ == "__main__":
    Tapjsonplaceholder.cli()
