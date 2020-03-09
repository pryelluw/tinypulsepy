# reference: https://api-docs.tinypulse.com/doc/api

CHEERS = '/v1/cheers'
CHEER = '/v1/cheers/{id}'
CHEER_COMMENTS = '/v1/cheers/{id}/comments'

FILTERS = '/v1/filters'

RESPONSES = '/v1/responses'
OBOARD_RESPONSES = '/v1/onboard/responses'
SURVEY_RESPONSES = '/v1/surveys/{id}/responses'

ORGANIZATIONS = '/v1/organizations/{id}/leaders'

RECEIVERS = '/v1/receivers'
RECEIVER_FILTER = '/v1/receivers/{id}/filters'

SEGMENTS = '/v1/segments'

SUGGESTIONS = '/v1/suggestions'
SUGGESTION_COMMENTS = '/v1/suggestions/{id}/comments'
SUGGESTION_PRIVATE_MESSAGES = '/v1/suggestions/{id}/private_messages'
SURVEY_SUGGESTIONS = '/v1/surveys/{id}/suggestions'

SURVEYS = '/v1/surveys'
SURVEY_STATS = '/v1/surveys/{id}/stats'
SURVEY_SEGMENTS = '/v1/surveys/{id}/segments'
SURVEY_FILTER = '/v1/surveys/{id}/filters'
SURVEY_RESPONSE_COMMENTS = '/v1/surveys/{survey_id}/responses/{response_id}/comments'
SURVEY_RESPONSE_PRIVATE_MESSAGES = '/v1/surveys/{survey_id}/responses/{response_id}/private_messages'
