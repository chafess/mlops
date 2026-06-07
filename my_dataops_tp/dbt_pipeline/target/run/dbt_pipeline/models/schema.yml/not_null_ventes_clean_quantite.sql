
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select quantite
from "ventes"."main"."ventes_clean"
where quantite is null



  
  
      
    ) dbt_internal_test