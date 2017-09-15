import googleplay_pb2
import time

# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "en_US"
ANDROID_ID      = "320d104c4dc6eaa4"
GOOGLE_PUBKEY   = "AAAAgMom/1a/v0lblO2Ubrt60J2gcuXSljGFQXgcyZWveWLEwo6prwgi3iJIZdodyhKZQrNWp5nKJ3srRXcUW+F1BD3baEVGcmEgqaLZUNBjm057pKRI16kB0YppeGx5qIQ5QjKzsR8ETQbKLNWgRY0QRNVz34kMJR3P/LgHax/6rmf5AAAAAwEAAQ=="
GOOGLE_LOGIN    = ""
GOOGLE_PASSWORD = ""
AUTH_TOKEN      = ""

# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

# All the following data is taken from play-store-api
# https://github.com/yeriomin/play-store-api/blob/master/src/main/resources/device-bacon.properties
# The device used as a reference is a OnePlus One (bacon)

LIB_LIST        = "com.qualcomm.qcnvitems,com.android.location.provider,com.android.future.usb.accessory,android.ext.shared,javax.obex,android.ext.services,com.dsi.ant.antradio_library,com.qualcomm.qcrilhook,android.test.runner,org.apache.http.legacy,com.android.nfc_extras,com.android.media.remotedisplay,com.android.mediadrm.signer"
FEATURE_LIST    = "android.hardware.sensor.proximity,android.hardware.sensor.accelerometer,android.hardware.faketouch,org.cyanogenmod.appsuggest,android.hardware.usb.accessory,android.hardware.telephony.cdma,android.software.backup,android.hardware.touchscreen,android.hardware.touchscreen.multitouch,android.software.print,android.hardware.consumerir,org.cyanogenmod.partner,org.cyanogenmod.telephony,android.software.voice_recognizers,android.hardware.fingerprint,android.hardware.sensor.gyroscope"
",android.hardware.audio.low_latency,android.hardware.opengles.aep,android.hardware.bluetooth,android.hardware.camera.autofocus,com.google.android.feature.GOOGLE_BUILD,android.hardware.telephony.gsm,android.software.sip.voip,org.cyanogenmod.profiles,android.hardware.usb.host,com.cyanogenmod.android,android.hardware.audio.output,android.hardware.camera.flash,android.hardware.camera.front,android.hardware.sensor.hifi_sensors,android.hardware.screen.portrait,android.hardware.nfc"
",com.nxp.mifare,android.hardware.sensor.stepdetector,org.cyanogenmod.audio,org.cyanogenmod.theme,android.software.home_screen,android.hardware.microphone,org.cyanogenmod.statusbar,android.hardware.bluetooth_le,android.hardware.sensor.compass,android.hardware.touchscreen.multitouch.jazzhand,android.hardware.sensor.barometer,android.software.app_widgets,android.software.input_methods,android.hardware.sensor.light,android.software.device_admin,android.hardware.camera"
",org.cyanogenmod.hardware,android.hardware.screen.landscape,org.cyanogenmod.weather,org.cyanogenmod.performance,android.software.managed_users,android.software.webview,android.hardware.sensor.stepcounter,android.hardware.camera.capability.manual_post_processing,org.cyanogenmod.livedisplay,android.hardware.camera.any,android.hardware.camera.capability.raw,android.software.connectionservice,android.hardware.touchscreen.multitouch.distinct,android.hardware.location.network"
",android.software.sip,android.hardware.camera.capability.manual_sensor,android.hardware.camera.level.full,android.hardware.wifi.direct,android.software.live_wallpaper,com.google.android.feature.GOOGLE_EXPERIENCE,com.google.android.feature.EXCHANGE_6_2,org.cyanogenmod.theme.v1,org.cyanogenmod.livelockscreen,android.hardware.location.gps,android.software.midi,android.hardware.nfc.hce,android.hardware.wifi,android.hardware.location,android.hardware.telephony"
LOCALE_LIST     = "hi,so_ET,ro_MD,in,sn_ZW,sw_UG,es_BO,dyo,ru_KZ,en_JE,zu,en_JM,pt_BR,en_MS,ar_SD,en_ZM,es_PA,en_GG,es_SV,en_SE,es,rof,fr_SC,fr_GA,en_CM,ta,en_SX,fr_MC,fy,to,fr_RW,en_SD,qu,en_KE,rw_RW,gv_IM,sv_FI,cgg,pt_GW,fr_CF,sv_SE,dje,en_SS,ar_DZ,si,es_UY,ar_SA,tr_TR,dua,fr_BL,nb_SJ,fr_CA,ff,es_PE,om,en_FK,cs_CZ,zu_ZA,sl_SI,es_NI,en_GY,fr_ML,fr_MF,nmg,fo_DK,en_LR,el_CY,nus,mt,en_NU,en_UG,ta_MY,pt_ST,ha_NE,ca_FR,ru,es_IC,ar_KW,it_IT,en_GI,ji,hr,ka_GE,pt_PT,nl,en_TV,ru_RU,pa,mgh,es_ES,km,ee_TG"
",ca_AD,twq,ar_YE,eo,ne,as_IN,es_GT,vi_VN,de_CH,ig_NG,or_IN,mua,pl_PL,lv,fr_DZ,lb,hr_HR,haw,sw_KE,shi,mn,om_ET,fr_LU,es_PR,lo_LA,es_HN,kl_GL,bo_IN,et_EE,en_ZA,fr_TG,br_FR,yo_NG,tr_CY,sr,bem,fr_PF,ti_ET,hu,mk,de_LI,so_SO,nb_NO,luo,en_ZW,sk_SK,ksh,sk,nyn,fa,zgh,fr_HT,en_CY,uz,rm,en_MH,sn,to_TO,te,sq_MK,ha_GH,ta_IN,en_MW,da,en_BS,ms_SG,ps_AF,lt_LT,br,it_CH,fr_NE,en_LC,bm_ML,kk_KZ,qu_BO,tr,nl_SR,ln,sw,luy,en,fo,en_GD,asa,lag,fr_GQ,fr,fr_GN,dz,ar_SO,dz_BT,ca,es_CL,rn_BI,sq_XK,en_CC,en_SI"
",el_GR,yo_BJ,vi,my,de_LU,mk_MK,ak_GH,fr_GF,en_PK,my_MM,fr_CG,cy,es_PH,en_IN,ksf,en_LS,fy_NL,ce,ff_MR,af_ZA,fa_IR,bn_BD,vun,ks,bg,sq_AL,fr_BF,rw,af_NA,dsb,qu_PE,en_DM,ar_TN,nd,en_UM,en_FM,en_NR,ro,uk,se_SE,ln_CF,pt_MZ,am_ET,kl,pt,ta_SG,th,se_NO,ff_GN,ky,en_NG,ur_PK,af,en_DE,so,sah,fr_SN,ar_EH,vai,gu_IN,en_WS,es_EA,ms,fr_MG,th_TH,fr_RE,ru_BY,nl_SX,lv_LV,ki_KE,fr_CI,en_BB,ja,kde,am,nl_BQ,bo_CN,ga_IE,sl,bn_IN,mer,en_SZ,fr_CM,dav,ti_ER,da_GL,kw_GB,ga,mfe,it,it_SM,fo_FO,en_BW,en_SG,en_KN"
",cs,chr,km_KH,en_SC,mr_IN,el,en_PN,mg_MG,ru_KG,en_PW,en_SB,fur,en_BZ,ka,bm,de_DE,te_IN,ml_IN,hy,sw_TZ,kw,kn,ru_UA,ln_CD,et,fr_CH,en_DG,bn,ps,qu_EC,lt,ii_CN,en_FJ,eu,en_TC,ksb,pt_CV,gl_ES,en_VU,en_MP,ee,ar_PS,wae,nl_BE,xog,is,fr_PM,saq,iw_IL,om_KE,en_FI,nn_NO,pt_MO,mgo,en_US,fr_BE,ar,gd,kok,de,kln,kam,mt_MT,be,ce_RU,en_BE,fr_SY,es_MX,sv_AX,agq,sq,hr_BA,tzm,de_AT,os_RU,es_DO,en_BI,mg,ar_SY,yav,ks_IN,ro_RO,lu_CD,en_PG,jgo,is_IS,es_CU,ff_CM,en_VG,az,en_GU,fr_MR,ug_CN,in_ID,en_AU,nl_CW"
",ru_MD,naq,gd_GB,en_CK,ml,ja_JP,sw_CD,uk_UA,ta_LK,pl,es_VE,da_DK,be_BY,fa_AF,pt_AO,fr_MQ,bs,mas,ar_QA,en_IO,en_SH,en_NL,es_GQ,lg,hu_HU,fr_BJ,en_MO,brx,fr_WF,ar_OM,ca_ES,en_GB,ug,ha,en_NA,en_NF,sv,as,ig,en_KI,en_CX,en_TO,sbp,bo,ne_NP,bg_BG,jmc,en_GM,ar_JO,en_HK,ar_IQ,fr_DJ,fr_GP,lkt,kn_IN,ha_NG,en_IL,en_KY,en_TT,fil,fr_BI,sg,hsb,ca_IT,teo,fr_TN,en_AS,kk,guz,fr_VU,mr,es_EC,en_TZ,ko_KR,ar_MA,ar_LB,fr_CD,en_DK,es_CO,ur_IN,rwk,es_PY,ms_MY,cy_GB,en_PH,seh,ar_BH,en_TK,en_RW,eu_ES,ki,fr_TD"
",smn,ses,so_KE,es_CR,en_MY,en_AI,lo,en_MG,en_PR,gsw,en_VI,en_BM,se,en_IE,en_SL,khq,en_CH,ee_GH,ko,lb_LU,en_AT,nn,ar_ER,lrc,ar_TD,ar_MR,fr_YT,en_GH,en_MU,si_LK,gv,ky_KG,nl_NL,rm_CH,ar_IL,ti,iw,hy_AM,se_FI,pt_TL,en_AG,or,bez,ff_SN,en_IM,fr_MA,en_MT,nd_ZW,fi_FI,en_NZ,de_BE,fr_KM,bas,ak,nl_AW,ar_AE,kab,ar_EG,ur,es_AR,ar_DJ,ar_KM,kkj,fi,lu,fr_FR,ebu,os,ne_IN,ln_AO,gu,zh,os_GE,sg_CF,mn_MN,gl,lg_UG,ko_KP,rn,mzn,es_US,hi_IN,ar_LY,ms_BN,fr_NC,so_DJ,ii,en_ER,ar_SS,kea,ln_CG,fr_MU"
",nb,yo,nnh,en_VC,ewo,en_CA"
GL_EXTENSIONS   = "GL_AMD_compressed_ATC_texture,GL_AMD_performance_monitor,GL_ANDROID_extension_pack_es31a,GL_APPLE_texture_2D_limited_npot,GL_ARB_vertex_buffer_object,GL_ARM_shader_framebuffer_fetch_depth_stencil,GL_EXT_YUV_target,GL_EXT_blit_framebuffer_params,GL_EXT_buffer_storage,GL_EXT_color_buffer_float,GL_EXT_color_buffer_half_float,GL_EXT_copy_image,GL_EXT_debug_label,GL_EXT_debug_marker,GL_EXT_discard_framebuffer,GL_EXT_disjoint_timer_query,GL_EXT_draw_buffers_indexed,GL_EXT_geometry_shader"
",GL_EXT_gpu_shader5,GL_EXT_multisampled_render_to_texture,GL_EXT_primitive_bounding_box,GL_EXT_robustness,GL_EXT_sRGB,GL_EXT_sRGB_write_control,GL_EXT_shader_framebuffer_fetch,GL_EXT_shader_io_blocks,GL_EXT_tessellation_shader,GL_EXT_texture_border_clamp,GL_EXT_texture_buffer,GL_EXT_texture_cube_map_array,GL_EXT_texture_filter_anisotropic,GL_EXT_texture_format_BGRA8888,GL_EXT_texture_norm16,GL_EXT_texture_sRGB_R8,GL_EXT_texture_sRGB_decode,GL_EXT_texture_type_2_10_10_10_REV"
",GL_KHR_blend_equation_advanced,GL_KHR_blend_equation_advanced_coherent,GL_KHR_debug,GL_KHR_no_error,GL_KHR_texture_compression_astc_hdr,GL_KHR_texture_compression_astc_ldr,GL_OES_EGL_image,GL_OES_EGL_image_external,GL_OES_EGL_sync,GL_OES_blend_equation_separate,GL_OES_blend_func_separate,GL_OES_blend_subtract,GL_OES_compressed_ETC1_RGB8_texture,GL_OES_compressed_paletted_texture,GL_OES_depth24,GL_OES_depth_texture,GL_OES_depth_texture_cube_map,GL_OES_draw_texture"
",GL_OES_element_index_uint,GL_OES_framebuffer_object,GL_OES_get_program_binary,GL_OES_matrix_palette,GL_OES_packed_depth_stencil,GL_OES_point_size_array,GL_OES_point_sprite,GL_OES_read_format,GL_OES_rgb8_rgba8,GL_OES_sample_shading,GL_OES_sample_variables,GL_OES_shader_image_atomic,GL_OES_shader_multisample_interpolation,GL_OES_standard_derivatives,GL_OES_stencil_wrap,GL_OES_surfaceless_context,GL_OES_texture_3D,GL_OES_texture_compression_astc,GL_OES_texture_cube_map"
",GL_OES_texture_env_crossbar,GL_OES_texture_float,GL_OES_texture_float_linear,GL_OES_texture_half_float,GL_OES_texture_half_float_linear,GL_OES_texture_mirrored_repeat,GL_OES_texture_npot,GL_OES_texture_stencil8,GL_OES_texture_storage_multisample_2d_array,GL_OES_vertex_array_object,GL_OES_vertex_half_float,GL_OVR_multiview,GL_OVR_multiview2,GL_OVR_multiview_multisampled_render_to_texture,GL_QCOM_alpha_test,GL_QCOM_extended_get,GL_QCOM_tiled_rendering,GL_EXT_multi_draw_arrays"
",GL_EXT_shader_texture_lod,GL_IMG_multisampled_render_to_texture,GL_IMG_program_binary,GL_IMG_read_format,GL_IMG_shader_binary,GL_IMG_texture_compression_pvrtc,GL_IMG_texture_format_BGRA8888,GL_IMG_texture_npot,GL_IMG_vertex_array_object,GL_OES_byte_coordinates,GL_OES_extended_matrix_palette,GL_OES_fixed_point,GL_OES_fragment_precision_high,GL_OES_mapbuffer,GL_OES_matrix_get,GL_OES_query_matrix,GL_OES_required_internalformat,GL_OES_single_precision,GL_OES_stencil8"


libList = LIB_LIST.split(",")
featureList = FEATURE_LIST.split(",")
localeList = LOCALE_LIST.split(",")
glList = GL_EXTENSIONS.split(",")
currentTime = int(time.time())

deviceConfig = googleplay_pb2.DeviceConfigurationProto()
deviceConfig.touchScreen = 3
deviceConfig.keyboard = 1
deviceConfig.navigation = 1
deviceConfig.screenLayout = 2
deviceConfig.hasHardKeyboard = False
deviceConfig.hasFiveWayNavigation = False
deviceConfig.screenDensity = 420
deviceConfig.screenWidth = 1080
deviceConfig.screenHeight = 1920
deviceConfig.nativePlatform.append("armeabi-v7a")
deviceConfig.nativePlatform.append("armeabi")
for x in libList:
    deviceConfig.systemSharedLibrary.append(x)
for x in featureList:
    deviceConfig.systemAvailableFeature.append(x)
for x in localeList:
    deviceConfig.systemSupportedLocale.append(x)
    deviceConfig.glEsVersion = 131072
for x in glList:
    deviceConfig.glExtension.append(x)

androidBuild = googleplay_pb2.AndroidBuildProto()
androidBuild.id = 'oneplus/bacon/A0001:6.0.1/MHC19Q/ZNH2KAS1KN:user/release-keys'
androidBuild.product = 'bacon'
androidBuild.carrier = 'oneplus'
androidBuild.radio = '.4.0.1.c7-00013-M8974AAAAANAZM-1'
androidBuild.bootloader = 'unknown'
androidBuild.device = 'A0001'
androidBuild.sdkVersion = 25
androidBuild.model = 'A0001'
androidBuild.manufacturer = 'OnePlus'
androidBuild.buildProduct = 'bacon'
androidBuild.client = 'android-google'
androidBuild.otaInstalled = False
androidBuild.timestamp = currentTime
androidBuild.googleServices = 10548448

androidCheckin = googleplay_pb2.AndroidCheckinProto()
androidCheckin.build.CopyFrom(androidBuild)
androidCheckin.lastCheckinMsec = 0
androidCheckin.cellOperator = '310260'
androidCheckin.simOperator = '310260'
androidCheckin.roaming = 'mobile-notroaming'
androidCheckin.userNumber = 0