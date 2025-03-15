from voluptuous import Schema, Required, PREVENT_EXTRA


register_success = Schema({
    Required("id"): int,
    Required("token"): str
}, extra=PREVENT_EXTRA)

register_unsuccess = Schema({
    Required("error"): str
}, extra=PREVENT_EXTRA)