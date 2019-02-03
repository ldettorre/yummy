
$("document").ready(function(){
    
    $("#readInstructions").click(function(){
        $("#instructions").slideToggle("slow");
        
    })
    
    function hide(){
         $("#instructions").hide("slow");
    }
    function show(){
        $("#instructions").show("slow");
        
    }
    
    $("#readIngredients").click(function(){
        $("#ingredients").slideToggle("slow");
        
    })
    
    function hide(){
         $("#ingredients").hide("slow");
    }
    function show(){
        $("#ingredients").show("slow");
        
    }
})