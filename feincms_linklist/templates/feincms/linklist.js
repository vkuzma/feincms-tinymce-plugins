
var tinyMCELinkList = new Array(
    {% for page in pages %}["{{ page.depth_indicator }} {{ page }}", "{{page.get_absolute_url }}?p={{ page.id }}"]{% if not forloop.last %},{% endif %}
    {% endfor %}
);
