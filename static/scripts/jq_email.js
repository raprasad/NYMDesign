$(document).ready(function(){
		$('span.mlink').each(function(){
		    var at_str = / \(at\) /;
    		var dot_str = / \(dot\) /g;
    		orig_val = $(this).html();
    		
		    val = orig_val.replace(dot_str, '.').replace(at_str, '@');
    		if (val!=orig_val){
        	    lnk_str = '<a href="mailto:' + val + '" title="send email">' + val + "</a>";
        		$(this).html(lnk_str);
    	    }
		});
});
