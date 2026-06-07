
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select produit
from "ventes"."main"."ventes_clean"
where produit is null



  
  
      
    ) dbt_internal_test