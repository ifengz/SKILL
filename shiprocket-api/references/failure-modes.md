# Failure Modes

Block completion when:

- the main Shiprocket panel account is used as the API credential contract
- API User credential, JWT, server URL, or password is present as a real value
- local order id, Shiprocket order id, shipment id, and AWB are collapsed into one field
- write flows run before read/detail/serviceability smoke tests
- pickup location is modeled as only an internal warehouse id
- cancel/reassign after AWB or pickup is promised without verified public API support
- backend and frontend disagree on which status blocks a write
- token refresh/expiry behavior is omitted
