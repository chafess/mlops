
  
    
    

    create  table
      "ventes"."main"."ventes_resume__dbt_tmp"
  
    as (
      select
    categorie,
    sum(quantite) as total_quantite,
    sum(chiffre_affaires) as total_ca
from "ventes"."main"."ventes_clean"
group by categorie
    );
  
  