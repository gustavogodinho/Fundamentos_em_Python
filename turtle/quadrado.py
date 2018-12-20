

CREATE TABLE BSC_PUB_NF_CAPA_TERMINAL 
(
PNT_ID NUMBER(20) NOT NULL,
PNC_ID NUMBER(20) NOT NULL,
PNT_NUM_TERMINAL VARCHAR2(12) NULL,
PWFCCID VARCHAR2(38)
);

ALTER TABLE BSC_PUB_NF_CAPA_TERMINAL ADD PRIMARY KEY (PNT_ID);

ALTER TABLE BSC_PUB_NF_CAPA_TERMINAL ADD CONSTRAINT PNC_ID_PUB_NF_CAPA_TERMINAL FOREIGN KEY (PNC_ID) REFERENCES BSC_PUB_NF_CAPA(PNC_ID);


COMMENT ON COLUMN BSC_PUB_NF_CAPA_TERMINAL.PNT_ID IS 'Identificador único';

COMMENT ON COLUMN BSC_PUB_NF_CAPA_TERMINAL.PNC_ID IS 'ID de relacionamento para tabela BSC_PUB_NF_CAPA';

COMMENT ON COLUMN BSC_PUB_NF_CAPA_TERMINAL.PNT_NUM_TERMINAL IS 'Número do terminal telefônico';

COMMENT ON COLUMN BSC_PUB_NF_CAPA_TERMINAL.PWFCCID IS ' ID de controle de transação';



{27c2bb0b-7191-46da-a369-c88ca4864f2e} 


update bsc_parametro 
set apl_id = '{27c2bb0b-7191-46da-a369-c88ca4864f2e}' 
where bpr_codigo  = 'valida_cfopxuf_00045' 
;


select * 
 from bsc_parametro a1,
	  bsc_param_conf a2 	
where a1.bpr_id = a2.bpr_id
and bpr_codigo  = 'valida_cfopxuf_00045' 
;
