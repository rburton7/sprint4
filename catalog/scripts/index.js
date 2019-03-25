$((function(context) {
    return function() {


        var containers = $('.product-container');
        containers.each(function(i,c){
            var pid = $(c).attr('data-product-id');
            $.ajax({
                "url": "/catalog/product.tile/" + pid
            }).done(function(data){
                $(c).html(data);
            });

        });

    }
    
})(DMP_CONTEXT.get()));
