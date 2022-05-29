from stand_utils import config_parser
from sbis_root import sbis

config = config_parser.Config()
_session_id = sbis.САП.АутентифицироватьсяПоЛогину(config.auth_url, config.login, config.password)
sbis.Session.Set(0, _session_id)
sbis.SetCurrentSearchPath(config.schema_name)
print("You have logged in successfully")
sbis.Session.Set(sbis.WebServerContextKey.icsREQUEST_NUMBER, 'test_session_from_console')

def _convert_recursive(q):
    if type(q) is sbis.Record:
        return dict((k, _convert_recursive(v)) for (k, v) in q.as_dict().items())
    if type(q) is sbis.RecordSet:
        return [_convert_recursive(x) for x in list(q)]
    return q

# Convert record/recordset to readable view
def convert_printable(q):
    return _convert_recursive(q)