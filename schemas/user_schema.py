from voluptuous import  Required, Schema, PREVENT_EXTRA


create_user = Schema({
    Required("name"): str,
    Required("job"): str,
    Required("id"): str,
    Required("createdAt"): str
}, extra=PREVENT_EXTRA)

update_user = Schema({
    Required("name"): str,
    Required("job"): str,
    Required("updatedAt"): str
}, extra=PREVENT_EXTRA)

data_schema = Schema({
    Required("id"): int,
    Required("email"): str,
    Required("first_name"): str,
    Required("last_name"): str,
    Required("avatar"): str
}, extra=PREVENT_EXTRA)

support_schema = Schema({
    Required("url"): str,
    Required("text"): str
}, extra=PREVENT_EXTRA)

get_user = Schema({
    Required("data"): data_schema,
    Required("support"): support_schema
}, extra=PREVENT_EXTRA)
