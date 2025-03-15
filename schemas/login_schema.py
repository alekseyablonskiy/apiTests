from voluptuous import Schema, Required, PREVENT_EXTRA


login_success = Schema({
    Required("token"): str
}, extra=PREVENT_EXTRA)

login_unsuccess = Schema({
    Required("error"): str
}, extra=PREVENT_EXTRA)