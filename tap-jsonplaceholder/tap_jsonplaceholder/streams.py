# """Stream type classes for tap-jsonplaceholder."""

# from __future__ import annotations

# import sys
# import typing as t

# from singer_sdk import typing as th  # JSON Schema typing helpers

# from tap_jsonplaceholder.client import jsonplaceholderStream

# if sys.version_info >= (3, 9):
#     import importlib.resources as importlib_resources
# else:
#     import importlib_resources


# # TODO: Delete this is if not using json files for schema definition
# SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"
# # TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
# #       - Copy-paste as many times as needed to create multiple stream types.


# class UsersStream(jsonplaceholderStream):
#     """Define custom stream."""

#     name = "users"
#     path = "/users"
#     primary_keys: t.ClassVar[list[str]] = ["id"]
#     replication_key = None
#     # Optionally, you may also use `schema_filepath` in place of `schema`:
#     # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property(
#             "id",
#             th.StringType,
#             description="The user's system ID",
#         ),
#         th.Property(
#             "age",
#             th.IntegerType,
#             description="The user's age in years",
#         ),
#         th.Property(
#             "email",
#             th.StringType,
#             description="The user's email address",
#         ),
#         th.Property("street", th.StringType),
#         th.Property("city", th.StringType),
#         th.Property(
#             "state",
#             th.StringType,
#             description="State name in ISO 3166-2 format",
#         ),
#         th.Property("zip", th.StringType),
#     ).to_dict()


# class GroupsStream(jsonplaceholderStream):
#     """Define custom stream."""

#     name = "groups"
#     path = "/groups"
#     primary_keys: t.ClassVar[list[str]] = ["id"]
#     replication_key = "modified"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property("id", th.StringType),
#         th.Property("modified", th.DateTimeType),
#     ).to_dict()


# class CommentsStream(jsonplaceholderStream):
#     primary_keys = ["id"]
#     path = "/comments"
#     name = "comments"
#     schema = th.PropertiesList(
#         th.Property("postId", th.IntegerType),
#         th.Property("id", th.IntegerType),
#         th.Property("name", th.StringType),
#         th.Property("email", th.StringType),
#         th.Property("body", th.StringType),
#     ).to_dict()

"""Stream type classes for tap-jsonplaceholder."""

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_jsonplaceholder.client import jsonplaceholderStream


class CommentsStream(jsonplaceholderStream):
    primary_keys = ["id"]
    path = "/comments"
    name = "comments"
    schema = th.PropertiesList(
        th.Property("postId", th.IntegerType),
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("email", th.StringType),
        th.Property("body", th.StringType),
    ).to_dict()
