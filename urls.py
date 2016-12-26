#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import include, url
from views import misc, landing, geoserver, description, input, output, algorithms, references, batch, qaqc, history, generateReport


# All view functions here must be in '/views/views.py'
urlpatterns = [
    url(r'^api/cts/', include('cts_api.urls')),
    # url(r'^docs/', include('docs.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^api/ubertool/', include('api.urls')),
    url(r'^rest/', include('REST.urls')),
    url(r'^hwbi/', include('models.hwbi.urls')),
    url(r'^ubertool/hwbi/?', include('models.hwbi.urls')),
    url(r'^ubertool/webice/', include('models.webice.urls')),
    # url(r'^eco/test/?$', include('models.test.urls')),
    url(r'^ubertool/login/auth/?$', misc.login_auth),
    url(r'^ubertool/login*', misc.login),
    url(r'^ubertool/ore/', include('models.ore.urls')),
    url(r'^$', landing.ubertool_landing_page),
    url(r'^geoserver/?$', geoserver.test_page),
    url(r'^geoserver/query/(?P<jid>\d{20})$', geoserver.sam_huc_query),
    url(r'^geoserver/sam_done/(?P<jid>\d{20})$', geoserver.sam_done_query),
    url(r'^ubertool/?$', landing.eco_landing_page),
    url(r'^ubertool/(?P<model>.*?)/description/?$', description.description_page),
    url(r'^ubertool/(?P<model>.*?)/input/?$', input.input_page),
    url(r'^ubertool/(?P<model>.*?)/output/?$', output.output_page),
    url(r'^ubertool/(?P<model>.*?)/algorithms/?$', algorithms.algorithm_page),
    url(r'^ubertool/(?P<model>.*?)/references/?$', references.references_page),
    url(r'^ubertool/(?P<model>.*?)/batchinput/?$', batch.batchInputPage),
    url(r'^ubertool/(?P<model>.*?)/batchoutput/?$', batch.batchOutputPage),
    url(r'^ubertool/(?P<model>.*?)/qaqc/(?P<runID>.*?)/?$', qaqc.qaqcRunView),
    url(r'^ubertool/(?P<model>.*?)/qaqc/?$', qaqc.qaqcPage),
    url(r'^ubertool/(?P<model>.*?)/history/?$', history.historyPage),
    url(r'^ubertool/(?P<model>.*?)/history/query?$', history.historyQueryAjax),
    url(r'^ubertool/(?P<model>.*?)/history/revisit?$', history.historyPageRevist),
    # url(r'^ubertool/.*?/history_revisit\.html$', history.historyPageRevist),
    url(r'^ubertool/(?P<model>.*?)/pdf/?$', generateReport.pdfReceiver),
    url(r'^ubertool/(?P<model>.*?)/html/?$', generateReport.htmlReceiver),
    url(r'^ubertool/docs/?$', misc.docs_redirect),
    url(r'^ubertool/api/?$', misc.api_redirect),
    url(r'^ubertool/links/?$', misc.links),
    # url(r'^eco/.*?/przm5_intermediate\.html', przm5_intermediate.przm5IntermediatePage),
    url(r'^ubertool/(?P<model>.*?)/?$', description.description_page),
    url(r'^eco_index\.html$', landing.eco_landing_page),  # Legacy links
    url(r'^(?P<model>.*?)_description\.html$', description.description_page),  # Legacy links
    url(r'^(?P<model>.*?)_input\.html$', input.input_page),  # Legacy links
    url(r'^(?P<model>.*?)_output\.html$', output.output_page),  # Legacy links
    url(r'^(?P<model>.*?)_algorithms\.html$', algorithms.algorithm_page),  # Legacy links
    url(r'^(?P<model>.*?)_references\.html$', references.references_page),  # Legacy links
    url(r'^(?P<model>.*?)_batchinput\.html$', batch.batchInputPage),  # Legacy links
    url(r'^(?P<model>.*?)_batchoutput\.html$', batch.batchOutputPage),  # Legacy links
    url(r'^(?P<model>.*?)_qaqc\.html$', qaqc.qaqcPage),  # Legacy links
    url(r'^(?P<model>.*?)_history\.html$', history.historyPage),  # Legacy links
    # url(r'^ubertool/api/', include('rest_framework_swagger.urls')),
    # url(r'^admin/', include(admin.site.urls)),
]

# 404 Error view (file not found)
handler404 = misc.file_not_found
# 500 Error view (server error)
handler500 = misc.file_not_found
# 403 Error view (forbidden)
handler403 = misc.file_not_found