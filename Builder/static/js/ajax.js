$(document).ready(function() {

});

$('.get_case').click(function(){
var id;
id = $(this).attr("data-id");
 $.get('/CLP/case/', {caseId: id}, function(data){
           $('#case').html(data.value);
		   $('#case').attr('data-id', id);
       });
})

$('.get_map').click(function(){
var id;
id = $(this).attr("data-id");
 $.get('/CLP/map/', {mapId: id}, function(data){
           $('#map').html(data.value);
           
           if(!editor)
           	   $('#map').attr('data-id', id);

       });
})

$('#add_case').click(function(){
	var id;
	id = $(this).attr("data-id");
	$.post('CLP/case/save', {caseId: id}, function(data){
		$('#case').html(value);
	});
})