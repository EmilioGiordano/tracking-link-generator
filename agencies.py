AGENCIES = {
    'dhl_es': {
        'aliases': ['dhl españa', 'dhl es', 'dhl'],
        'url': 'https://clientesparcel.dhl.es/LiveTrackingN/ModificarEnvio/'
    },
    # 'dhl_pt': {
    #     'aliases': ['dhl portugal', 'dhl pt'],
    #     'url': 'https://clientesparcel.dhl.es/LiveTracking/ModificarMeuEnvio/'  # Portugués
    # },
    # 'dhl_fr': {
    #     'aliases': ['dhl francia', 'dhl fr'],
    #     'url': 'https://www.dhl.com/fr-fr/home/tracking/tracking-ecommerce.html?submit=1&tracking-id='  # Francés
    # },
    'correos_express': {
        'aliases': ['correos', 'correosexpress', 'c. express'],
        'url': 'https://s.correosexpress.com/SeguimientoSinCP/search?n='
    },
    'tnt_fr': {
        'aliases': ['tnt francia', 'tnt fr'],
        'url': 'https://www.tnt.com/express/fr_fr/site/outils-expedition/suivi.html?searchType=con&cons='
    },
    # GLS España con CP e idioma
    # 'gls_es': {
    #     'aliases': ['gls españa', 'gls es'],
    #     'url': 'https://mygls.gls-spain.es/e/REFERENCIA/CP/es'
    # },
    'gls_fr': {
        'aliases': ['gls francia', 'gls fr'],
        'url': 'https://gls-group.com/FR/fr/suivi-colis/?match='
    },
    'gls_ie': {
        'aliases': ['gls irlanda', 'gls ie'],
        'url': 'https://gls-group.com/IE/en/parcel-tracking/?match='
    },
    'gls_int': {
        'aliases': ['gls internacional', 'gls international'],
        'url': 'https://www.gls-spain.es/es/recibir-paquetes/seguimiento-envio/?match={}&international=1'
    },
    'seur': {
        'aliases': ['seur'],
        'url': 'https://seur.com/miseur/mis-envios/detalle?tracking='
    },
    # 'seur_idioma': {
    #     'aliases': ['seur idioma'],
    #     'url': 'https://www.seur.com/livetracking/?segOnlineIdentificador=REFERENCIA&segOnlineIdioma=es'  # Cambiar idioma
    # },
    'transaher': {
        'aliases': ['transaher'],
        'url': 'https://clientes.transaher.es/webclient/tracking/-5,0,'
    },
    'raben': {
        'aliases': ['raben'],
        'url': 'https://www.raben-group.com/'  # Se concatena referencia
    },
    'envialia': {
        'aliases': ['envialia'],
        'url': 'https://www.aftership.com/es/track/envialia/'
    },
    'viaxpress': {
        'aliases': ['viaxpress'],
        'url': 'https://www.aftership.com/es/track/viaxpress/'
    },
    'redur_ref': {
        'aliases': ['redur referencia'],
        'url': 'https://www.aftership.com/es/track/redur-es/'
    },
    'redur_exp': {
        'aliases': ['redur expedicion', 'redur'],
        'url': 'https://redur.es/track-trace/?cliExt=&idioma=es&buscarPor=EXPEDICION&valor='
    },
    'cbl': {
        'aliases': ['cbl', 'cbl logistica'],
        'url': 'https://clientes.cbl-logistica.com/public/consultaenvio.aspx?id='
    },
    'ctt': {
        'aliases': ['ctt', 'ctt express'],
        'url': 'https://www.cttexpress.com/localizador-de-envios/?sc='
    },
    'mrw': {
        'aliases': ['mrw'],
        'url': 'https://www.mrw.es/seguimiento_envios/MRW_resultados_consultas.asp?modo=nacional&envio='
    },
    # 'dachser': {
    #     'aliases': ['dachser'],
    #     'url': 'https://elogistics.dachser.com/shp2s/?search=REFERENCIA&javalocale=es_ES'  # Cambiar idioma
    # },
    'tdn': {
        'aliases': ['tdn'],
        'url': 'http://tracking.tdnonline.com/consulta_expediciones/tracking?REFERENCIA='  # Solo expediciones
    },
    'xpo': {
        'aliases': ['xpo'],
        'url': 'https://xpoconnecteu.xpo.com/track/'
    },
    # 'ontime_cp': {
    #     'aliases': ['ontime cp'],
    #     'url': 'https://core.ontime.es/ords/r/ontime/portalcliente999/url-seguimiento-consignatario?p_param1=NUMERO_DE_SEGUIMIENTO&p_param2=CODIGO_POSTAL'
    # },
    'ontime': {
        'aliases': ['ontime'],
        'url': 'https://ontimegts.alertran.net/gts/pub/locNumSeguimiento.seam?localizador='
    },
    'dpd_es': {
        'aliases': ['dpd españa', 'dpd es', 'dpd'],
        'url': 'https://tracking.dpd.de/status/es_ES/parcel/'
    },
    'dpd_fr': {
        'aliases': ['dpd francia', 'dpd fr'],
        'url': 'https://tracking.dpd.de/status/fr_FR/parcel/'
    },
    'dpd_de': {
        'aliases': ['dpd alemania', 'dpd de'],
        'url': 'https://tracking.dpd.de/status/de_de/parcel/'
    },
    'ups_es': {
        'aliases': ['ups españa', 'ups es'],
        'url': 'https://www.ups.com/track?loc=es_ES&requester=QUIC&tracknum={}/trackdetails'
    },
    'ups_fr': {
        'aliases': ['ups francia', 'ups fr'],
        'url': 'https://www.ups.com/track?loc=FR_FR&tracknum={}&requester=WT/trackdetails'
    },
    'ups_ie': {
        'aliases': ['ups irlanda', 'ups ie'],
        'url': 'https://www.ups.com/track?loc=en_IE&requester=QUIC&tracknum={}/trackdetails'
    },
    'ups_it': {
        'aliases': ['ups italia', 'ups it'],
        'url': 'https://www.ups.com/track?loc=it_IT&requester=QUIC&tracknum={}/trackdetails'
    },
    'laposte': {
        'aliases': ['laposte', 'la poste'],
        'url': 'https://www.laposte.fr/outils/track-a-parcel?code='
    },
    'impackta': {
        'aliases': ['impackta'],
        'url': 'https://seguimiento.impackta.com/index.php?albaran='
    },
    'dbschenker': {
        'aliases': ['dbschenker', 'db schenker'],
        'url': 'https://www.dbschenker.com/app/tracking-public/?refNumber='
    },
    'dbschenker_fr': {
        'aliases': ['dbschenker francia', 'db schenker fr'],
        'url': 'https://eschenker.dbschenker.com/app/tracking-public/?refNumber={}&language_region=fr'  # Francés
    },
    'suus': {
        'aliases': ['suus'],
        'url': 'https://portal.suus.com/order-details/'
    },
    # 'gw_cp': {
    #     'aliases': ['gw cp'],
    #     'url': 'https://my.gw-world.com/trackntrace/-/search/CP/REFERENCIA'
    # },
    'kn': {
        'aliases': ['kuehne nagel', 'kn'],
        'url': 'https://mykn.kuehne-nagel.com/public-tracking/shipments/{}?query=REFERENCIA'
    },
    'fedex': {
        'aliases': ['fedex'],
        'url': 'https://www.fedex.com/wtrk/track/?action=track&tracknumbers={}&locale=es_ES'  # Cambiar idioma
    },
    'packeta': {
        'aliases': ['packeta'],
        'url': 'https://tracking.packeta.com/es_ES/{}'  # Cambiar idioma
    },
    'zeleris': {
        'aliases': ['zeleris'],
        'url': 'https://www.zeleris.com/seguimiento-de-envios/?tracking_number='
    },
    'aftership_fedex': {
        'aliases': ['aftership fedex'],
        'url': 'https://www.aftership.com/de/track/fedex/'  # Cambiar idioma y agencia
    },
    'mbe_es': {
        'aliases': ['mbe españa', 'mbe es'],
        'url': 'https://www.mbe.es/es/tracking?c='
    },
    'mbe_fr': {
        'aliases': ['mbe francia', 'mbe fr'],
        'url': 'https://www.mbefrance.fr/fr/suivi?c='
    },
    'ntl_trans': {
        'aliases': ['ntl trans'],
        'url': 'http://red.ntl-trans.com/B2B/trackorder.asp?OTSREF=EHAI0169&TIEID=REFERENCIA'  # Requiere referencia
    },
} 