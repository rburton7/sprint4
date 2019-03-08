$((function(context) {
    return function() {


        var containers = $('.product-container');
        containers.each(function(i,c){
            var pid = $(c).attr('data-product-id');
            $.ajax({
                "url": "/catalog/index.tile/" + pid
            }).done(function(data){

            });

        });

    }
    
})(DMP_CONTEXT.get()));
