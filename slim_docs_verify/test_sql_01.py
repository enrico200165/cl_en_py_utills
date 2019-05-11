
sql_test_comments_01 = "aaa/**/aaaabbb/*xxxxxxx*/bbbbbbbbbbcccc/*xxxxxxx*/ccccccccd#ddddd"

sql_test_comments_02 = '''\
ok
\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ANAG_TEAM"
ok 2
'''


sql_test_comments_03 = '''\
segue has comment  # bbb
dopo questo commento multilineat /* non dovresti vederlo
non dovresti vederlo */ ok

'''

sql_test_ddl_01 = '''\

CREATE TABLE  "T_DMT_P4C_DM_ANAG_PARTNER"
(
     PK_P4C_PARTNER                    bigint                   not null,
     DTA_INIZIO_VALIDITA               timestamp                not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                  not null  default 1,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                   not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                   not null  default 0,
     CDN_MASTER                        bigint                   not null  default 0,
     DTA_INSERIMENTO                   timestamp                not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_UTENTE_INSERIMENTO             bigint                   not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                   not null  default -1,
     FLN_CANC_FISICA                   byteint                  not null  default 2,
     DTA_CANC_FISICA                   timestamp                not null  default '2999-12-31'::DATE,
     CDC_SOCIETA_PARTNER               character varying(50)    not null  default '***'::"NVARCHAR",
     SDS_NOME_MIS_ML                   character varying(50)    not null  default '***'::"NVARCHAR",
     SDS_NOME_WR                       character varying(50)    not null  default '***'::"NVARCHAR",
     CDC_PROFILAZIONE                  character varying(50)    not null  default '***'::"NVARCHAR",
     CDC_MATRICOLA_UTENTE              character varying(50)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_P4C_PARTNER)
;

/*
       Number of columns  18
 
    (Variable) Data Size  100 - 350
            Row Overhead  28 - 30
  ======================  =============
  Total Row Size (bytes)  128 - 380
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ANAG_TEAM"

CREATE TABLE  T_DMT_P4C_DM_ANAG_TEAM
(
     PK_P4C_TEAM                       bigint                             not null,
     DTA_INIZIO_VALIDITA               timestamp                          not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                          not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                            not null  default 1,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                             not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                             not null  default 0,
     CDN_MASTER                        bigint                             not null  default 0,
     DTA_INSERIMENTO                   timestamp                          not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                          not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_UTENTE_INSERIMENTO             bigint                             not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                             not null  default -1,
     FLN_CANC_FISICA                   byteint                            not null  default 2,
     DTA_CANC_FISICA                   timestamp                          not null  default '2999-12-31'::DATE,
     XN0_CODICE_TEAM                   national character varying(500)    not null  default '***'::"NVARCHAR",
     CDC_PARTNER                       character varying(50)              not null  default '***'::"NVARCHAR",
     CDC_SOCIETA_PARTNER               character varying(50)              not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_P4C_TEAM)
;

/*
       Number of columns  16
 
    (Variable) Data Size  96 - 2196
            Row Overhead  28
  ======================  =============
  Total Row Size (bytes)  124 - 2224
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_CANALE_CONTATTO"

CREATE TABLE  T_DMT_P4C_DM_CANALE_CONTATTO
(
     PK_CANALE_CONTATTO                bigint                    not null,
     CDN_MASTER                        bigint                    not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PIATTAFORMA                   character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO               character varying(255)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_CANALE_CONTATTO)
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_DM_CANALE_CONTATTO
ALTER TABLE T_DMT_P4C_DM_CANALE_CONTATTO ADD Constraint PK_CANALE_CONTATTO PRIMARY KEY (PK_CANALE_CONTATTO);

/*
       Number of columns  17
 
    (Variable) Data Size  98 - 710
            Row Overhead  30
  ======================  =============
  Total Row Size (bytes)  128 - 740
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_DIRECT_CONTROLLORI"

CREATE TABLE  T_DMT_P4C_DM_DIRECT_CONTROLLORI
(
     LDS_PIATTAFORMA                   character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO               character varying(255)    not null  default '***'::"NVARCHAR",
     SDS_NOME_PARTNER_CONTROLLORE      character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_RIFERIMENTO                   timestamp                 not null  default '1900-01-01'::DATE,
     QTA_CAMPIONE_LAVORATO             bigint,
     PK_DMT_DIRECT_CONTROLLORI         bigint                    not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default 'DIRECT'::"NVARCHAR",
     FK_PARTNER                        bigint                    not null  default 0,
     FK_CANALE_CONTATTO                bigint                    not null  default 0,
     FK_DTA_RIFERIMENTO                bigint                    not null  default 0,
     FK_PARTNER_SITE                   bigint                    not null  default 0
)
DISTRIBUTE ON RANDOM
;

/*
       Number of columns  23
 
    (Variable) Data Size  140 - 802
            Row Overhead  32 - 34
  ======================  =============
  Total Row Size (bytes)  172 - 836
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_DIRECT_INDICATORI"

CREATE TABLE  T_DMT_P4C_DM_DIRECT_INDICATORI
(
     LDS_PIATTAFORMA                   character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO               character varying(255)    not null  default '***'::"NVARCHAR",
     FLC_GRACE_PERIOD                  character(1)              not null  default '*'::"NVARCHAR",
     SDS_NOME_PARTNER                  character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_RIFERIMENTO                   timestamp                 not null  default '1900-01-01'::DATE,
     DTA_AGGIORNAMENTO_DIRECT          timestamp                 not null  default '1900-01-01'::DATE,
     QTA_CAMPIONI                      bigint,
     QTA_CAMPIONE_CONFORMI             bigint,
     QTA_CAMPIONE_NON_CONFORMI         bigint,
     VAL_PESI_NON_CONFORM_RILEVATA     numeric(22,7),
     VAL_PESI_NON_CONFORM_POTENZ       numeric(22,7),
     VAL_PERFORMANCE_OPERATIVA         numeric(22,7),
     VAL_DIFETTOSITA                   numeric(22,7),
     QTA_CAMPIONI_WORST                bigint,
     QTA_CAMPIONI_BEST                 bigint,
     PK_DMT_DIRECT_INDICATORI          bigint                    not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default 'DIRECT'::"NVARCHAR",
     FK_PARTNER                        bigint                    not null  default 0,
     FK_CANALE_CONTATTO                bigint                    not null  default 0,
     FK_DTA_RIFERIMENTO                bigint                    not null  default 0,
     FK_PARTNER_SITE                   bigint                    not null  default 0
)
DISTRIBUTE ON RANDOM
;

/*
       Number of columns  33
 
    (Variable) Data Size  245 - 907
            Row Overhead  35 - 33
  ======================  =============
  Total Row Size (bytes)  280 - 940
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_PARTNER_SITE"

CREATE TABLE  T_DMT_P4C_DM_PARTNER_SITE
(
     FK_IDN_AUDIT_PROGRAMMA      bigint                    not null  default 0,
     PK_P4C_PARTNER_SITE         bigint                    not null  default 0,
     CDN_MASTER                  bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO       bigint                    not null  default 0,
     DTA_INSERIMENTO             timestamp                 not null,
     FK_UTENTE_AGGIORNAMENTO     bigint                    not null  default 0,
     DTA_AGGIORNAMENTO           timestamp                 not null,
     DTA_INIZIO_VALIDITA         timestamp                 not null,
     DTA_FINE_VALIDITA           timestamp                 not null,
     FLN_VALIDITA                byteint                   not null  default 0,
     DTA_CANC_FISICA             timestamp                 not null,
     FLN_CANC_FISICA             byteint                   not null  default 0,
     LDS_AGENT_SITE              character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_ENTE_DEST               character varying(255)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_P4C_PARTNER_SITE)
;

/*
       Number of columns  14
 
    (Variable) Data Size  86 - 598
            Row Overhead  30
  ======================  =============
  Total Row Size (bytes)  116 - 628
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_PIATTAFORMA"

CREATE TABLE  T_DMT_P4C_DM_PIATTAFORMA
(
     PK_PIATTAFORMA                    bigint                    not null  default 0,
     CDN_MASTER                        bigint                    not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PIATTAFORMA                   character varying(255)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON RANDOM
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_DM_PIATTAFORMA
ALTER TABLE T_DMT_P4C_DM_PIATTAFORMA ADD Constraint PK_PIATTAFORMA PRIMARY KEY (PK_PIATTAFORMA);

/*
       Number of columns  15
 
    (Variable) Data Size  94 - 400
            Row Overhead  30 - 28
  ======================  =============
  Total Row Size (bytes)  124 - 428
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_QUARTI_ORA"

CREATE TABLE  T_DMT_P4C_DM_QUARTI_ORA
(
     PK_P4C_QUARTO_ORA                 bigint                   not null,
     DTA_INIZIO_VALIDITA               timestamp                not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                  not null  default 1,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                   not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                   not null  default 0,
     CDN_MASTER                        bigint                   not null  default 0,
     DTA_INSERIMENTO                   timestamp                not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_UTENTE_INSERIMENTO             bigint                   not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                   not null  default -1,
     FLN_CANC_FISICA                   byteint                  not null  default 2,
     DTA_CANC_FISICA                   timestamp                not null  default '2999-12-31'::DATE,
     SDS_QUARTO_ORA                    character varying(50)    not null  default '***'::"NVARCHAR",
     SDS_DESC_QUARTO_ORA               character varying(50)    not null  default '***'::"NVARCHAR",
     SDS_FASCIA_ORARIA                 character varying(50)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_P4C_QUARTO_ORA)
;

/*
       Number of columns  16
 
    (Variable) Data Size  96 - 246
            Row Overhead  28 - 30
  ======================  =============
  Total Row Size (bytes)  124 - 276
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_TIPO_CLIENTE"

CREATE TABLE  T_DMT_P4C_DM_TIPO_CLIENTE
(
     PK_DMT_TIPO_CLIENTE         bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA      bigint                    not null  default 0,
     CDN_MASTER                  bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO       bigint                    not null  default 0,
     DTA_INSERIMENTO             timestamp                 not null,
     FK_UTENTE_AGGIORNAMENTO     bigint                    not null  default 0,
     DTA_AGGIORNAMENTO           timestamp                 not null,
     DTA_INIZIO_VALIDITA         timestamp                 not null,
     DTA_FINE_VALIDITA           timestamp                 not null,
     FLN_VALIDITA                byteint                   not null  default 0,
     DTA_CANC_FISICA             timestamp                 not null,
     FLN_CANC_FISICA             byteint                   not null  default 0,
     CDC_SISTEMA_PROVENIENZA     character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_TIPO_CLIENTE            character varying(120)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON RANDOM
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_DM_TIPO_CLIENTE
ALTER TABLE T_DMT_P4C_DM_TIPO_CLIENTE ADD Constraint PK_DMT_TIPO_CLIENTE PRIMARY KEY (PK_DMT_TIPO_CLIENTE);

/*
       Number of columns  14
 
    (Variable) Data Size  86 - 256
            Row Overhead  30 - 28
  ======================  =============
  Total Row Size (bytes)  116 - 284
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_TIPO_EVENTO"

CREATE TABLE  T_DMT_P4C_DM_TIPO_EVENTO
(
     PK_DMT_TIPO_EVENTO                bigint                    not null,
     CDN_MASTER                        bigint                    not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                    character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                    character varying(50)     not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON RANDOM
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_DM_TIPO_EVENTO
ALTER TABLE T_DMT_P4C_DM_TIPO_EVENTO ADD Constraint PK_DMT_TIPO_EVENTO PRIMARY KEY (PK_DMT_TIPO_EVENTO);

/*
       Number of columns  17
 
    (Variable) Data Size  98 - 710
            Row Overhead  30
  ======================  =============
  Total Row Size (bytes)  128 - 740
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_CDR_CHAT"

CREATE TABLE  T_DMT_P4C_FT_CDR_CHAT
(
     PK_P4C_CDR_CHAT                   bigint                    not null,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     FLN_CANC_FISICA                   byteint                   not null  default 0,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     DTA_INSERIMENTO                   timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_P4C_PARTNER                    bigint                    not null  default 0,
     FK_P4C_QD                         bigint                    not null  default 0,
     FK_TEMPO                          bigint                    not null  default 0,
     FK_P4C_CANALE_CONTATTO            bigint                    not null  default 0,
     FLC_RISPOSTA                      character(1)              not null  default '*'::"NVARCHAR",
     FLN_RISPOSTA                      byteint                   not null  default 0,
     XD0_MOTIVO_1L                     character varying(500)    not null  default '***'::"NVARCHAR",
     QTA_CONTATTI_CHAT                 bigint
)
DISTRIBUTE ON (PK_P4C_CDR_CHAT)
;

/*
       Number of columns  20
 
    (Variable) Data Size  126 - 626
            Row Overhead  34
  ======================  =============
  Total Row Size (bytes)  160 - 660
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_CDR_INBOUND"

CREATE TABLE  T_DMT_P4C_FT_CDR_INBOUND
(
     PK_P4C_CDR_INBOUND                bigint                     not null,
     DTA_INIZIO_VALIDITA               timestamp                  not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                  not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                     not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                     not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                     not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                     not null  default -1,
     FLN_CANC_FISICA                   byteint                    not null  default 0,
     DTA_CANC_FISICA                   timestamp                  not null  default '2999-12-31'::DATE,
     DTA_INSERIMENTO                   timestamp                  not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                  not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_P4C_PARTNER                    bigint                     not null  default 0,
     FK_P4C_CANALE_CONTATTO            bigint                     not null  default 0,
     FK_TEMPO                          bigint                     not null  default 0,
     FK_P4C_QD                         bigint                     not null  default 0,
     FK_TIPO_CLIENTE                   bigint                     not null  default 0,
     FK_CODA                           bigint                     not null  default 0,
     SDS_TIPOLOGIA_TEL                 character varying(50)      not null  default '***'::"NVARCHAR",
     FLC_REPEATED                      character(1)               not null  default '*'::"NVARCHAR",
     FLN_REPEATED                      byteint                    not null  default 0,
     XD1_CODA                          character varying(1000)    not null  default '***'::"NVARCHAR",
     SDS_MERCATO                       character varying(50)      not null  default '***'::"NVARCHAR",
     QTA_CHIAMATE_INBOUND              bigint,
     FK_P4C_PARTNER_SITE               bigint                     not null  default 0,
     LDS_FASCIA_TEMPO_CONVER           character varying(255)     not null  default '***'::"NVARCHAR",
     LDS_ATTESA_CODA                   character varying(255)     not null  default '***'::"NVARCHAR",
     FLC_RICH_OP                       character(1)               not null  default '*'::"NVARCHAR",
     FLC_RISP_AGENT                    character(1)               not null  default '*'::"NVARCHAR"
)
DISTRIBUTE ON (PK_P4C_CDR_INBOUND)
;

/*
       Number of columns  29
 
    (Variable) Data Size  160 - 1772
            Row Overhead  32
  ======================  =============
  Total Row Size (bytes)  192 - 1804
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_CDR_OUTBOUND"

CREATE TABLE  T_DMT_P4C_FT_CDR_OUTBOUND
(
     PK_P4C_CDR_OUTBOUND               bigint                    not null,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     FLN_CANC_FISICA                   byteint                   not null  default 0,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     DTA_INSERIMENTO                   timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_P4C_PARTNER                    bigint                    not null  default 0,
     FK_P4C_QD                         bigint                    not null  default 0,
     FK_TEMPO                          bigint                    not null  default 0,
     FK_P4C_CANALE_CONTATTO            bigint                    not null  default 0,
     SDS_MERCATO                       character varying(50)     not null  default '***'::"NVARCHAR",
     FLC_RISPOSTA                      character(1)              not null  default '*'::"NVARCHAR",
     FLN_RISPOSTA                      byteint                   not null  default 0,
     LDS_QC_CAMP_NAME                  character varying(255)    not null  default '***'::"NVARCHAR",
     QTA_CHIAMATE_OUTBOUND             bigint
)
DISTRIBUTE ON (PK_P4C_CDR_OUTBOUND)
;

/*
       Number of columns  21
 
    (Variable) Data Size  128 - 434
            Row Overhead  32 - 34
  ======================  =============
  Total Row Size (bytes)  160 - 468
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_COG_KPI_ISTITUZIONALE"

CREATE TABLE  T_DMT_P4C_FT_COG_KPI_ISTITUZIONALE
(
     PK_COG_KPI_ISTITUZIONALE          bigint                    not null,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default '***'::"NVARCHAR",
     FK_PARTNER                        bigint                    not null  default -1,
     LDS_PIATTAFORMA                   character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO               character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_ELABORAZIONE_KPI              timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     CDC_AGENZIA                       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_KPI                           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_DESCRIZIONE_KPI               character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_PERIODO_RIFERIMENTO           timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     VAL_VALORE_KPI                    numeric(22,7)
)
DISTRIBUTE ON RANDOM
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_FT_COG_KPI_ISTITUZIONALE
ALTER TABLE T_DMT_P4C_FT_COG_KPI_ISTITUZIONALE ADD Constraint PK_COG_KPI_ISTITUZIONALE PRIMARY KEY (PK_COG_KPI_ISTITUZIONALE);

/*
       Number of columns  22
 
    (Variable) Data Size  134 - 1052
            Row Overhead  34 - 32
  ======================  =============
  Total Row Size (bytes)  168 - 1084
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_CONSUNTIVO_SESSIONI_FP"

CREATE TABLE  T_DMT_P4C_FT_CONSUNTIVO_SESSIONI_FP
(
     PK_P4C_FP_CONSUNTIVO              bigint                    not null  default 0,
     CDN_MASTER                        bigint                    not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     CDC_ID_SESSIONE                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PIATTAFOMRA                   character varying(255)    not null  default '***'::"NVARCHAR",
     SDS_NOME_PARTNER                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_MACRO_AREA                    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_MODULO                        character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_GIORNI                 numeric(22,7),
     QTA_NUM_RISORSE                   bigint,
     VAL_ORE_GIORNO                    numeric(22,7),
     VAL_TOTALE                        numeric(22,7),
     DTA_CHIUSURA                      timestamp                 not null,
     VAL_PAGAMENTO                     numeric(22,7),
     LDS_TIPOLOGIA                     character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_NOME_EVENTO                   character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CDC                           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_NOME_FORMATORE                character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_INIZIO_CORSO                  timestamp                 not null,
     DTA_FINE_CORSO                    timestamp                 not null,
     LDS_N_F                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_MERCATO                       character varying(255)    not null  default '***'::"NVARCHAR",
     FK_DTA_CHIUSURA                   bigint                    not null  default 0,
     FK_PARTNER                        bigint                    not null  default 0
)
DISTRIBUTE ON (PK_P4C_FP_CONSUNTIVO)
;

/*
       Number of columns  34
 
    (Variable) Data Size  224 - 2422
            Row Overhead  32 - 34
  ======================  =============
  Total Row Size (bytes)  256 - 2456
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_LIBERO_CODE"

CREATE TABLE  T_DMT_P4C_FT_LIBERO_CODE
(
     PK_P4C_LIBERO_CODE                bigint                    not null,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     FLN_CANC_FISICA                   byteint                   not null  default 0,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     DTA_INSERIMENTO                   timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_TEMPO                          bigint                    not null  default 0,
     FK_PARTNER                        bigint                    not null  default 0,
     FK_QUARTO_ORA                     bigint                    not null  default 0,
     FK_CANALE_CONTATTO                bigint                    not null  default 0,
     LDS_CODA                          character varying(255)    not null  default '***'::"NVARCHAR",
     QTA_AEEG_RISP                     bigint,
     QTA_L_RISP_30                     bigint,
     QTA_L_RISP_31_60                  bigint,
     QTA_L_RISP_61_90                  bigint,
     QTA_L_RISP_91_120                 bigint,
     QTA_L_RISP_120                    bigint,
     QTA_L_RISP_180                    bigint,
     QTA_L_ATT_CODA_RISP               bigint,
     QTA_L_ATT_CODA_ABB                bigint,
     QTA_L_AEEG_RISP_END               bigint,
     QTA_L_AEEG_RICH_OP                bigint,
     QTA_L_AEEG_RICH_OP_GL             bigint,
     QTA_L_AEEG_RICH_OP_SG             bigint,
     QTA_L_CH_REG_VOCALI_OP            bigint,
     LDS_PROVENIENZA                   character varying(255)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_P4C_LIBERO_CODE)
;

/*
       Number of columns  32
 
    (Variable) Data Size  230 - 742
            Row Overhead  34
  ======================  =============
  Total Row Size (bytes)  264 - 776
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_LIBERO_GA"

CREATE TABLE  T_DMT_P4C_FT_LIBERO_GA
(
     PK_P4C_LIBERO_GA                  bigint       not null,
     DTA_INIZIO_VALIDITA               timestamp    not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp    not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint      not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint       not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint       not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint       not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint       not null  default -1,
     FLN_CANC_FISICA                   byteint      not null  default 0,
     DTA_CANC_FISICA                   timestamp    not null  default '2999-12-31'::DATE,
     DTA_INSERIMENTO                   timestamp    not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp    not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_TEMPO                          bigint       not null  default 0,
     FK_PARTNER                        bigint       not null  default 0,
     FK_QD                             bigint       not null  default 0,
     FK_GRUPPO_AGENTE                  bigint       not null  default 0,
     FK_CANALE_CONTATTO                bigint       not null  default 0,
     QTA_L_RISP                        bigint,
     QTA_L_RISP_GL                     bigint,
     QTA_L_GA_NUM_CH_RISP_SGCRM        bigint,
     QTA_L_RISP_GHOST                  bigint,
     QTA_L_GA_NUM_RISP_CON_SEL0        bigint,
     QTA_L_RISP_SC1                    bigint,
     QTA_L_RISP_SC2                    bigint,
     QTA_L_NUM_RISP_CONS_2_1           bigint,
     QTA_L_NUM_RISP_CONS_2_4           bigint,
     QTA_L_RISP_SC3                    bigint,
     QTA_L_RISP_SC4                    bigint,
     QTA_GA_NUM_RISP_CONS_50           bigint,
     QTA_L_CONS_CONV                   bigint,
     QTA_L_CONS_LOGGATI                bigint,
     QTA_L_CONS_READY                  bigint,
     QTA_L_CONS_NOT_READY              bigint,
     QTA_L_CONS_IN_ACW                 bigint,
     QTA_L_CONS_IN_PAUSA               bigint,
     QTA_L_TIME_CONV                   bigint,
     QTA_L_TIME_CONV_GL                bigint,
     QTA_L_TIME_CONV_SG_CRM            bigint,
     QTA_L_TIME_CONV_GHOST             bigint,
     QTA_L_GA_TMPCONVSEL0              bigint,
     QTA_L_TIMECONV_SC1                bigint,
     QTA_L_TIMECONV_SC2                bigint,
     QTA_L_TIMECONV_SC3                bigint,
     QTA_L_TIMECONV_SC4                bigint,
     QTA_L_GA_TMPCONVSEL50             bigint,
     QTA_L_RISP_TIMECONV_0_6S          bigint,
     QTA_L_RISP_TIMECONV_6_10S         bigint,
     QTA_L_RISP_TIMECONV_10_30S        bigint,
     QTA_L_RISP_TIMECONV_30_60S        bigint,
     QTA_L_RISP_TIMECONV_60_120S       bigint,
     QTA_L_RISP_TIMECONV_120_180S      bigint,
     QTA_L_RISP_TIMECONV_180_300S      bigint,
     QTA_L_RISP_TIMECONV_300S          bigint,
     QTA_L_TIMEJCK_TOTALE_CONSLOG      bigint,
     QTA_L_TIMEJCK_CONSLOG             bigint,
     QTA_L_TIMEACW_CONSLOGGATI         bigint,
     QTA_L_TIMEHOLD_CONSLOGGATI        bigint,
     QTA_T_PAUSA_TRAIN_CONSLOGGATI     bigint,
     QTA_T_PAUSA_MENSA_CONSLOGGATI     bigint,
     QTA_T_PAUSA626_CONSLOGGATI        bigint,
     QTA_T_PAUSA_DOC_CONSLOG           bigint,
     QTA_T_ALTRE_PAUSE_NON_MOT         bigint,
     QTA_T_PATT_CONSPARTNER            bigint,
     QTA_T_CONV_CONSULTAZIONE          bigint,
     QTA_T_NUM_CH_OUTB_RISP            bigint,
     QTA_T_CONV_OUTBOUND               bigint,
     QTA_T_ACW_OUTBOUND                bigint,
     QTA_L_CLIENTE_1VAL                bigint,
     QTA_L_CLIENTE_2VAL                bigint,
     QTA_L_CLIENTE_3VAL                bigint,
     QTA_L_CLIENTE_4VAL                bigint,
     QTA_L_CLIENTE_5VAL                bigint,
     QTA_L_RISP_T_10_20S               bigint,
     QTA_L_RISP_T_20_30S               bigint,
     QTA_L_RISP_T_10_30S               bigint
)
DISTRIBUTE ON (PK_P4C_LIBERO_GA)
;

/*
       Number of columns  75
 
    (Constant) Data Size  586
            Row Overhead  38
  ======================  =============
  Total Row Size (bytes)  624
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_LIBERO_GA_TEAM"

CREATE TABLE  T_DMT_P4C_FT_LIBERO_GA_TEAM
(
     PK_P4C_LIBERO_TEAM                bigint       not null,
     DTA_INIZIO_VALIDITA               timestamp    not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp    not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint      not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint       not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint       not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint       not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint       not null  default -1,
     FLN_CANC_FISICA                   byteint      not null  default 0,
     DTA_CANC_FISICA                   timestamp    not null  default '2999-12-31'::DATE,
     DTA_INSERIMENTO                   timestamp    not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp    not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_TEMPO                          bigint       not null  default 0,
     FK_PARTNER                        bigint       not null  default 0,
     FK_QUARTO_ORA                     bigint       not null  default 0,
     FK_TEAM                           bigint       not null  default 0,
     QTA_RISP_CONS_TOT                 bigint,
     QTA_T_CONVERSAZIONE               bigint,
     QTA_T_CON_0_6                     bigint,
     QTA_T_CON_6_10                    bigint,
     QTA_JACK_IN_LOGGATI               bigint,
     QTA_JACK_IN_LOGGATI_RING          bigint,
     QTA_T_PAUSA                       bigint,
     QTA_T_HOLD_LOGGATI                bigint,
     QTA_ACW_CON_LOG                   bigint,
     QTA_T_PAUSA_TRAINING              bigint,
     QTA_T_PAUSA_MESA                  bigint,
     QTA_T_PAUSA_DOCUMENTALE           bigint,
     QTA_T_ALTRE_PAUSE                 bigint,
     QTA_T_ATT_CONS_PARTNER            bigint,
     QTA_T_CONV_CONSULTAZIONE          bigint,
     QTA_RISP_EMCC                     bigint,
     QTA_RISP_TC_EMCC                  bigint,
     FK_CANALE_CONTATTO                bigint       not null  default 0
)
DISTRIBUTE ON (PK_P4C_LIBERO_TEAM)
;

/*
       Number of columns  34
 
    (Constant) Data Size  258
            Row Overhead  34
  ======================  =============
  Total Row Size (bytes)  292
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_PIANIFICAZIONE_FORECAST_KD"

CREATE TABLE  T_DMT_P4C_FT_PIANIFICAZIONE_FORECAST_KD
(
     PK_P4C_KD_FORECAST                bigint                   not null  default 0,
     CDN_MASTER                        bigint                   not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                  not null  default 1,
     FLN_CANC_FISICA                   byteint                  not null  default 2,
     DTA_CANC_FISICA                   timestamp                not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                   not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                   not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                   not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                   not null  default -1,
     DTA_INSERIMENTO                   timestamp                not null  default DATE('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                not null  default DATE('now(0)'::"VARCHAR"),
     SDS_NOME_PARTNER                  character varying(50)    not null  default '***'::"NVARCHAR",
     DTA_RIFERIMENTO                   timestamp                not null,
     DTA_INVIO_FLUSSO                  timestamp                not null,
     VAL_SOSTENIBILITA_FORECAST        numeric(22,7),
     VAL_SOSTENIBILITA_PIANIFICATO     numeric(22,7),
     VAL_PIANIFICATO                   numeric(22,7),
     VAL_CONSUNTIVO                    numeric(22,7),
     FK_DTA_RIFERIMENTO                bigint                   not null  default 0,
     FK_DTA_INVIO_FLUSSO               bigint                   not null  default 0,
     FK_PARTNER                        bigint                   not null  default 0
)
DISTRIBUTE ON (PK_P4C_KD_FORECAST)
;

/*
       Number of columns  23
 
    (Variable) Data Size  196 - 246
            Row Overhead  32 - 34
  ======================  =============
  Total Row Size (bytes)  228 - 280
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_PIANIFICAZIONE_TEL_KD"

CREATE TABLE  T_DMT_P4C_FT_PIANIFICAZIONE_TEL_KD
(
     PK_P4C_KD_CONSUNTIVO              bigint                   not null  default 0,
     CDN_MASTER                        bigint                   not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                  not null  default 1,
     FLN_CANC_FISICA                   byteint                  not null  default 2,
     DTA_CANC_FISICA                   timestamp                not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                   not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                   not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                   not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                   not null  default -1,
     DTA_INSERIMENTO                   timestamp                not null  default DATE('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                not null  default DATE('now(0)'::"VARCHAR"),
     SDS_NOME_PARTNER                  character varying(50)    not null  default '***'::"NVARCHAR",
     CDC_COMMODITY                     character varying(50)    not null  default '***'::"NVARCHAR",
     DTA_RIFERIMENTO                   timestamp                not null,
     SDS_QUARTO_ORA                    character varying(50)    not null  default '***'::"NVARCHAR",
     VAL_PIANIFICAZIONE_I              numeric(22,7),
     VAL_PIANIFICAZIONE_II             numeric(22,7),
     VAL_PIANIFICAZIONE_LAST           numeric(22,7),
     FK_DTA_RIFERIMENTO                bigint                   not null  default 0,
     FK_PARTNER                        bigint                   not null  default 0,
     FK_QUARTI_ORA                     bigint                   not null  default 0
)
DISTRIBUTE ON (PK_P4C_KD_CONSUNTIVO)
;

/*
       Number of columns  23
 
    (Variable) Data Size  176 - 326
            Row Overhead  32 - 34
  ======================  =============
  Total Row Size (bytes)  208 - 360
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_PRESTAZIONE"

CREATE TABLE  T_DMT_P4C_FT_PRESTAZIONE
(
     PK_DMT_PRESTAZIONE                bigint                    not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null,
     DTA_AGGIORNAMENTO                 timestamp                 not null,
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_PARTNER                    bigint                    not null  default 0,
     FK_P4C_ATTIVITA                   bigint                    not null  default 0,
     FK_P4C_ATTIVAZIONI                bigint                    not null  default 0,
     FK_P4C_CASEITEM                   bigint                    not null  default 0,
     SK_IDN_INTERAZIONE                bigint                    not null  default 0,
     SK_IDN_CLIENTE_CRM                bigint                    not null  default 0,
     SK_IDN_RICHIESTA                  bigint                    not null  default 0,
     SK_IDN_SOTTOCANALE                bigint                    not null  default 0,
     SK_IDN_SITO                       bigint                    not null  default 0,
     FK_DTA_INSERIMENTO                bigint                    not null  default 0,
     FK_DTA_AGGIORNAMENTO              bigint                    not null  default 0,
     FK_CDR_INBOUND                    bigint                    not null  default 0,
     FK_CDR_CHAT                       bigint                    not null  default 0,
     FK_P4C_CANALE_CONTATTO            bigint                    not null  default 0,
     FK_P4C_TIPO_EVENTO                bigint                    not null  default 0,
     FK_CDR_OUTBOUND                   bigint                    not null  default 0,
     FK_P4C_COMMODITY                  bigint                    not null  default 0,
     FK_P4C_TIPO_CLIENTE               bigint                    not null  default 0,
     FK_P4C_PIATTAFORMA                bigint                    not null  default 0,
     VAL_DURATA_CHIAMATA_INTER         numeric(22,7),
     QTA_DURATA_CDR                    bigint,
     QTA_P4C_ATTIVITA                  bigint,
     QTA_P4C_ATTIVAZIONI               bigint,
     QTA_P4C_CASEITEM                  bigint,
     LDS_CODA                          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_MERCATO                       character varying(255)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_DMT_PRESTAZIONE)
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_FT_PRESTAZIONE
ALTER TABLE T_DMT_P4C_FT_PRESTAZIONE ADD Constraint PK_DMT_PRESTAZIONE PRIMARY KEY (PK_DMT_PRESTAZIONE);

/*
       Number of columns  39
 
    (Variable) Data Size  288 - 850
            Row Overhead  32 - 34
  ======================  =============
  Total Row Size (bytes)  320 - 884
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_FT_PRESTAZIONE_AGG"

CREATE TABLE  T_DMT_P4C_FT_PRESTAZIONE_AGG
(
     PK_DMT_PRESTAZIONE_AGG            bigint                   not null  default 0,
     DTA_INIZIO_VALIDITA               timestamp                not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                  not null  default 1,
     FLN_CANC_FISICA                   byteint                  not null  default 2,
     DTA_CANC_FISICA                   timestamp                not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                   not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                   not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                   not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                   not null  default -1,
     DTA_INSERIMENTO                   timestamp                not null,
     DTA_AGGIORNAMENTO                 timestamp                not null,
     CDC_SISTEMA_PROVENIENZA           character varying(50)    not null  default '***'::"NVARCHAR",
     SK_IDN_PARTNER                    bigint                   not null  default 0,
     FK_DTA_INSERIMENTO                bigint                   not null  default 0,
     FK_DTA_AGGIORNAMENTO              bigint                   not null  default 0,
     FK_P4C_PIATTAFORMA                bigint                   not null  default 0,
     FK_P4C_CANALE_CONTATTO            bigint                   not null  default 0,
     FK_P4C_TIPO_EVENTO                bigint                   not null  default 0,
     FK_P4C_COMMODITY                  bigint                   not null  default 0,
     FK_P4C_TIPO_CLIENTE               bigint                   not null  default 0,
     QTA_PRESTAZIONE                   bigint
)
DISTRIBUTE ON (PK_DMT_PRESTAZIONE_AGG)
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_FT_PRESTAZIONE_AGG
ALTER TABLE T_DMT_P4C_FT_PRESTAZIONE_AGG ADD Constraint PK_DMT_PRESTAZIONE_AGG PRIMARY KEY (PK_DMT_PRESTAZIONE_AGG);

/*
       Number of columns  22
 
    (Variable) Data Size  156 - 206
            Row Overhead  32 - 34
  ======================  =============
  Total Row Size (bytes)  188 - 240
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ATTIVAZIONI_FOTO_I4P"

CREATE TABLE  T_DMT_P4C_DM_ATTIVAZIONI_FOTO_I4P
(
     FK_IDN_AUDIT_PROGRAMMA                          bigint                    not null  default 0,
     PK_P4C_ATTIVAZIONI                              bigint                    not null  default 0,
     CDN_MASTER                                      bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO                           bigint                    not null  default 0,
     DTA_INSERIMENTO                                 timestamp                 not null,
     FK_UTENTE_AGGIORNAMENTO                         bigint                    not null  default 0,
     DTA_AGGIORNAMENTO                               timestamp                 not null,
     DTA_INIZIO_VALIDITA                             timestamp                 not null,
     DTA_FINE_VALIDITA                               timestamp                 not null,
     FLN_VALIDITA                                    byteint                   not null  default 0,
     DTA_CANC_FISICA                                 timestamp                 not null,
     FLN_CANC_FISICA                                 byteint                   not null  default 0,
     DTA_RIFERIMENTO_FLUSSO                          timestamp                 not null,
     LDS_CAUSALE_OPERAZIONE                          character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CASO_REMUNERAZIONE                          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CASO_REMUNERAZIONE_SFC                      character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CASO_REMUNERAZIONE_OLD                      character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_COD_AGENTE                                  character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA                              character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_EFFETTO                                     timestamp                 not null,
     DTA_INIZIO_TIMING                               timestamp                 not null,
     DTA_FINE_TIMING                                 timestamp                 not null,
     IDC_ROW_ID_OFFERTA                              character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_OFFERTA_OLD                          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_NUMERO_OFFERTA                              character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_OFFERTA                           timestamp                 not null,
     DTA_ULT_MOD_OFFERTA                             timestamp                 not null,
     LDS_STATO_OFFERTA_SFC                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_STATO_OFFERTA                               character varying(255)    not null  default '***'::"NVARCHAR",
     FLN_DOCUMENTO_ARCHIVIATO                        byteint                   not null  default 0,
     LDS_CAUSALE_STATO_OFFERTA                       character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_POD_OFFERTA                                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPOLOGIA_OFFERTA                           character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_OFFERTA                         character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_OFFERTA_OLD                     character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_RIGA_OFFERTA                      timestamp                 not null,
     DTA_ULT_MOD_RIGA_OFFERTA                        timestamp                 not null,
     LDS_STATO_RIGA_OFFERTA                          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_STATO_RIGA_OFFERTA                  character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_RIGA_OFFERTA                      character varying(120)    not null  default '***'::"NVARCHAR",
     FLN_CANCELLAZIONE_RIGA_OFFERTA                  byteint                   not null  default 0,
     IDC_ROW_ID_ORDINE                               character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_ORDINE_OLD                           character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_ORDINE                            timestamp                 not null,
     DTA_ULT_MOD_ORDINE                              timestamp                 not null,
     CDC_POD_ORDINE                                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPOLOGIA_ORDINE                            character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_ORDINE                          character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_ORDINE_OLD                      character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_RIGA_ORDINE                       timestamp                 not null,
     DTA_ULT_MOD_RIGA_ORDINE                         timestamp                 not null,
     LDS_STATO_RIGA_ORDINE                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_STATO_RIGA_ORDINE                   character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_RIGA_ORDINE                       character varying(120)    not null  default '***'::"NVARCHAR",
     FLN_CANCELLAZIONE_RIGA_ORDINE                   byteint                   not null  default 0,
     DTA_RILAVORAZIONE_COMMERCIALE                   timestamp                 not null,
     FLN_RILAVORAZIONE_COMMERCIALE                   byteint                   not null  default 0,
     CDC_STATO_RID                                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_SERVIZIO                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_NOME_PRODOTTO_SERVIZIO                      character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_DESCRIZIONE_PRODOTTO_SERVIZIO               character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_ATTIVAZIONE_SERVIZIO                        timestamp                 not null,
     LDS_STATO_SERVIZIO                              character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_CESSAZIONE_SERVIZIO                         timestamp                 not null,
     LDS_STATO_TRASPORTO                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CAP_PRODOTTO_SERVIZIO                       character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_COMUNE_PRODOTTO_SERVIZIO                    character varying(255)    not null  default '***'::"NVARCHAR",
     SDS_PROVINCIA_PRODOTTO                          character varying(50)     not null  default '***'::"NVARCHAR",
     VAL_TOT_POT_CONTRATTUALE_SITO                   numeric(22,7),
     VAL_TOT_POTENZA_DISPONIBILE                     numeric(22,7),
     FLN_OPZIONE_GREEN_PRODOTTO                      byteint                   not null  default 0,
     LDS_PIANO_PROVVIGIONALE_PROD                    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_TIPO_UTILIZZO_PRODOTTO                      character varying(255)    not null  default '***'::"NVARCHAR",
     FLC_RESIDENTE                                   character(1)              not null  default '*'::"NVARCHAR",
     LDS_TIPO_SERVIZIO_PRODOTTO                      character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_CLIENTE                              character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_CLIENTE_OLD                          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_BUSINESS_PARTNER                            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPOLOGIA_CLIENTE                           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_FISCALE_CLIENTE                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_PART_IVA_CLIENTE                            character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_RAGIONE_SOCIALE_CLIENTE                     character varying(120)    not null  default '***'::"NVARCHAR",
     LDS_FORMA_GIURIDICA                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CAP_CLIENTE                                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_COMUNE_CLIENTE                              character varying(255)    not null  default '***'::"NVARCHAR",
     SDS_SIGLA_PROVINCIA_CLIENTE                     character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_CONTATTO_VOCAL                              byteint                   not null  default 0,
     CDC_CANALE                                      character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_RID_IN_QC                                   byteint                   not null  default 0,
     DTA_ST_RICEVUTA                                 timestamp                 not null,
     DTA_ST_CHIUSA                                   timestamp                 not null,
     CDC_AGENZIA_BOLLETTA_WEB                        character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CATEGORIA_USO                               character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_MERCATO                                     character varying(255)    not null  default '***'::"NVARCHAR",
     FLN_BOLLETTA_WEB                                byteint                   not null  default 0,
     CDC_STATO_BOLLETTA_WEB                          character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_CROSS_SELLING                               byteint                   not null  default 0,
     IDC_ROW_ID_SITO                                 character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_SITO_OLD                             character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_INSERIMENTO_SDD                             timestamp                 not null  default '01-01-1900 00:00:00',
     LDS_FASE_INS_SDD                                character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_SOTTOCANALE_SDD                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_SDD                                 character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_BOLLETTA_WEB_IN_QC                          byteint                   not null  default 0,
     IDC_ROW_ID_INTERAZ                              character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_INTERAZ                                character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_CHIAMATA_INTERAZ                     numeric(22,7),
     DTA_CREAZ_INTERAZ                               timestamp                 not null  default '01-01-1900 00:00:00',
     IDN_SOTTOCANALE_ATTIVAZ_SDD                     bigint                    not null  default 0,
     LDS_CANALE_INVIO_CONTRATTO                      character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_MODALITA_FIRMA                              character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_ACQUISITIVO                 bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_INS_OFFERTA                    character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_OFFERTA                 bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_OFFERTA                    character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_OFFERTA                 bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_INS_LINEA_OFFERTA_FORN         character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_LINEA_OFFERTA_FORN      bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_LINEA_OFFERTA_FORN         character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_LINEA_OFFERTA_FORN      bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_RICEV             character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_RICEV          bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_DA_CONFERM        character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_DA_CONFERM     bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_SOSP              character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_SOSP           bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_CHIUSA            character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_CHIUSA         bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_ANNULL            character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_ANNULL         bigint                    not null  default 0,
     FLN_QC_CHIAMATA_CONCLUSA                        byteint                   not null  default 0,
     MDS_LOGIN_UTENTE_INS_LINEA_OFFERTA_BW           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_LINEA_OFFERTA_BW        bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_LINEA_OFFERTA_BW           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_LINEA_OFFERTA_BW        bigint                    not null  default 0,
     CDC_CODA_TELEFONICA                             character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SOTTOCODA_TELEFONICA                        character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ID_CASE                                     character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INTERAZ                     bigint                    not null  default 0,
     LDS_CONSENSO_MARKET_TELEFONO                    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_MARKET_EMAIL                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_MARKET_CELL                        character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_PROFILAZIONE                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_TERZI_TEL                          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_TERZI_EMAIL                        character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_TERZI_CELL                         character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_CLIENTE                                  bigint                    not null  default 0,
     SK_IDN_SITO                                     bigint                    not null  default 0,
     CDC_CALL_ID                                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE                                      character varying(255)    not null  default '***'::"NVARCHAR",
     QTA_DURATA                                      bigint,
     FK_CDR_INBOUND                                  bigint                    not null  default 0,
     FK_CDR_CHAT                                     bigint                    not null  default 0,
     FK_CDR_OUTBOUND                                 bigint                    not null  default 0,
     LDS_CODA    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_INS_OFFERTA                         character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_PARTNER_INS_OFFERTA                      bigint                    not null  default 0,
     SDS_SOTTOCANALE_INS_OFFERTA                     character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_OFFERTA                     character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INS_LINEA_OFFERTA_FORN          character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_LINEA_OFFERTA_FORN          character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_RICEV              character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_DA_CONFERM         character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_SOSP               character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_CHIUSA             character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_ANNULL             character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INS_LINEA_OFFERTA_BW            character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_LINEA_OFFERTA_BW            character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INTERAZ                         character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SOTTOCANALE_INS_OFF                      bigint                    not null  default 0,
     FLN_RID_OBBLIGATORIO                            byteint                   not null  default 0,
     LDS_PIATTAFORMA                                 character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                               character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                                     character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                                  character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PROCESSO_CASE                               character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_STATO_RICHIESTA_CASE                        character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SUBSTATO_RICHIESTA_CASE                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_CANCELLAZIONE_CASE                  character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CASE                                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_VAS_CASE                           character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_RICHIESTA                                bigint                    not null  default 0,
     CDC_STATO_UDB_CITEM                             character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_AGG_OFFERTA                  character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_INS_LINEA_OFFERTA_FORN       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_AGG_LINEA_OFFERTA_FORN       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_RICEV           character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_DA_CONFERM      character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_SOSP            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_CHIUSA          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_ANNULL          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_INS_LINEA_OFFERTA_BW         character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_AGG_LINEA_OFFERTA_BW         character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_INTERAZIONE                              bigint                    not null  default 0
)
DISTRIBUTE ON (PK_P4C_ATTIVAZIONI)
;

/*
       Number of columns  196
 
    (Variable) Data Size  737 - 17237
            Row Overhead  55
  ======================  =============
  Total Row Size (bytes)  792 - 17292
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ANAG_CODA"

CREATE TABLE  T_DMT_P4C_DM_ANAG_CODA
(
     PK_P4C_ANAG_CODA                  bigint                    not null,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     CDN_MASTER                        bigint                    not null  default 0,
     DTA_INSERIMENTO                   timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     LDS_CODA                          character varying(255)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_P4C_ANAG_CODA)
;

/*
       Number of columns  14
 
    (Variable) Data Size  92 - 348
            Row Overhead  28
  ======================  =============
  Total Row Size (bytes)  120 - 376
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ANAG_GA"

CREATE TABLE  T_DMT_P4C_DM_ANAG_GA
(
     PK_P4C_ANAG_GA                    bigint                             not null,
     DTA_INIZIO_VALIDITA               timestamp                          not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                          not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                            not null  default 1,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                             not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                             not null  default 0,
     CDN_MASTER                        bigint                             not null  default 0,
     DTA_INSERIMENTO                   timestamp                          not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                          not null  default "TIMESTAMP"('now(0)'::"VARCHAR"),
     FK_UTENTE_INSERIMENTO             bigint                             not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                             not null  default -1,
     FLN_CANC_FISICA                   byteint                            not null  default 2,
     DTA_CANC_FISICA                   timestamp                          not null  default '2999-12-31'::DATE,
     XN0_CODICE_GA                     national character varying(500)    not null  default '***'::"NVARCHAR",
     CDC_PARTNER                       character varying(50)              not null  default '***'::"NVARCHAR",
     CDC_SOCIETA_PARTNER               character varying(50)              not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_P4C_ANAG_GA)
;

/*
       Number of columns  16
 
    (Variable) Data Size  96 - 2196
            Row Overhead  28
  ======================  =============
  Total Row Size (bytes)  124 - 2224
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_CASE_ITEM"

CREATE TABLE  T_DMT_P4C_DM_CASE_ITEM
(
     FK_IDN_AUDIT_PROGRAMMA              bigint                    not null  default 0,
     PK_P4C_CASE_ITEM                    bigint                    not null  default 0,
     CDN_MASTER                          bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO               bigint                    not null  default 0,
     DTA_INSERIMENTO                     timestamp                 not null  default '1900-01-01'::DATE,
     FK_UTENTE_AGGIORNAMENTO             bigint                    not null  default 0,
     DTA_AGGIORNAMENTO                   timestamp                 not null  default '1900-01-01'::DATE,
     DTA_INIZIO_VALIDITA                 timestamp                 not null  default '1900-01-01'::DATE,
     DTA_FINE_VALIDITA                   timestamp                 not null  default '1900-01-01'::DATE,
     FLN_VALIDITA                        byteint                   not null  default 0,
     DTA_CANC_FISICA                     timestamp                 not null  default '1900-01-01'::DATE,
     FLN_CANC_FISICA                     byteint                   not null  default 0,
     IDC_ID_KEY_CITEM                    character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_STATO_CITEM                     character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_NOME_CITEM                      character varying(120)    not null  default '***'::"NVARCHAR",
     MDS_TIPO_CLIENTE                    character varying(120)    not null  default '***'::"NVARCHAR",
     CDC_SEGMENTO_CLIENTE                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_POD_CITEM                       character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_MENSOLA_GAS                character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPO_RECORD_CITEM               character varying(120)    not null  default '***'::"NVARCHAR",
     MDS_LOGIN_UTENTE_INS_CASE           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_CASE        bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_CASE           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_CASE        bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_INS_CASEITEM       character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_CITEM       bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_CASEITEM       character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_CITEM       bigint                    not null  default 0,
     CDC_TIPO_SORGENTE                   character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_CITEM                 timestamp                 not null  default '1900-01-01'::DATE,
     DTA_AGGIORNAMENTO_CITEM             timestamp                 not null  default '1900-01-01'::DATE,
     CDC_STATO_UDB_CITEM                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_ANNULLAMENTO_CITEM      character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ID_INTERAZIONE                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_INTERAZIONE                character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_CHIAMATA_INTERAZ         numeric(22,7),
     DTA_CREAZIONE_INTERAZ               timestamp                 not null  default '1900-01-01'::DATE,
     IDC_ID_CASE                         character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_CASE                       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_STATO_RICHIESTA                 character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SUBSTATO_CASE                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_CANCELLAZIONE_CASE      character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_PROCESSO_CASE                   character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CODICE_FISCALE                  character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CODICE_CLIENTE                  character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SITO                         bigint                    not null  default 0,
     FK_PARTNER_INS_CASEITEM             bigint                    not null  default 0,
     LDS_DESC_TRIPLETTA                  character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_VAS                    character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CALL_ID                         character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_INTER                    character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_CLIENTE                      bigint                    not null  default 0,
     QTA_DURATA                          bigint,
     FK_CDR_INBOUND                      bigint                    not null  default 0,
     FK_CDR_CHAT                         bigint                    not null  default 0,
     FK_CDR_OUTBOUND                     bigint                    not null  default 0,
     LDS_CODA                            character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_PIATTAFORMA                     character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO                 character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                         character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                      character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                      character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SOTTOCANALE_INS_CASEITEM     bigint                    not null  default 0,
     SDS_SOTTOCANALE_INS_CASEITEM        character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_INS_CASEITEM            character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INS_CASE            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_INS_CASE                character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_CASE            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_AGG_CASE                character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_CASEITEM        character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_AGG_CASEITEM            character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_RICHIESTA                    bigint                    not null  default 0,
     SK_IDN_INTERAZIONE                  bigint                    not null  default 0
)
DISTRIBUTE ON (PK_P4C_CASE_ITEM)
;

/*
       Number of columns  74
 
    (Variable) Data Size  322 - 5896
            Row Overhead  38 - 36
  ======================  =============
  Total Row Size (bytes)  360 - 5932
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_CASE_ITEM_LOAD"

CREATE TABLE  T_DMT_P4C_DM_CASE_ITEM_LOAD
(
     FK_IDN_AUDIT_PROGRAMMA              bigint                    not null  default 0,
     PK_P4C_CASE_ITEM                    bigint                    not null  default 0,
     CDN_MASTER                          bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO               bigint                    not null  default 0,
     DTA_INSERIMENTO                     timestamp                 not null  default '1900-01-01'::DATE,
     FK_UTENTE_AGGIORNAMENTO             bigint                    not null  default 0,
     DTA_AGGIORNAMENTO                   timestamp                 not null  default '1900-01-01'::DATE,
     DTA_INIZIO_VALIDITA                 timestamp                 not null  default '1900-01-01'::DATE,
     DTA_FINE_VALIDITA                   timestamp                 not null  default '1900-01-01'::DATE,
     FLN_VALIDITA                        byteint                   not null  default 0,
     DTA_CANC_FISICA                     timestamp                 not null  default '1900-01-01'::DATE,
     FLN_CANC_FISICA                     byteint                   not null  default 0,
     IDC_ID_KEY_CITEM                    character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_STATO_CITEM                     character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_NOME_CITEM                      character varying(120)    not null  default '***'::"NVARCHAR",
     MDS_TIPO_CLIENTE                    character varying(120)    not null  default '***'::"NVARCHAR",
     CDC_SEGMENTO_CLIENTE                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_POD_CITEM                       character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_MENSOLA_GAS                character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPO_RECORD_CITEM               character varying(120)    not null  default '***'::"NVARCHAR",
     MDS_LOGIN_UTENTE_INS_CASE           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_CASE        bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_CASE           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_CASE        bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_INS_CASEITEM       character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_CITEM       bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_CASEITEM       character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_CITEM       bigint                    not null  default 0,
     CDC_TIPO_SORGENTE                   character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_CITEM                 timestamp                 not null  default '1900-01-01'::DATE,
     DTA_AGGIORNAMENTO_CITEM             timestamp                 not null  default '1900-01-01'::DATE,
     CDC_STATO_UDB_CITEM                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_ANNULLAMENTO_CITEM      character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ID_INTERAZIONE                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_INTERAZIONE                character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_CHIAMATA_INTERAZ         numeric(22,7),
     DTA_CREAZIONE_INTERAZ               timestamp                 not null  default '1900-01-01'::DATE,
     IDC_ID_CASE                         character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_CASE                       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_STATO_RICHIESTA                 character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SUBSTATO_CASE                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_CANCELLAZIONE_CASE      character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_PROCESSO_CASE                   character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CODICE_FISCALE                  character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CODICE_CLIENTE                  character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SITO                         bigint                    not null  default 0,
     FK_PARTNER_INS_CASEITEM             bigint                    not null  default 0,
     LDS_DESC_TRIPLETTA                  character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_VAS                    character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CALL_ID                         character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_INTER                    character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_CLIENTE                      bigint                    not null  default 0,
     QTA_DURATA                          bigint,
     FK_CDR_INBOUND                      bigint                    not null  default 0,
     FK_CDR_CHAT                         bigint                    not null  default 0,
     FK_CDR_OUTBOUND                     bigint                    not null  default 0,
     LDS_CODA                            character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_PIATTAFORMA                     character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO                 character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                         character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                      character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                      character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SOTTOCANALE_INS_CASEITEM     bigint                    not null  default 0,
     SDS_SOTTOCANALE_INS_CASEITEM        character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_INS_CASEITEM            character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INS_CASE            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_INS_CASE                character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_CASE            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_AGG_CASE                character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_CASEITEM        character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_AGG_CASEITEM            character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_RICHIESTA                    bigint                    not null  default 0,
     SK_IDN_INTERAZIONE                  bigint                    not null  default 0
)
DISTRIBUTE ON (PK_P4C_CASE_ITEM)
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_DM_CASE_ITEM_LOAD
ALTER TABLE T_DMT_P4C_DM_CASE_ITEM_LOAD ADD Constraint PK_P4C_CASE_ITEM PRIMARY KEY (PK_P4C_CASE_ITEM);

/*
       Number of columns  74
 
    (Variable) Data Size  322 - 5896
            Row Overhead  38 - 36
  ======================  =============
  Total Row Size (bytes)  360 - 5932
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ATTIVITA"

CREATE TABLE  T_DMT_P4C_DM_ATTIVITA
(
     FK_IDN_AUDIT_PROGRAMMA             bigint                    not null  default 0,
     PK_P4C_ATTIVITA                    bigint                    not null  default 0,
     CDN_MASTER                         bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO              bigint                    not null  default 0,
     DTA_INSERIMENTO                    timestamp                 not null,
     FK_UTENTE_AGGIORNAMENTO            bigint                    not null  default 0,
     DTA_AGGIORNAMENTO                  timestamp                 not null,
     DTA_INIZIO_VALIDITA                timestamp                 not null,
     DTA_FINE_VALIDITA                  timestamp                 not null,
     FLN_VALIDITA                       byteint                   not null  default 0,
     DTA_CANC_FISICA                    timestamp                 not null,
     FLN_CANC_FISICA                    byteint                   not null  default 0,
     IDC_ID_KEY_ATTIVITA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_STATO_ATTIVITA                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_COMMODITY                      character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPO_CLIENTE                   character varying(120)    not null  default '***'::"NVARCHAR",
     CDC_POD                            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_ATTIVITA                  character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_ATTIVITA             character varying(120)    not null  default '***'::"NVARCHAR",
     LDS_FAMIGLIA                       character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_SPECIFICA                      character varying(120)    not null  default '***'::"NVARCHAR",
     CDC_SERVIZIO_CALC                  character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_LOGIN_INS                      character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS            bigint                    not null  default 0,
     MDS_LOGIN_OWNER                    character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_OWNER          bigint                    not null  default 0,
     MDS_LOGIN_AGG                      character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG            bigint                    not null  default 0,
     DTA_INSERIMENTO_RO                 timestamp                 not null,
     DTA_AGGIORNAMENTO_RO               timestamp                 not null,
     DTA_TERMINE                        timestamp                 not null,
     DTA_INIZIO_ATTIVITA                timestamp                 not null,
     DTA_PRIMA_ASSEGNAZIONE             timestamp                 not null,
     DTA_ULTIMA_ASSEGNAZIONE            timestamp                 not null,
     DTA_ULTIMO_FATTO                   timestamp                 not null,
     IDC_ID_KEY_RICHIESTE               character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PROCESSO                       character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_STATO_RICHIESTA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SUBSTATO_RICHIESTA             character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_CANCELLAZIONE          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_FISCALE                        character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CLIENTE                        character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ID_KEY_OFF                     character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_INTERAZIONE                 bigint                    not null  default 0,
     IDC_ID_KEY_INTERAZIONE             character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_ATTIVITA                  character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_CHIAMATA                numeric(22,7),
     DTA_INSERIMENTO_RO_INTERAZIONE     timestamp                 not null,
     CDC_CODA_TELEFONICA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SOTTOCODA_TELEFONICA           character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_TIPO_RECORD_ATTIVITA           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER                bigint                    not null  default 0,
     CDC_BUSINESS_PARTNER               character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_SORGENTE                  character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SITO                        bigint                    not null  default 0,
     CDC_TIPO                           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_VAS                   character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_CLIENTE                     bigint                    not null  default 0,
     CDC_SEGMENTO_CLIENTE               character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CALL_ID                        character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_INTERAZ                 character varying(255)    not null  default '***'::"NVARCHAR",
     QTA_DURATA                         bigint,
     FK_CDR_INBOUND                     bigint                    not null  default 0,
     FK_CDR_CHAT                        bigint                    not null  default 0,
     FK_CDR_OUTBOUND                    bigint                    not null  default 0,
     LDS_CODA                           character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_SOTTOCANALE_INS             bigint                    not null  default 0,
     SDS_SOTTOCANALE_INS                character varying(50)     not null  default '***'::"NVARCHAR",
     FK_PARTNER_INS                     bigint                    not null  default 0,
     CDC_AGENZIA_INS                    character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_OWNER              character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_OWNER                  character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_AGG                    character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_DOC_ALLEGATO                   byteint                   not null  default 0,
     LDS_PIATTAFORMA                    character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO                character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                        character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                     character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_ID_CORRISPONDENZA              character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_RICHIESTA                   bigint                    not null  default 0,
     LDS_FAMIGLIA_RECLAMI               character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_FAMIGLIA_ATTIVITA              character varying(255)    not null  default '***'::"NVARCHAR",
     FK_PARTNER_AGG                     bigint                    not null  default 0
)
DISTRIBUTE ON (PK_P4C_ATTIVITA)
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_DM_ATTIVITA
ALTER TABLE T_DMT_P4C_DM_ATTIVITA ADD Constraint PK_P4C_ATTIVITA PRIMARY KEY (PK_P4C_ATTIVITA);

/*
       Number of columns  86
 
    (Variable) Data Size  381 - 6617
            Row Overhead  43
  ======================  =============
  Total Row Size (bytes)  424 - 6660
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ATTIVAZIONI"

CREATE TABLE  T_DMT_P4C_DM_ATTIVAZIONI
(
     FK_IDN_AUDIT_PROGRAMMA                          bigint                    not null  default 0,
     PK_P4C_ATTIVAZIONI                              bigint                    not null  default 0,
     CDN_MASTER                                      bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO                           bigint                    not null  default 0,
     DTA_INSERIMENTO                                 timestamp                 not null,
     FK_UTENTE_AGGIORNAMENTO                         bigint                    not null  default 0,
     DTA_AGGIORNAMENTO                               timestamp                 not null,
     DTA_INIZIO_VALIDITA                             timestamp                 not null,
     DTA_FINE_VALIDITA                               timestamp                 not null,
     FLN_VALIDITA                                    byteint                   not null  default 0,
     DTA_CANC_FISICA                                 timestamp                 not null,
     FLN_CANC_FISICA                                 byteint                   not null  default 0,
     DTA_RIFERIMENTO_FLUSSO                          timestamp                 not null,
     LDS_CAUSALE_OPERAZIONE                          character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CASO_REMUNERAZIONE                          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CASO_REMUNERAZIONE_SFC                      character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CASO_REMUNERAZIONE_OLD                      character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_COD_AGENTE                                  character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA                              character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_EFFETTO                                     timestamp                 not null,
     DTA_INIZIO_TIMING                               timestamp                 not null,
     DTA_FINE_TIMING                                 timestamp                 not null,
     IDC_ROW_ID_OFFERTA                              character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_OFFERTA_OLD                          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_NUMERO_OFFERTA                              character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_OFFERTA                           timestamp                 not null,
     DTA_ULT_MOD_OFFERTA                             timestamp                 not null,
     LDS_STATO_OFFERTA_SFC                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_STATO_OFFERTA                               character varying(255)    not null  default '***'::"NVARCHAR",
     FLN_DOCUMENTO_ARCHIVIATO                        byteint                   not null  default 0,
     LDS_CAUSALE_STATO_OFFERTA                       character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_POD_OFFERTA                                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPOLOGIA_OFFERTA                           character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_OFFERTA                         character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_OFFERTA_OLD                     character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_RIGA_OFFERTA                      timestamp                 not null,
     DTA_ULT_MOD_RIGA_OFFERTA                        timestamp                 not null,
     LDS_STATO_RIGA_OFFERTA                          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_STATO_RIGA_OFFERTA                  character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_RIGA_OFFERTA                      character varying(120)    not null  default '***'::"NVARCHAR",
     FLN_CANCELLAZIONE_RIGA_OFFERTA                  byteint                   not null  default 0,
     IDC_ROW_ID_ORDINE                               character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_ORDINE_OLD                           character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_ORDINE                            timestamp                 not null,
     DTA_ULT_MOD_ORDINE                              timestamp                 not null,
     CDC_POD_ORDINE                                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPOLOGIA_ORDINE                            character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_ORDINE                          character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_ORDINE_OLD                      character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_RIGA_ORDINE                       timestamp                 not null,
     DTA_ULT_MOD_RIGA_ORDINE                         timestamp                 not null,
     LDS_STATO_RIGA_ORDINE                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_STATO_RIGA_ORDINE                   character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_RIGA_ORDINE                       character varying(120)    not null  default '***'::"NVARCHAR",
     FLN_CANCELLAZIONE_RIGA_ORDINE                   byteint                   not null  default 0,
     DTA_RILAVORAZIONE_COMMERCIALE                   timestamp                 not null,
     FLN_RILAVORAZIONE_COMMERCIALE                   byteint                   not null  default 0,
     CDC_STATO_RID                                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_SERVIZIO                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_NOME_PRODOTTO_SERVIZIO                      character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_DESCRIZIONE_PRODOTTO_SERVIZIO               character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_ATTIVAZIONE_SERVIZIO                        timestamp                 not null,
     LDS_STATO_SERVIZIO                              character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_CESSAZIONE_SERVIZIO                         timestamp                 not null,
     LDS_STATO_TRASPORTO                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CAP_PRODOTTO_SERVIZIO                       character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_COMUNE_PRODOTTO_SERVIZIO                    character varying(255)    not null  default '***'::"NVARCHAR",
     SDS_PROVINCIA_PRODOTTO                          character varying(50)     not null  default '***'::"NVARCHAR",
     VAL_TOT_POT_CONTRATTUALE_SITO                   numeric(22,7),
     VAL_TOT_POTENZA_DISPONIBILE                     numeric(22,7),
     FLN_OPZIONE_GREEN_PRODOTTO                      byteint                   not null  default 0,
     LDS_PIANO_PROVVIGIONALE_PROD                    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_TIPO_UTILIZZO_PRODOTTO                      character varying(255)    not null  default '***'::"NVARCHAR",
     FLC_RESIDENTE                                   character(1)              not null  default '*'::"NVARCHAR",
     LDS_TIPO_SERVIZIO_PRODOTTO                      character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_CLIENTE                              character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_CLIENTE_OLD                          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_BUSINESS_PARTNER                            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPOLOGIA_CLIENTE                           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_FISCALE_CLIENTE                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_PART_IVA_CLIENTE                            character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_RAGIONE_SOCIALE_CLIENTE                     character varying(120)    not null  default '***'::"NVARCHAR",
     LDS_FORMA_GIURIDICA                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CAP_CLIENTE                                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_COMUNE_CLIENTE                              character varying(255)    not null  default '***'::"NVARCHAR",
     SDS_SIGLA_PROVINCIA_CLIENTE                     character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_CONTATTO_VOCAL                              byteint                   not null  default 0,
     CDC_CANALE                                      character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_RID_IN_QC                                   byteint                   not null  default 0,
     DTA_ST_RICEVUTA                                 timestamp                 not null,
     DTA_ST_CHIUSA                                   timestamp                 not null,
     CDC_AGENZIA_BOLLETTA_WEB                        character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CATEGORIA_USO                               character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_MERCATO                                     character varying(255)    not null  default '***'::"NVARCHAR",
     FLN_BOLLETTA_WEB                                byteint                   not null  default 0,
     CDC_STATO_BOLLETTA_WEB                          character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_CROSS_SELLING                               byteint                   not null  default 0,
     IDC_ROW_ID_SITO                                 character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_SITO_OLD                             character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_INSERIMENTO_SDD                             timestamp                 not null  default '01-01-1900 00:00:00',
     LDS_FASE_INS_SDD                                character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_SOTTOCANALE_SDD                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_SDD                                 character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_BOLLETTA_WEB_IN_QC                          byteint                   not null  default 0,
     IDC_ROW_ID_INTERAZ                              character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_INTERAZ                                character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_CHIAMATA_INTERAZ                     numeric(22,7),
     DTA_CREAZ_INTERAZ                               timestamp                 not null  default '01-01-1900 00:00:00',
     IDN_SOTTOCANALE_ATTIVAZ_SDD                     bigint                    not null  default 0,
     LDS_CANALE_INVIO_CONTRATTO                      character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_MODALITA_FIRMA                              character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_ACQUISITIVO                 bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_INS_OFFERTA                    character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_OFFERTA                 bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_OFFERTA                    character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_OFFERTA                 bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_INS_LINEA_OFFERTA_FORN         character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_LINEA_OFFERTA_FORN      bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_LINEA_OFFERTA_FORN         character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_LINEA_OFFERTA_FORN      bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_RICEV             character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_RICEV          bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_DA_CONFERM        character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_DA_CONFERM     bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_SOSP              character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_SOSP           bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_CHIUSA            character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_CHIUSA         bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_ANNULL            character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_ANNULL         bigint                    not null  default 0,
     FLN_QC_CHIAMATA_CONCLUSA                        byteint                   not null  default 0,
     MDS_LOGIN_UTENTE_INS_LINEA_OFFERTA_BW           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_LINEA_OFFERTA_BW        bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_LINEA_OFFERTA_BW           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_LINEA_OFFERTA_BW        bigint                    not null  default 0,
     CDC_CODA_TELEFONICA                             character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SOTTOCODA_TELEFONICA                        character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ID_CASE                                     character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INTERAZ                     bigint                    not null  default 0,
     LDS_CONSENSO_MARKET_TELEFONO                    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_MARKET_EMAIL                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_MARKET_CELL                        character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_PROFILAZIONE                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_TERZI_TEL                          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_TERZI_EMAIL                        character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_TERZI_CELL                         character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_CLIENTE                                  bigint                    not null  default 0,
     SK_IDN_SITO                                     bigint                    not null  default 0,
     CDC_CALL_ID                                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE                                      character varying(255)    not null  default '***'::"NVARCHAR",
     QTA_DURATA                                      bigint,
     FK_CDR_INBOUND                                  bigint                    not null  default 0,
     FK_CDR_CHAT                                     bigint                    not null  default 0,
     FK_CDR_OUTBOUND                                 bigint                    not null  default 0,
     LDS_CODA    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_INS_OFFERTA                         character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_PARTNER_INS_OFFERTA                      bigint                    not null  default 0,
     SDS_SOTTOCANALE_INS_OFFERTA                     character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_OFFERTA                     character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INS_LINEA_OFFERTA_FORN          character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_LINEA_OFFERTA_FORN          character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_RICEV              character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_DA_CONFERM         character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_SOSP               character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_CHIUSA             character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_ANNULL             character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INS_LINEA_OFFERTA_BW            character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_LINEA_OFFERTA_BW            character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INTERAZ                         character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SOTTOCANALE_INS_OFF                      bigint                    not null  default 0,
     FLN_RID_OBBLIGATORIO                            byteint                   not null  default 0,
     LDS_PIATTAFORMA                                 character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                               character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                                     character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                                  character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PROCESSO_CASE                               character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_STATO_RICHIESTA_CASE                        character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SUBSTATO_RICHIESTA_CASE                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_CANCELLAZIONE_CASE                  character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CASE                                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_VAS_CASE                           character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_RICHIESTA                                bigint                    not null  default 0,
     CDC_STATO_UDB_CITEM                             character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_AGG_OFFERTA                  character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_INS_LINEA_OFFERTA_FORN       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_AGG_LINEA_OFFERTA_FORN       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_RICEV           character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_DA_CONFERM      character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_SOSP            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_CHIUSA          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_ANNULL          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_INS_LINEA_OFFERTA_BW         character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_AGG_LINEA_OFFERTA_BW         character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_INTERAZIONE                              bigint                    not null  default 0,
     DTA_ST_PRIMO_ANN                                timestamp                 not null,
     LDS_TIPO_USO                                    character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_INV             character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_INV                character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_ST_PRIMO_INV                                timestamp                 not null  default '01-01-1900 00:00:00',
     DTA_ST_PRIMO_SOS                                timestamp                 not null  default '01-01-1900 00:00:00',
     DTA_ST_PRIMO_CDC                                timestamp                 not null  default '01-01-1900 00:00:00'
)
DISTRIBUTE ON (CDC_CASO_REMUNERAZIONE)
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_DM_ATTIVAZIONI
ALTER TABLE T_DMT_P4C_DM_ATTIVAZIONI ADD Constraint PK_P4C_ATTIVAZIONI PRIMARY KEY (PK_P4C_ATTIVAZIONI);

/*
       Number of columns  203
 
    (Variable) Data Size  775 - 17631
            Row Overhead  53
  ======================  =============
  Total Row Size (bytes)  828 - 17684
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ATTIVITA_FOTO_I4P"

CREATE TABLE  T_DMT_P4C_DM_ATTIVITA_FOTO_I4P
(
     FK_IDN_AUDIT_PROGRAMMA             bigint                    not null  default 0,
     PK_P4C_ATTIVITA                    bigint                    not null  default 0,
     CDN_MASTER                         bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO              bigint                    not null  default 0,
     DTA_INSERIMENTO                    timestamp                 not null,
     FK_UTENTE_AGGIORNAMENTO            bigint                    not null  default 0,
     DTA_AGGIORNAMENTO                  timestamp                 not null,
     DTA_INIZIO_VALIDITA                timestamp                 not null,
     DTA_FINE_VALIDITA                  timestamp                 not null,
     FLN_VALIDITA                       byteint                   not null  default 0,
     DTA_CANC_FISICA                    timestamp                 not null,
     FLN_CANC_FISICA                    byteint                   not null  default 0,
     IDC_ID_KEY_ATTIVITA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_STATO_ATTIVITA                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_COMMODITY                      character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPO_CLIENTE                   character varying(120)    not null  default '***'::"NVARCHAR",
     CDC_POD                            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_ATTIVITA                  character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_ATTIVITA             character varying(120)    not null  default '***'::"NVARCHAR",
     LDS_FAMIGLIA                       character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_SPECIFICA                      character varying(120)    not null  default '***'::"NVARCHAR",
     CDC_SERVIZIO_CALC                  character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_LOGIN_INS                      character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS            bigint                    not null  default 0,
     MDS_LOGIN_OWNER                    character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_OWNER          bigint                    not null  default 0,
     MDS_LOGIN_AGG                      character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG            bigint                    not null  default 0,
     DTA_INSERIMENTO_RO                 timestamp                 not null,
     DTA_AGGIORNAMENTO_RO               timestamp                 not null,
     DTA_TERMINE                        timestamp                 not null,
     DTA_INIZIO_ATTIVITA                timestamp                 not null,
     DTA_PRIMA_ASSEGNAZIONE             timestamp                 not null,
     DTA_ULTIMA_ASSEGNAZIONE            timestamp                 not null,
     DTA_ULTIMO_FATTO                   timestamp                 not null,
     IDC_ID_KEY_RICHIESTE               character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PROCESSO                       character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_STATO_RICHIESTA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SUBSTATO_RICHIESTA             character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_CANCELLAZIONE          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_FISCALE                        character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CLIENTE                        character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ID_KEY_OFF                     character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_INTERAZIONE                 bigint                    not null  default 0,
     IDC_ID_KEY_INTERAZIONE             character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_ATTIVITA                  character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_CHIAMATA                numeric(22,7),
     DTA_INSERIMENTO_RO_INTERAZIONE     timestamp                 not null,
     CDC_CODA_TELEFONICA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SOTTOCODA_TELEFONICA           character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_TIPO_RECORD_ATTIVITA           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER                bigint                    not null  default 0,
     CDC_BUSINESS_PARTNER               character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_SORGENTE                  character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SITO                        bigint                    not null  default 0,
     CDC_TIPO                           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_VAS                   character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_CLIENTE                     bigint                    not null  default 0,
     CDC_SEGMENTO_CLIENTE               character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CALL_ID                        character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_INTERAZ                 character varying(255)    not null  default '***'::"NVARCHAR",
     QTA_DURATA                         bigint,
     FK_CDR_INBOUND                     bigint                    not null  default 0,
     FK_CDR_CHAT                        bigint                    not null  default 0,
     FK_CDR_OUTBOUND                    bigint                    not null  default 0,
     LDS_CODA                           character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_SOTTOCANALE_INS             bigint                    not null  default 0,
     SDS_SOTTOCANALE_INS                character varying(50)     not null  default '***'::"NVARCHAR",
     FK_PARTNER_INS                     bigint                    not null  default 0,
     CDC_AGENZIA_INS                    character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_OWNER              character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_OWNER                  character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_AGG                    character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_DOC_ALLEGATO                   byteint                   not null  default 0,
     LDS_PIATTAFORMA                    character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO                character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                        character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                     character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_ID_CORRISPONDENZA              character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_RICHIESTA                   bigint                    not null  default 0,
     LDS_FAMIGLIA_RECLAMI               character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_FAMIGLIA_ATTIVITA              character varying(255)    not null  default '***'::"NVARCHAR"
)
DISTRIBUTE ON (PK_P4C_ATTIVITA)
;

/*
       Number of columns  85
 
    (Variable) Data Size  373 - 6609
            Row Overhead  43
  ======================  =============
  Total Row Size (bytes)  416 - 6652
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_CASE_ITEM_FOTO_I4P"

CREATE TABLE  T_DMT_P4C_DM_CASE_ITEM_FOTO_I4P
(
     FK_IDN_AUDIT_PROGRAMMA              bigint                    not null  default 0,
     PK_P4C_CASE_ITEM                    bigint                    not null  default 0,
     CDN_MASTER                          bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO               bigint                    not null  default 0,
     DTA_INSERIMENTO                     timestamp                 not null  default '01-01-1900',
     FK_UTENTE_AGGIORNAMENTO             bigint                    not null  default 0,
     DTA_AGGIORNAMENTO                   timestamp                 not null  default '01-01-1900',
     DTA_INIZIO_VALIDITA                 timestamp                 not null  default '01-01-1900',
     DTA_FINE_VALIDITA                   timestamp                 not null  default '01-01-1900',
     FLN_VALIDITA                        byteint                   not null  default 0,
     DTA_CANC_FISICA                     timestamp                 not null  default '01-01-1900',
     FLN_CANC_FISICA                     byteint                   not null  default 0,
     IDC_ID_KEY_CITEM                    character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_STATO_CITEM                     character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_NOME_CITEM                      character varying(120)    not null  default '***'::"NVARCHAR",
     MDS_TIPO_CLIENTE                    character varying(120)    not null  default '***'::"NVARCHAR",
     CDC_SEGMENTO_CLIENTE                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_POD_CITEM                       character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_MENSOLA_GAS                character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPO_RECORD_CITEM               character varying(120)    not null  default '***'::"NVARCHAR",
     MDS_LOGIN_UTENTE_INS_CASE           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_CASE        bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_CASE           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_CASE        bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_INS_CASEITEM       character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_CITEM       bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_CASEITEM       character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_CITEM       bigint                    not null  default 0,
     CDC_TIPO_SORGENTE                   character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_CITEM                 timestamp                 not null  default '01-01-1900',
     DTA_AGGIORNAMENTO_CITEM             timestamp                 not null  default '01-01-1900',
     CDC_STATO_UDB_CITEM                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_ANNULLAMENTO_CITEM      character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ID_INTERAZIONE                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_INTERAZIONE                character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_CHIAMATA_INTERAZ         numeric(22,7),
     DTA_CREAZIONE_INTERAZ               timestamp                 not null  default '01-01-1900',
     IDC_ID_CASE                         character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_CASE                       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_STATO_RICHIESTA                 character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SUBSTATO_CASE                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_CANCELLAZIONE_CASE      character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_PROCESSO_CASE                   character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CODICE_FISCALE                  character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CODICE_CLIENTE                  character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SITO                         bigint                    not null  default 0,
     FK_PARTNER_INS_CASEITEM             bigint                    not null  default 0,
     LDS_DESC_TRIPLETTA                  character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_VAS                    character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CALL_ID                         character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_INTER                    character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_CLIENTE                      bigint                    not null  default 0,
     QTA_DURATA                          bigint,
     FK_CDR_INBOUND                      bigint                    not null  default 0,
     FK_CDR_CHAT                         bigint                    not null  default 0,
     FK_CDR_OUTBOUND                     bigint                    not null  default 0,
     LDS_CODA                            character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_PIATTAFORMA                     character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO                 character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                         character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                      character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                      character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SOTTOCANALE_INS_CASEITEM     bigint                    not null  default 0,
     SDS_SOTTOCANALE_INS_CASEITEM        character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_INS_CASEITEM            character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INS_CASE            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_INS_CASE                character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_CASE            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_AGG_CASE                character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_CASEITEM        character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_AGG_CASEITEM            character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_RICHIESTA                    bigint                    not null  default 0,
     SK_IDN_INTERAZIONE                  bigint                    not null  default 0
)
DISTRIBUTE ON (PK_P4C_CASE_ITEM)
;

/*
       Number of columns  74
 
    (Variable) Data Size  322 - 5896
            Row Overhead  38 - 36
  ======================  =============
  Total Row Size (bytes)  360 - 5932
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_LM_CONFIG_CASE_ITEM"

CREATE TABLE  T_DMT_P4C_LM_CONFIG_CASE_ITEM
(
     PK_CONFIG_CASE_ITEM               bigint                    not null,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_MATRICOLA_UTENTE              character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_TIPO_OPERAZIONE               character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_RICHIESTA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_RIGA_RICHIESTA           character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_COMMODITY                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_DESC_TRIPLETTA                character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_START_DATE                    timestamp                 not null  default '1900-01-01'::DATE,
     FLN_ATTIVO                        byteint                   not null  default 1,
     FLN_COMMISSIONING                 byteint                   not null  default 1
)
DISTRIBUTE ON RANDOM
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_LM_CONFIG_CASE_ITEM
ALTER TABLE T_DMT_P4C_LM_CONFIG_CASE_ITEM ADD Constraint PK_CONFIG_CASE_ITEM PRIMARY KEY (PK_CONFIG_CASE_ITEM);

/*
       Number of columns  23
 
    (Variable) Data Size  108 - 1126
            Row Overhead  28 - 30
  ======================  =============
  Total Row Size (bytes)  136 - 1156
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_LM_CONFIG_BLKLST_ATT"

CREATE TABLE  T_DMT_P4C_LM_CONFIG_BLKLST_ATT
(
     PK_CONFIG_BLKLST_ATT              bigint                    not null,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_MATRICOLA_UTENTE              character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_TIPO_OPERAZIONE               character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_ATTIVITA                 character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_ATTIVITA            character varying(120)    not null  default '***'::"NVARCHAR",
     LDS_FAMIGLIA                      character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_SPECIFICA                     character varying(120)    not null  default '***'::"NVARCHAR",
     DTA_START_DATE                    timestamp                 not null  default '1900-01-01'::DATE,
     FLN_ATTIVO                        byteint                   not null  default 1,
     FLN_COMMISSIONING                 byteint                   not null  default 1
)
DISTRIBUTE ON RANDOM
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_LM_CONFIG_BLKLST_ATT
ALTER TABLE T_DMT_P4C_LM_CONFIG_BLKLST_ATT ADD Constraint PK_CONFIG_BLKLST_ATT PRIMARY KEY (PK_CONFIG_BLKLST_ATT);

/*
       Number of columns  23
 
    (Variable) Data Size  108 - 1266
            Row Overhead  28 - 30
  ======================  =============
  Total Row Size (bytes)  136 - 1296
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_LM_CONFIG_ATTIVITA"

CREATE TABLE  T_DMT_P4C_LM_CONFIG_ATTIVITA
(
     PK_CONFIG_ATTIVITA                bigint                    not null,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_MATRICOLA_UTENTE              character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_TIPO_OPERAZIONE               character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_ATTIVITA                 character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_ATTIVITA            character varying(120)    not null  default '***'::"NVARCHAR",
     LDS_FAMIGLIA                      character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_SPECIFICA                     character varying(120)    not null  default '***'::"NVARCHAR",
     DTA_START_DATE                    timestamp                 not null  default '1900-01-01'::DATE,
     FLN_ATTIVO                        byteint                   not null  default 1,
     FLN_COMMISSIONING                 byteint                   not null  default 1
)
DISTRIBUTE ON RANDOM
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_LM_CONFIG_ATTIVITA
ALTER TABLE T_DMT_P4C_LM_CONFIG_ATTIVITA ADD Constraint PK_CONFIG_ATTIVITA PRIMARY KEY (PK_CONFIG_ATTIVITA);

/*
       Number of columns  23
 
    (Variable) Data Size  108 - 1266
            Row Overhead  28 - 30
  ======================  =============
  Total Row Size (bytes)  136 - 1296
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_LM_CONFIG_ATTIVAZIONE"

CREATE TABLE  T_DMT_P4C_LM_CONFIG_ATTIVAZIONE
(
     PK_CONFIG_ATTIVAZIONE             bigint                    not null,
     DTA_INIZIO_VALIDITA               timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_FINE_VALIDITA                 timestamp                 not null  default '2999-12-31'::DATE,
     FLN_VALIDITA                      byteint                   not null  default 1,
     FLN_CANC_FISICA                   byteint                   not null  default 2,
     DTA_CANC_FISICA                   timestamp                 not null  default '2999-12-31'::DATE,
     FK_IDN_AUDIT_PROGRAMMA_INSERT     bigint                    not null  default 0,
     FK_IDN_AUDIT_PROGRAMMA_UPDATE     bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO             bigint                    not null  default -1,
     FK_UTENTE_AGGIORNAMENTO           bigint                    not null  default -1,
     DTA_INSERIMENTO                   timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     DTA_AGGIORNAMENTO                 timestamp                 not null  default DATE('now(0)'::"VARCHAR"),
     CDC_SISTEMA_PROVENIENZA           character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_MATRICOLA_UTENTE              character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_TIPO_OPERAZIONE               character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONFIG                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE                       character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_START_DATE                    timestamp                 not null  default '1900-01-01'::DATE,
     FLN_ATTIVO                        byteint                   not null  default 1,
     FLN_COMMISSIONING                 byteint                   not null  default 1
)
DISTRIBUTE ON RANDOM
;

\echo
\echo *****  Adding Primary Key Constraint:  T_DMT_P4C_LM_CONFIG_ATTIVAZIONE
ALTER TABLE T_DMT_P4C_LM_CONFIG_ATTIVAZIONE ADD Constraint PK_CONFIG_ATTIVAZIONE PRIMARY KEY (PK_CONFIG_ATTIVAZIONE);

/*
       Number of columns  21
 
    (Variable) Data Size  104 - 1022
            Row Overhead  28 - 30
  ======================  =============
  Total Row Size (bytes)  132 - 1052
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ATTIVITA_LOAD"

CREATE TABLE  T_DMT_P4C_DM_ATTIVITA_LOAD
(
     FK_IDN_AUDIT_PROGRAMMA             bigint                    not null  default 0,
     PK_P4C_ATTIVITA                    bigint                    not null  default 0,
     CDN_MASTER                         bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO              bigint                    not null  default 0,
     DTA_INSERIMENTO                    timestamp                 not null,
     FK_UTENTE_AGGIORNAMENTO            bigint                    not null  default 0,
     DTA_AGGIORNAMENTO                  timestamp                 not null,
     DTA_INIZIO_VALIDITA                timestamp                 not null,
     DTA_FINE_VALIDITA                  timestamp                 not null,
     FLN_VALIDITA                       byteint                   not null  default 0,
     DTA_CANC_FISICA                    timestamp                 not null,
     FLN_CANC_FISICA                    byteint                   not null  default 0,
     IDC_ID_KEY_ATTIVITA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_STATO_ATTIVITA                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_COMMODITY                      character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPO_CLIENTE                   character varying(120)    not null  default '***'::"NVARCHAR",
     CDC_POD                            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_ATTIVITA                  character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_ATTIVITA             character varying(120)    not null  default '***'::"NVARCHAR",
     LDS_FAMIGLIA                       character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_SPECIFICA                      character varying(120)    not null  default '***'::"NVARCHAR",
     CDC_SERVIZIO_CALC                  character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_LOGIN_INS                      character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS            bigint                    not null  default 0,
     MDS_LOGIN_OWNER                    character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_OWNER          bigint                    not null  default 0,
     MDS_LOGIN_AGG                      character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG            bigint                    not null  default 0,
     DTA_INSERIMENTO_RO                 timestamp                 not null,
     DTA_AGGIORNAMENTO_RO               timestamp                 not null,
     DTA_TERMINE                        timestamp                 not null,
     DTA_INIZIO_ATTIVITA                timestamp                 not null,
     DTA_PRIMA_ASSEGNAZIONE             timestamp                 not null,
     DTA_ULTIMA_ASSEGNAZIONE            timestamp                 not null,
     DTA_ULTIMO_FATTO                   timestamp                 not null,
     IDC_ID_KEY_RICHIESTE               character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PROCESSO                       character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_STATO_RICHIESTA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SUBSTATO_RICHIESTA             character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_CANCELLAZIONE          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_FISCALE                        character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CLIENTE                        character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ID_KEY_OFF                     character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_INTERAZIONE                 bigint                    not null  default 0,
     IDC_ID_KEY_INTERAZIONE             character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_ATTIVITA                  character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_CHIAMATA                numeric(22,7),
     DTA_INSERIMENTO_RO_INTERAZIONE     timestamp                 not null,
     CDC_CODA_TELEFONICA                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SOTTOCODA_TELEFONICA           character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_TIPO_RECORD_ATTIVITA           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER                bigint                    not null  default 0,
     CDC_BUSINESS_PARTNER               character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPO_SORGENTE                  character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SITO                        bigint                    not null  default 0,
     CDC_TIPO                           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_VAS                   character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_CLIENTE                     bigint                    not null  default 0,
     CDC_SEGMENTO_CLIENTE               character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CALL_ID                        character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_INTERAZ                 character varying(255)    not null  default '***'::"NVARCHAR",
     QTA_DURATA                         bigint,
     FK_CDR_INBOUND                     bigint                    not null  default 0,
     FK_CDR_CHAT                        bigint                    not null  default 0,
     FK_CDR_OUTBOUND                    bigint                    not null  default 0,
     LDS_CODA                           character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_SOTTOCANALE_INS             bigint                    not null  default 0,
     SDS_SOTTOCANALE_INS                character varying(50)     not null  default '***'::"NVARCHAR",
     FK_PARTNER_INS                     bigint                    not null  default 0,
     CDC_AGENZIA_INS                    character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_OWNER              character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_OWNER                  character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG                character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_AGG                    character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_DOC_ALLEGATO                   byteint                   not null  default 0,
     LDS_PIATTAFORMA                    character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO                character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                        character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                     character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_ID_CORRISPONDENZA              character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_RICHIESTA                   bigint                    not null  default 0,
     LDS_FAMIGLIA_RECLAMI               character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_FAMIGLIA_ATTIVITA              character varying(255)    not null  default '***'::"NVARCHAR",
     FK_PARTNER_AGG                     bigint                    not null  default 0
)
DISTRIBUTE ON (PK_P4C_ATTIVITA)
;

/*
       Number of columns  86
 
    (Variable) Data Size  381 - 6617
            Row Overhead  43
  ======================  =============
  Total Row Size (bytes)  424 - 6660
*/
                      

\echo
\echo *****  Creating table:  "T_DMT_P4C_DM_ATTIVAZIONI_LOAD"

CREATE TABLE  T_DMT_P4C_DM_ATTIVAZIONI_LOAD
(
     FK_IDN_AUDIT_PROGRAMMA                          bigint                    not null  default 0,
     PK_P4C_ATTIVAZIONI                              bigint                    not null  default 0,
     CDN_MASTER                                      bigint                    not null  default 0,
     FK_UTENTE_INSERIMENTO                           bigint                    not null  default 0,
     DTA_INSERIMENTO                                 timestamp                 not null,
     FK_UTENTE_AGGIORNAMENTO                         bigint                    not null  default 0,
     DTA_AGGIORNAMENTO                               timestamp                 not null,
     DTA_INIZIO_VALIDITA                             timestamp                 not null,
     DTA_FINE_VALIDITA                               timestamp                 not null,
     FLN_VALIDITA                                    byteint                   not null  default 0,
     DTA_CANC_FISICA                                 timestamp                 not null,
     FLN_CANC_FISICA                                 byteint                   not null  default 0,
     DTA_RIFERIMENTO_FLUSSO                          timestamp                 not null,
     LDS_CAUSALE_OPERAZIONE                          character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CASO_REMUNERAZIONE                          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CASO_REMUNERAZIONE_SFC                      character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CASO_REMUNERAZIONE_OLD                      character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_COD_AGENTE                                  character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA                              character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_EFFETTO                                     timestamp                 not null,
     DTA_INIZIO_TIMING                               timestamp                 not null,
     DTA_FINE_TIMING                                 timestamp                 not null,
     IDC_ROW_ID_OFFERTA                              character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_OFFERTA_OLD                          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_NUMERO_OFFERTA                              character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_OFFERTA                           timestamp                 not null,
     DTA_ULT_MOD_OFFERTA                             timestamp                 not null,
     LDS_STATO_OFFERTA_SFC                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_STATO_OFFERTA                               character varying(255)    not null  default '***'::"NVARCHAR",
     FLN_DOCUMENTO_ARCHIVIATO                        byteint                   not null  default 0,
     LDS_CAUSALE_STATO_OFFERTA                       character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_POD_OFFERTA                                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPOLOGIA_OFFERTA                           character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_OFFERTA                         character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_OFFERTA_OLD                     character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_RIGA_OFFERTA                      timestamp                 not null,
     DTA_ULT_MOD_RIGA_OFFERTA                        timestamp                 not null,
     LDS_STATO_RIGA_OFFERTA                          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_STATO_RIGA_OFFERTA                  character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_RIGA_OFFERTA                      character varying(120)    not null  default '***'::"NVARCHAR",
     FLN_CANCELLAZIONE_RIGA_OFFERTA                  byteint                   not null  default 0,
     IDC_ROW_ID_ORDINE                               character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_ORDINE_OLD                           character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_ORDINE                            timestamp                 not null,
     DTA_ULT_MOD_ORDINE                              timestamp                 not null,
     CDC_POD_ORDINE                                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPOLOGIA_ORDINE                            character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_ORDINE                          character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_RIGA_ORDINE_OLD                      character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_CREAZIONE_RIGA_ORDINE                       timestamp                 not null,
     DTA_ULT_MOD_RIGA_ORDINE                         timestamp                 not null,
     LDS_STATO_RIGA_ORDINE                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_STATO_RIGA_ORDINE                   character varying(255)    not null  default '***'::"NVARCHAR",
     MDS_TIPOLOGIA_RIGA_ORDINE                       character varying(120)    not null  default '***'::"NVARCHAR",
     FLN_CANCELLAZIONE_RIGA_ORDINE                   byteint                   not null  default 0,
     DTA_RILAVORAZIONE_COMMERCIALE                   timestamp                 not null,
     FLN_RILAVORAZIONE_COMMERCIALE                   byteint                   not null  default 0,
     CDC_STATO_RID                                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_SERVIZIO                           character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_NOME_PRODOTTO_SERVIZIO                      character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_DESCRIZIONE_PRODOTTO_SERVIZIO               character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_ATTIVAZIONE_SERVIZIO                        timestamp                 not null,
     LDS_STATO_SERVIZIO                              character varying(255)    not null  default '***'::"NVARCHAR",
     DTA_CESSAZIONE_SERVIZIO                         timestamp                 not null,
     LDS_STATO_TRASPORTO                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CAP_PRODOTTO_SERVIZIO                       character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_COMUNE_PRODOTTO_SERVIZIO                    character varying(255)    not null  default '***'::"NVARCHAR",
     SDS_PROVINCIA_PRODOTTO                          character varying(50)     not null  default '***'::"NVARCHAR",
     VAL_TOT_POT_CONTRATTUALE_SITO                   numeric(22,7),
     VAL_TOT_POTENZA_DISPONIBILE                     numeric(22,7),
     FLN_OPZIONE_GREEN_PRODOTTO                      byteint                   not null  default 0,
     LDS_PIANO_PROVVIGIONALE_PROD                    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_TIPO_UTILIZZO_PRODOTTO                      character varying(255)    not null  default '***'::"NVARCHAR",
     FLC_RESIDENTE                                   character(1)              not null  default '*'::"NVARCHAR",
     LDS_TIPO_SERVIZIO_PRODOTTO                      character varying(255)    not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_CLIENTE                              character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_CLIENTE_OLD                          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_BUSINESS_PARTNER                            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_TIPOLOGIA_CLIENTE                           character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_FISCALE_CLIENTE                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_PART_IVA_CLIENTE                            character varying(50)     not null  default '***'::"NVARCHAR",
     MDS_RAGIONE_SOCIALE_CLIENTE                     character varying(120)    not null  default '***'::"NVARCHAR",
     LDS_FORMA_GIURIDICA                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CAP_CLIENTE                                 character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_COMUNE_CLIENTE                              character varying(255)    not null  default '***'::"NVARCHAR",
     SDS_SIGLA_PROVINCIA_CLIENTE                     character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_CONTATTO_VOCAL                              byteint                   not null  default 0,
     CDC_CANALE                                      character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_RID_IN_QC                                   byteint                   not null  default 0,
     DTA_ST_RICEVUTA                                 timestamp                 not null,
     DTA_ST_CHIUSA                                   timestamp                 not null,
     CDC_AGENZIA_BOLLETTA_WEB                        character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CATEGORIA_USO                               character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_MERCATO                                     character varying(255)    not null  default '***'::"NVARCHAR",
     FLN_BOLLETTA_WEB                                byteint                   not null  default 0,
     CDC_STATO_BOLLETTA_WEB                          character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_CROSS_SELLING                               byteint                   not null  default 0,
     IDC_ROW_ID_SITO                                 character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ROW_ID_SITO_OLD                             character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_INSERIMENTO_SDD                             timestamp                 not null  default '01-01-1900',
     LDS_FASE_INS_SDD                                character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_SOTTOCANALE_SDD                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_SDD                                 character varying(50)     not null  default '***'::"NVARCHAR",
     FLN_BOLLETTA_WEB_IN_QC                          byteint                   not null  default 0,
     IDC_ROW_ID_INTERAZ                              character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_TIPO_INTERAZ                                character varying(255)    not null  default '***'::"NVARCHAR",
     VAL_DURATA_CHIAMATA_INTERAZ                     numeric(22,7),
     DTA_CREAZ_INTERAZ                               timestamp                 not null  default '01-01-1900',
     IDN_SOTTOCANALE_ATTIVAZ_SDD                     bigint                    not null  default 0,
     LDS_CANALE_INVIO_CONTRATTO                      character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_MODALITA_FIRMA                              character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_ACQUISITIVO                 bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_INS_OFFERTA                    character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_OFFERTA                 bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_OFFERTA                    character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_OFFERTA                 bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_INS_LINEA_OFFERTA_FORN         character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_LINEA_OFFERTA_FORN      bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_LINEA_OFFERTA_FORN         character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_LINEA_OFFERTA_FORN      bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_RICEV             character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_RICEV          bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_DA_CONFERM        character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_DA_CONFERM     bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_SOSP              character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_SOSP           bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_CHIUSA            character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_CHIUSA         bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_PASSAG_STATO_ANNULL            character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_PASSAG_STATO_ANNULL         bigint                    not null  default 0,
     FLN_QC_CHIAMATA_CONCLUSA                        byteint                   not null  default 0,
     MDS_LOGIN_UTENTE_INS_LINEA_OFFERTA_BW           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INS_LINEA_OFFERTA_BW        bigint                    not null  default 0,
     MDS_LOGIN_UTENTE_AGG_LINEA_OFFERTA_BW           character varying(120)    not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_AGG_LINEA_OFFERTA_BW        bigint                    not null  default 0,
     CDC_CODA_TELEFONICA                             character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SOTTOCODA_TELEFONICA                        character varying(50)     not null  default '***'::"NVARCHAR",
     IDC_ID_CASE                                     character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_ANAG_PARTNER_INTERAZ                     bigint                    not null  default 0,
     LDS_CONSENSO_MARKET_TELEFONO                    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_MARKET_EMAIL                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_MARKET_CELL                        character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_PROFILAZIONE                       character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_TERZI_TEL                          character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_TERZI_EMAIL                        character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CONSENSO_TERZI_CELL                         character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_CLIENTE                                  bigint                    not null  default 0,
     SK_IDN_SITO                                     bigint                    not null  default 0,
     CDC_CALL_ID                                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CANALE                                      character varying(255)    not null  default '***'::"NVARCHAR",
     QTA_DURATA                                      bigint,
     FK_CDR_INBOUND                                  bigint                    not null  default 0,
     FK_CDR_CHAT                                     bigint                    not null  default 0,
     FK_CDR_OUTBOUND                                 bigint                    not null  default 0,
     LDS_CODA    character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_CANALE_CONTATTO                             character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_AGENZIA_INS_OFFERTA                         character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_PARTNER_INS_OFFERTA                      bigint                    not null  default 0,
     SDS_SOTTOCANALE_INS_OFFERTA                     character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_OFFERTA                     character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INS_LINEA_OFFERTA_FORN          character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_LINEA_OFFERTA_FORN          character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_RICEV              character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_DA_CONFERM         character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_SOSP               character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_CHIUSA             character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_ANNULL             character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INS_LINEA_OFFERTA_BW            character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_AGG_LINEA_OFFERTA_BW            character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_INTERAZ                         character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_SOTTOCANALE_INS_OFF                      bigint                    not null  default 0,
     FLN_RID_OBBLIGATORIO                            byteint                   not null  default 0,
     LDS_PIATTAFORMA                                 character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CONTATTO                               character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CLUSTER                                     character varying(255)    not null  default '***'::"NVARCHAR",
     LDS_OPERAZIONE                                  character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_ENTITA_RIF                                  character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PROCESSO_CASE                               character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_STATO_RICHIESTA_CASE                        character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_SUBSTATO_RICHIESTA_CASE                     character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_CAUSALE_CANCELLAZIONE_CASE                  character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_TIPO_CASE                                   character varying(50)     not null  default '***'::"NVARCHAR",
     LDS_PRODOTTO_VAS_CASE                           character varying(255)    not null  default '***'::"NVARCHAR",
     SK_IDN_RICHIESTA                                bigint                    not null  default 0,
     CDC_STATO_UDB_CITEM                             character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_AGG_OFFERTA                  character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_INS_LINEA_OFFERTA_FORN       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_AGG_LINEA_OFFERTA_FORN       character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_RICEV           character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_DA_CONFERM      character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_SOSP            character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_CHIUSA          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_ANNULL          character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_INS_LINEA_OFFERTA_BW         character varying(50)     not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_AGG_LINEA_OFFERTA_BW         character varying(50)     not null  default '***'::"NVARCHAR",
     SK_IDN_INTERAZIONE                              bigint                    not null  default 0,
     DTA_ST_PRIMO_ANN                                timestamp                 not null,
     LDS_TIPO_USO                                    character varying(255)    not null  default '***'::"NVARCHAR",
     CDC_CODICE_AGENZIA_PASSAG_STATO_INV             character varying(50)     not null  default '***'::"NVARCHAR",
     SDS_SOTTOCANALE_PASSAG_STATO_INV                character varying(50)     not null  default '***'::"NVARCHAR",
     DTA_ST_PRIMO_INV                                timestamp                 not null  default '01-01-1900 00:00:00',
     DTA_ST_PRIMO_SOS                                timestamp                 not null  default '01-01-1900 00:00:00',
     DTA_ST_PRIMO_CDC                                timestamp                 not null  default '01-01-1900 00:00:00'
)
DISTRIBUTE ON (CDC_CASO_REMUNERAZIONE)
;
'''