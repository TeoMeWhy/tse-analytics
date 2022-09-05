-- Databricks notebook source
DROP TABLE IF EXISTS silver_tse.candidatos_sociodemografico;
CREATE TABLE silver_tse.candidatos_sociodemografico

WITH tb_partido_summary (

  SELECT CASE WHEN SG_PARTIDO LIKE '%PCA%' THEN 'PCA' ELSE SG_PARTIDO END AS SG_PARTIDO,
         CASE WHEN NM_PARTIDO LIKE '%SEM PARTIDO%' THEN 'SEM PARTIDO' ELSE NM_PARTIDO END AS NM_PARTIDO,
         SQ_CANDIDATO,
         DS_GENERO,
         DS_GRAU_INSTRUCAO,
         DS_ESTADO_CIVIL,
         DS_COR_RACA,
         DATEDIFF(TO_DATE(DT_ELEICAO,'d/M/y'), TO_DATE(DT_NASCIMENTO, 'd/M/y'))/365.2425 AS VL_IDADE
  FROM bronze_tse.consulta_cand_2022_brasil

),

tb_bem_candidato (

  SELECT SQ_CANDIDATO,
         SUM(CAST(REPLACE(VR_BEM_CANDIDATO, ',', '.') AS FLOAT)) AS VL_BEM_CANDIDATO
  FROM bronze_tse.bem_candidato_2022_brasil
  GROUP BY SQ_CANDIDATO

)

SELECT t1.*,
       COALESCE(t2.VL_BEM_CANDIDATO,0) AS VL_BEM_CANDIDATO
       
FROM tb_partido_summary AS t1

LEFT JOIN tb_bem_candidato AS t2
on t1.SQ_CANDIDATO = t2.SQ_CANDIDATO
