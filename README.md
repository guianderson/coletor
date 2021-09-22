# Coletor

## Primeiros Passos


#### 1.  Criação do ambiente virutal.

1.1.    Instalar a virtualenv
```sh
pip install virtualenv
```

1.2.    Criar virtualenv
```sh
virtualenv nome_da_virtualenv
```

1.3.    Ativar a virtual env
```sh
cd nome_da_venv/Scripts
Activate
```

#### 2.  Instalar dependência do projeto
2.1.    Retorne até a raiz do projeto
```sh
cd ../..
```

2.2.    Instalar todas as dependências do projeto
```sh
cd core
pip install -r requirements.txt
```

#### 3. Criação do Banco de dados

###### 3.1 Criando tabela responsável por armazenar informações do arquivo branch-1__3-rrhh.csv 
```sh
CREATE TABLE branch (
	ec5_branch_owner_uuid 	VARCHAR ( 255 ) PRIMARY KEY,
	ec5_branch_uuid 		VARCHAR ( 255 ) UNIQUE NOT NULL,
	created_at 				date,
	uploaded_at 			date,
	created_by 				varchar(255),
    title 					varchar(255) ,
	rea_laboral_24			varchar(255),
	Nmero_de_personal_25 	varchar(255),
	Nmero_de_personal_26 	varchar(255)
);
```

###### 3.2 Criando tabela responsável por armazenar informações do arquivo form-1__industrias.csv
```sh
CREATE TABLE form(
	ec5_uuid				VARCHAR ( 255 ) PRIMARY KEY,
	created_at				date,
	uploaded_at				date,
	created_by				varchar (255),
	title					varchar (255),
	lat_1_GPS				varchar (255),
	long_1_GPS				varchar (255),
	accuracy_1_GPS			varchar (255),
	UTM_Northing_1_GPS		varchar (255),
	UTM_Easting_1_GPS		varchar (255),
	UTM_Zone_1_GPS			varchar (255),
	Razn_Social_2			varchar (255),
	Razn_Social_opcion_3	varchar (255),
	Situaci_4				varchar (255),
	CUITCUIL_5				varchar (255),
	Correo_electrnico_6		varchar (255),
	Propietario_7			varchar (255),
	Telfono_8				varchar (255),
	Superficie_total_10		varchar (255),
	Superficie_cubier_11	varchar (255),
	Potencia_total_in_12	varchar (255),
	Consumo_de_energa_13	varchar (255),
	Capacidad_total_i_14	varchar (255),
	Capacidad_total_i_15	varchar (255),
	Produccin_anual_a_16	varchar (255),
	Produccin_anual_a_17	varchar (255),
	Produccin_anual_u_18	varchar (255),
	Mesao_22				varchar (255),
	Dasmes_21				varchar (255),
	Nmero_de_turnosda_19	varchar (255),
	Horasturno_20			varchar (255),
	RRHH_23					varchar (255),
	LINEA_DE_ASERR_28		varchar (255),
	LINEA_DE_ASERR_37_5		varchar (255),
	LINEA_DE_COMPE_50_7		varchar (255),
	a__LINEA_DE_REM_35_4	varchar (255),
	Bao_antimanchas_46		varchar (255),
	Impregnado_47			varchar (255),
	Volumen_impregnad_58	varchar (255),
	Capacidad_total_d_59	varchar (255),
	Porcentaje_propio_81	varchar (255),
	Tienen_CATEM_62			varchar (255),
	Tipo_de_secado_65		varchar (255),
	Porcentaje_de_sec_66	varchar (255),
	Capacidad_instala_63	varchar (255),
	Volumen_secado_mm_64	varchar (255),
	Tiene_deficiencia_63	varchar (255),
	Tiene_intensin_de_62	varchar (255),
	Tipo_de_chip_75			varchar (255),
	Toneladas_anuales_76	varchar (255),
	Destino_77				varchar (255),
	SECADO_34_5				varchar (255),
	AFILADO_81_13			varchar (255),	
	Potencia_total_de_81	varchar (255),
	Tipo_de_maquina_89		varchar (255),
	Otra_aclarar_93			varchar (255),
	Cantidad_88				varchar (255),
	Ao_de_compra_91			varchar (255),
	Cuenta_con_EPP_51		varchar (255),
	Cuenta_con_preven_52	varchar (255),
	Tiene_ART_53			varchar (255),
	Elementos_anti_in_54	varchar (255),
	Red_antiincendio_93		varchar (255),
	Observaciones_55		varchar (255),
	MATERIA_PRIMA_p_56_8	varchar (255),
	PRODUCCIN_prome_64_9	varchar (255),
	COMERCIALIZACI_69_10	varchar (255),
	PATRIMONIO_FOR_76_12	varchar (255),
	CAPACITACION_N_82_14	varchar (255),
	Ha_utilizado_su__125	varchar (255),
	Modalidad_implem_126	varchar (255),
	Su_establecimie_127_2	varchar (255),
	Le_interesara_ac_128	varchar (255),
	Que_tipo_de_soft_125	varchar (255),
	Tipo_de_Softeare_128	varchar (255),
	Observaciones_129		varchar (255),
	Inversiones_real_137	varchar (255),
	Tipo_de_inversin_144	varchar (255),
	Estara_dispuesto_146	varchar (255),
	Tipo_de_redes_so_136	varchar (255),
	Que_uso_le_dan_137		varchar (255),
	Tiene_algun_pers_152	varchar (255),
	En_caso_de_respo_153	varchar (255),
	Que_diferencial_154		varchar (255),
	Est_dispuesto_a_155		varchar (255),
	Foto1_131				varchar (255),
	Foto_2_132				varchar (255),
	Foto_3_133				varchar (255),
	Observaciones_Ge_136	varchar (255)
);
```

#### 4. Configuração da conexão com Banco de dados

No arquivo main.py, localizado dentro da pasta coletor/core, na linha 5, existe <br/>
uma variável chamada **con**, ela armazena as informações de conexão com
o banco de dados.

- **Host:** Endereço do seu banco de dados<br>
- **Database:** Nome da sua conexão<br>
- **User:** Usuário para acessar o Banco de dados<br>
- **Password:** Senha para acessar o Banco de dados<br>

```sh
con = psycopg2.connect(host='localhost', database='alejandro', user='postgres', password='postgres')
```

#### 5. Executando projeto

Para executar o projeto basta estar dentro da pasta **core** e executar: 

```sh
python main.py
```