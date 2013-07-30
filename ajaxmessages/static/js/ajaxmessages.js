(function($) {
    function reloadMessages() {
        $('div.ajaxmessages').each(function(){
            // We only reload any elements that are currently being displayed.
            var queryParams = '';
            $('div.ajaxmessage').each(function(){
                var identity = $(this).attr('data-identity');
                if (queryParams.length) {
                    queryParams += ',';
                } else {
                    queryParams = '?filter=';
                }
                queryParams += identity;
            });
            // Perform the reload.
            var refreshUrl = $(this).attr('data-refresh');
            if (refreshUrl) {
                $(this).load(refreshUrl + queryParams);
            }
        });
    }

    $(document).ready(function() {
        window.setInterval(reloadMessages, 5000);
    });
})(jQuery);
