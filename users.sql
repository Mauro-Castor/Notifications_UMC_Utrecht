SELECT
DISTINCT(JSON_UNQUOTE(JSON_EXTRACT(CAST(FROM_BASE64(additional_info) AS CHAR), '$."Invited user ID"'))) AS user_id,
JSON_UNQUOTE(JSON_EXTRACT(CAST(FROM_BASE64(additional_info) AS CHAR), '$."Invited user email address"')) AS user_email
FROM
`crf_event_log`
WHERE
event_type = 'user_invited_to_study'
