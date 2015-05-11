var editor;
var activeId;

window.onload = function() {
	// Listen to the double click event.
	if ( window.addEventListener )
		document.body.addEventListener( 'dblclick', onDoubleClick, false );
	else if ( window.attachEvent )
		document.body.attachEvent( 'ondblclick', onDoubleClick );

};

$(document).keyup(function(e) {

		if (e.keyCode == 27) { // esc

		cancel();
	}
	   
});

$('#saveCancel').click(function(){
	cancel();
});

$('#save').click(function(){
	save();
});

function save(){
	if (!editor)
	{
		return;
	}

	var primary = 0;
	if (editor.name == "map")
	{
		primary = 1;
	}

	editor.destroy();


	if(primary == 0)
	{
		var activeId = $('#primary').attr('data-id');
		var value = $('#primary').html();
		$.get('case_save/', {caseId: activeId, caseData: value}, function(result){});
			
	}
}

function cancel(){
	if (!editor)
	{
		return;
	}

	editor.destroy();

	var activeId = $('#primary').attr('data-id');
	var value = $('#primary').html();
	$.get('/CLP/case/', {caseId: activeId}, function(data){
           	$('#primary').html(data.value);
		   	$('#primary').attr('data-id', activeId);
		});
}

function onDoubleClick( ev ) {

	if(editor)
		editor.destroy();
	// Get the element which fired the event. This is not necessarily the
	// element to which the event has been attached.
	var element = ev.target || ev.srcElement;

	// Find out the div that holds this element.
	var name;

	while ( element && ( name = element.nodeName.toLowerCase() ) &&
		( name != 'div' || element.className.indexOf( 'content' ) == -1 ) && name != 'body' )
	{
		element = element.parentNode;
	}

	if ( name == 'div' && element.className.indexOf( 'content' ) != -1 )
		replaceDiv( element );
}

function replaceDiv( div ) {
	if ( editor )
		editor.destroy();

	editor = CKEDITOR.replace( div );
}

function callback(data){
	alert(data.message);
}

function refreshSidebars(data){

}

$(document).on("click", ".get_case", function(){
var id;
id = $(this).attr("data-id");
var sender = $(this);
var parent = $(this).parent().parent().attr("id");
 $.get('/CLP/case/', {caseId: id}, function(data){
        if( parent != 'citationList' && parent!='stack' && (editor == undefined || editor.status == "destroyed"))
        {
        	console.log(sender.parent().parent())
           	$('#primary').html(data.value);
		   	$('#primary').attr('data-id', id);

		   	$('#citationList').empty();
		   	$('#citationList').append(data.citations);
		}
		else
		{
           	$('#secondary').html(data.value);
		   	$('#secondary').attr('data-id', id);

		}
		$('#stack' + id).remove();
		$('#stack').prepend("<li id=\"stack"+id+"\"><a class=\"get_case\" data-id=\"" + id + "\" href=\"#\">"+data.name+"</a></li>");
		if( $('#stack li').length > 20 )
			{$('#stack li:last').remove();}
    });
})

$(document).on("click", ".move_case", function(){
var parentId = $(this).attr("data-id");
var childId = $('#primary').attr("data-id");

 	$.get('/CLP/move_case/', {parentId:parentId, childId:childId}, function(data){
           $('#sideFolder' + parentId).append($('#sideItem' + childId).remove().html());
           $('#modalFolder' + parentId).append($('#modalItem' + childId).remove().html());
           $('#linkFolder' + parentId).append($('#linkItem' + childId).remove().html());

       });
})

$(document).on("click", ".link_case", function(){
var citation = $(this).attr("data-id");
var primary = $('#primary').attr("data-id");

 	$.get('/CLP/link_case/', {primary:primary, citation:citation}, function(data){

       });
})

$('#add_case').click(function(){

	$.get('/CLP/case_add/', {slave:"False"}, function(data){
		$('#primary').html(data.value);
		$('#primary').attr('data-id', data.id);
		$('#sideRoot').append(data.header);
		$('#linkRoot').append(data.header);
	})
})

$('#add_folder').click(function(){
	$.get('/CLP/case_add/', {slave:"True"}, function(data){
		$('#primary').html(data.value);
		$('#primary').attr('data-id', data.id);
		$('#sideRoot').append(data.header);
		$('#modalRoot').append(data.header); 
		$('#linkRoot').append(data.header);   
	})
})