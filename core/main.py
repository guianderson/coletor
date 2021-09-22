import psycopg2
import pandas as pd

# Conexão com Banco de Dados
con = psycopg2.connect(host='localhost', database='alejandro', user='postgres', password='postgres')
cur = con.cursor()

# Identificando e lendo arquivo que deseja inserir no Banco
data = pd.read_csv('branch-1__3-rrhh.csv', encoding='utf8')
values = pd.DataFrame().append(data)

# Renomeando Colunas com nomes inválidos
values = values.rename({'26_Nmero_de_personal': 'Nmero_de_personal_26'}, axis=1)
values = values.rename({'25_Nmero_de_personal': 'Nmero_de_personal_25'}, axis=1)
values = values.rename({'24_rea_laboral': 'rea_laboral_24'}, axis=1)

# Identificando e lendo arquivo que deseja inserir no Banco
data2 = pd.read_csv('form-1__industrias.csv', encoding='utf8')
values2 = pd.DataFrame().append(data2)

# Renomeando Colunas com nomes inválidos
values2 = values2.rename({'2_Razn_Social'               : 'Razn_Social_2'           }, axis=1)
values2 = values2.rename({'3_Razn_Social_opcion'        : 'Razn_Social_opcion_3'    }, axis=1)
values2 = values2.rename({'4_Situacin'                  : 'Situaci_4'               }, axis=1)
values2 = values2.rename({'5_CUITCUIL'                  : 'CUITCUIL_5'              }, axis=1)
values2 = values2.rename({'6_Correo_electrnico'         : 'Correo_electrnico_6'     }, axis=1)
values2 = values2.rename({'7_Propietario'               : 'Propietario_7'           }, axis=1)
values2 = values2.rename({'8_Telfono'                   : 'Telfono_8'               }, axis=1)
values2 = values2.rename({'10_Superficie_total_'        : 'Superficie_total_10'     }, axis=1)
values2 = values2.rename({'11_Superficie_cubier'        : 'Superficie_cubier_11'    }, axis=1)
values2 = values2.rename({'12_Potencia_total_in'        : 'Potencia_total_in_12'    }, axis=1)
values2 = values2.rename({'13_Consumo_de_energa'        : 'Consumo_de_energa_13'    }, axis=1)
values2 = values2.rename({'14_Capacidad_total_i'        : 'Capacidad_total_i_14'    }, axis=1)
values2 = values2.rename({'15_Capacidad_total_i'        : 'Capacidad_total_i_15'    }, axis=1)
values2 = values2.rename({'16_Produccin_anual_a'        : 'Produccin_anual_a_16'    }, axis=1)
values2 = values2.rename({'17_Produccin_anual_a'        : 'Produccin_anual_a_17'    }, axis=1)
values2 = values2.rename({'18_Produccin_anual_u'        : 'Produccin_anual_u_18'    }, axis=1)
values2 = values2.rename({'22_Mesao'                    : 'Mesao_22'                }, axis=1)
values2 = values2.rename({'21_Dasmes'                   : 'Dasmes_21'               }, axis=1)
values2 = values2.rename({'19_Nmero_de_turnosda'        : 'Nmero_de_turnosda_19'    }, axis=1)
values2 = values2.rename({'20_Horasturno'               : 'Horasturno_20'           }, axis=1)
values2 = values2.rename({'23_3__RRHH'                  : 'RRHH_23'                 }, axis=1)
values2 = values2.rename({'28_4__LINEA_DE_ASERR'        : 'LINEA_DE_ASERR_28'       }, axis=1)
values2 = values2.rename({'37_5__LINEA_DE_ASERR'        : 'LINEA_DE_ASERR_37_5'     }, axis=1)
values2 = values2.rename({'50_7__LINEA_DE_COMPE'        : 'LINEA_DE_COMPE_50_7'     }, axis=1)
values2 = values2.rename({'35_4_a__LINEA_DE_REM'        : 'a__LINEA_DE_REM_35_4'    }, axis=1)
values2 = values2.rename({'46_Bao_antimanchas'          : 'Bao_antimanchas_46'      }, axis=1)
values2 = values2.rename({'47_Impregnado'               : 'Impregnado_47'           }, axis=1)
values2 = values2.rename({'58_Volumen_impregnad'        : 'Volumen_impregnad_58'    }, axis=1)
values2 = values2.rename({'59_Capacidad_total_d'        : 'Capacidad_total_d_59'    }, axis=1)
values2 = values2.rename({'81_Porcentaje_propio'        : 'Porcentaje_propio_81'    }, axis=1)
values2 = values2.rename({'62_Tienen_CATEM'             : 'Tienen_CATEM_62'         }, axis=1)
values2 = values2.rename({'65_Tipo_de_secado'           : 'Tipo_de_secado_65'       }, axis=1)
values2 = values2.rename({'66_Porcentaje_de_sec'        : 'Porcentaje_de_sec_66'    }, axis=1)
values2 = values2.rename({'63_Capacidad_instala'        : 'Capacidad_instala_63'    }, axis=1)
values2 = values2.rename({'64_Volumen_secado_mm'        : 'Volumen_secado_mm_64'    }, axis=1)
values2 = values2.rename({'63_Tiene_deficiencia'        : 'Tiene_deficiencia_63'    }, axis=1)
values2 = values2.rename({'62_Tiene_intensin_de'        : 'Tiene_intensin_de_62'    }, axis=1)
values2 = values2.rename({'75_Tipo_de_chip'             : 'Tipo_de_chip_75'         }, axis=1)
values2 = values2.rename({'76_Toneladas_anuales'        : 'Toneladas_anuales_76'    }, axis=1)
values2 = values2.rename({'77_Destino'                  : 'Destino_77'              }, axis=1)
values2 = values2.rename({'34_5__SECADO'                : 'SECADO_34_5'             }, axis=1)
values2 = values2.rename({'81_13__AFILADO'              : 'AFILADO_81_13'           }, axis=1)
values2 = values2.rename({'81_Potencia_total_de'        : 'Potencia_total_de_81'    }, axis=1)
values2 = values2.rename({'89_Tipo_de_maquina'          : 'Tipo_de_maquina_89'      }, axis=1)
values2 = values2.rename({'93_Otra_aclarar'             : 'Otra_aclarar_93'         }, axis=1)
values2 = values2.rename({'88_Cantidad'                 : 'Cantidad_88'             }, axis=1)
values2 = values2.rename({'91_Ao_de_compra'             : 'Ao_de_compra_91'         }, axis=1)
values2 = values2.rename({'51_Cuenta_con_EPP'           : 'Cuenta_con_EPP_51'       }, axis=1)
values2 = values2.rename({'52_Cuenta_con_preven'        : 'Cuenta_con_preven_52'    }, axis=1)
values2 = values2.rename({'53_Tiene_ART'                : 'Tiene_ART_53'            }, axis=1)
values2 = values2.rename({'54_Elementos_anti_in'        : 'Elementos_anti_in_54'    }, axis=1)
values2 = values2.rename({'93_Red_antiincendio'         : 'Red_antiincendio_93'     }, axis=1)
values2 = values2.rename({'55_Observaciones'            : 'Observaciones_55'        }, axis=1)
values2 = values2.rename({'56_8_MATERIA_PRIMA_p'        : 'MATERIA_PRIMA_p_56_8'    }, axis=1)
values2 = values2.rename({'64_9_PRODUCCIN_prome'        : 'PRODUCCIN_prome_64_9'    }, axis=1)
values2 = values2.rename({'69_10_COMERCIALIZACI'        : 'COMERCIALIZACI_69_10'    }, axis=1)
values2 = values2.rename({'76_12_PATRIMONIO_FOR'        : 'PATRIMONIO_FOR_76_12'    }, axis=1)
values2 = values2.rename({'82_14_CAPACITACION_N'        : 'CAPACITACION_N_82_14'    }, axis=1)
values2 = values2.rename({'126_Modalidad_implem'        : 'Modalidad_implem_126'    }, axis=1)
values2 = values2.rename({'127_2Su_establecimie'        : 'Su_establecimie_127_2'   }, axis=1)
values2 = values2.rename({'128_Le_interesara_ac'        : 'Le_interesara_ac_128'    }, axis=1)
values2 = values2.rename({'125_Que_tipo_de_soft'        : 'Que_tipo_de_soft_125'    }, axis=1)
values2 = values2.rename({'128_Tipo_de_Softeare'        : 'Tipo_de_Softeare_128'    }, axis=1)
values2 = values2.rename({'129_Observaciones'           : 'Observaciones_129'       }, axis=1)
values2 = values2.rename({'137_Inversiones_real'        : 'Inversiones_real_137'    }, axis=1)
values2 = values2.rename({'144_Tipo_de_inversin'        : 'Tipo_de_inversin_144'    }, axis=1)
values2 = values2.rename({'146_Estara_dispuesto'        : 'Estara_dispuesto_146'    }, axis=1)
values2 = values2.rename({'136_Tipo_de_redes_so'        : 'Tipo_de_redes_so_136'    }, axis=1)
values2 = values2.rename({'137_Que_uso_le_dan'          : 'Que_uso_le_dan_137'      }, axis=1)
values2 = values2.rename({'152_Tiene_algun_pers'        : 'Tiene_algun_pers_152'    }, axis=1)
values2 = values2.rename({'153_En_caso_de_respo'        : 'En_caso_de_respo_153'    }, axis=1)
values2 = values2.rename({'154_Que_diferencial_'        : 'Que_diferencial_154'     }, axis=1)
values2 = values2.rename({'155_Est_dispuesto_a_'        : 'Est_dispuesto_a_155'     }, axis=1)
values2 = values2.rename({'131_Foto1'                   : 'Foto1_131'               }, axis=1)
values2 = values2.rename({'132_Foto_2'                  : 'Foto_2_132'              }, axis=1)
values2 = values2.rename({'133_Foto_3'                  : 'Foto_3_133'              }, axis=1)
values2 = values2.rename({'136_Observaciones_Ge'        : 'Observaciones_Ge_136'    }, axis=1)
values2 = values2.rename({'125_Ha_utilizado_su_'        : 'Ha_utilizado_su__125'    }, axis=1)

for index, row in values.iterrows():
    try:
        cur.execute(
        "INSERT INTO branch (ec5_branch_owner_uuid,ec5_branch_uuid,created_at,uploaded_at,created_by,title,"
        "rea_laboral_24,Nmero_de_personal_25,Nmero_de_personal_26) "
        "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)  ON CONFLICT (ec5_branch_owner_uuid) DO NOTHING;",
        (row.ec5_branch_owner_uuid, row.ec5_branch_uuid, row.created_at, row.uploaded_at, row.created_by, row.title,
         row.rea_laboral_24, row.Nmero_de_personal_25, row.Nmero_de_personal_26))
        con.commit()
    except:
        print('Falha ao inserir valores')
print('Informações do arquivo branch-1__3-rrhh.csv inseridas com Sucesso!')

for index, row in values2.iterrows():
    try:
        cur.execute(
            "INSERT INTO form (ec5_uuid,created_at,uploaded_at,created_by,title,lat_1_GPS,long_1_GPS,accuracy_1_GPS,"
            "UTM_Northing_1_GPS,UTM_Easting_1_GPS,UTM_Zone_1_GPS,Razn_Social_2,Razn_Social_opcion_3,Situaci_4,CUITCUIL_5,"
            "Correo_electrnico_6,Propietario_7,Telfono_8,Superficie_total_10,Superficie_cubier_11,Potencia_total_in_12,"
            "Consumo_de_energa_13,Capacidad_total_i_14,Capacidad_total_i_15,Produccin_anual_a_16,Produccin_anual_a_17,"
            "Produccin_anual_u_18,Mesao_22,Dasmes_21,Nmero_de_turnosda_19,Horasturno_20,RRHH_23,LINEA_DE_ASERR_28,"
            "LINEA_DE_ASERR_37_5,LINEA_DE_COMPE_50_7,a__LINEA_DE_REM_35_4,Bao_antimanchas_46,Impregnado_47,"
            "Volumen_impregnad_58,Capacidad_total_d_59,Porcentaje_propio_81,Tienen_CATEM_62,Tipo_de_secado_65,"
            "Porcentaje_de_sec_66,Capacidad_instala_63,Volumen_secado_mm_64,Tiene_deficiencia_63,Tiene_intensin_de_62,"
            "Tipo_de_chip_75,Toneladas_anuales_76,Destino_77,SECADO_34_5,AFILADO_81_13,Potencia_total_de_81,"
            "Tipo_de_maquina_89,Otra_aclarar_93,Cantidad_88,Ao_de_compra_91,Cuenta_con_EPP_51,Cuenta_con_preven_52,"
            "Tiene_ART_53,Elementos_anti_in_54,Red_antiincendio_93,Observaciones_55,MATERIA_PRIMA_p_56_8,"
            "PRODUCCIN_prome_64_9,COMERCIALIZACI_69_10,PATRIMONIO_FOR_76_12,CAPACITACION_N_82_14,Ha_utilizado_su__125,"
            "Modalidad_implem_126,Su_establecimie_127_2,Le_interesara_ac_128,Que_tipo_de_soft_125,Tipo_de_Softeare_128,"
            "Observaciones_129,Inversiones_real_137,Tipo_de_inversin_144,Estara_dispuesto_146,Tipo_de_redes_so_136,"
            "Que_uso_le_dan_137,Tiene_algun_pers_152,En_caso_de_respo_153,Que_diferencial_154,Est_dispuesto_a_155,Foto1_131,"
            "Foto_2_132,Foto_3_133,Observaciones_Ge_136)"
            "values("
            " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,"
            " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,"
            " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,"
            " %s, %s,%s, %s, %s )  ON CONFLICT (ec5_uuid) DO NOTHING;",
            (row.ec5_uuid, row.created_at, row.uploaded_at, row.created_by, row.title, row.lat_1_GPS, row.long_1_GPS,
             row.accuracy_1_GPS, row.UTM_Northing_1_GPS, row.UTM_Easting_1_GPS, row.UTM_Zone_1_GPS, row.Razn_Social_2,
             row.Razn_Social_opcion_3, row.Situaci_4, row.CUITCUIL_5, row.Correo_electrnico_6, row.Propietario_7,
             row.Telfono_8, row.Superficie_total_10, row.Superficie_cubier_11, row.Potencia_total_in_12,
             row.Consumo_de_energa_13, row.Capacidad_total_i_14, row.Capacidad_total_i_15, row.Produccin_anual_a_16,
             row.Produccin_anual_a_17, row.Produccin_anual_u_18, row.Mesao_22, row.Dasmes_21, row.Nmero_de_turnosda_19,
             row.Horasturno_20, row.RRHH_23, row.LINEA_DE_ASERR_28, row.LINEA_DE_ASERR_37_5, row.LINEA_DE_COMPE_50_7,
             row.a__LINEA_DE_REM_35_4, row.Bao_antimanchas_46, row.Impregnado_47, row.Volumen_impregnad_58,
             row.Capacidad_total_d_59, row.Porcentaje_propio_81, row.Tienen_CATEM_62, row.Tipo_de_secado_65,
             row.Porcentaje_de_sec_66, row.Capacidad_instala_63, row.Volumen_secado_mm_64, row.Tiene_deficiencia_63,
             row.Tiene_intensin_de_62, row.Tipo_de_chip_75, row.Toneladas_anuales_76, row.Destino_77, row.SECADO_34_5,
             row.AFILADO_81_13, row.Potencia_total_de_81, row.Tipo_de_maquina_89, row.Otra_aclarar_93, row.Cantidad_88,
             row.Ao_de_compra_91, row.Cuenta_con_EPP_51, row.Cuenta_con_preven_52, row.Tiene_ART_53,
             row.Elementos_anti_in_54, row.Red_antiincendio_93, row.Observaciones_55, row.MATERIA_PRIMA_p_56_8,
             row.PRODUCCIN_prome_64_9, row.COMERCIALIZACI_69_10, row.PATRIMONIO_FOR_76_12, row.CAPACITACION_N_82_14,
             row.Ha_utilizado_su__125, row.Modalidad_implem_126, row.Su_establecimie_127_2, row.Le_interesara_ac_128,
             row.Que_tipo_de_soft_125, row.Tipo_de_Softeare_128, row.Observaciones_129, row.Inversiones_real_137,
             row.Tipo_de_inversin_144, row.Estara_dispuesto_146, row.Tipo_de_redes_so_136, row.Que_uso_le_dan_137,
             row.Tiene_algun_pers_152, row.En_caso_de_respo_153, row.Que_diferencial_154, row.Est_dispuesto_a_155,
             row.Foto1_131, row.Foto_2_132, row.Foto_3_133, row.Observaciones_Ge_136))
        con.commit()
    except:
        print('Falha ao inserir valores')
print('Informações do arquivo form-1__industrias.csv inseridas com Sucesso!')
cur.close()
