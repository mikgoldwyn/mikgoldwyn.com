from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'api', 'config.api_urls', name='api'),
    host(r'empotech', 'config.empotech_urls', name='empotech'),
    host(r'', 'config.default_urls', name='default'),
)
