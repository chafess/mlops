
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select categorie
from "ventes"."main"."ventes_resume"
where categorie is null



  
  
      
    ) dbt_internal_test