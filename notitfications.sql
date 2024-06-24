SELECT
event_type,
recipients,
notification_type,
institute_filter,
message_template,
CASE WHEN f.field_variable_name IS NOT NULL THEN f.field_variable_name ELSE r.report_name END AS entity_filter,
CASE WHEN f.field_variable_name IS NOT NULL THEN 'field' ELSE 'report' END AS entity_type
FROM
`notification_configurations` nc
LEFT JOIN `crf_fields` f ON f.field_id = nc.field_filter
LEFT JOIN `crf_reports` r ON r.report_id = nc.report_filter
