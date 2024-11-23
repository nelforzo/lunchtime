document.body.addEventListener('htmx:afterSwap', function(evt) {
    if (evt.detail.target.id === "read_target") {
        var data = JSON.parse(evt.detail.xhr.responseText);

        var inner_html = '';
        data.forEach(function(item) {
            inner_html += '<div class="lunch_item" id="lunch_'+item.id+'">';
            inner_html += '<span>' + item.name + '</span> ';
            inner_html += '<span>' + item.price +'</span> ';
            inner_html += '<button class="outline" '
            +'hx-delete="/lunches/delete/'+item.id+'/" '
            +'hx-target="#delete_target" '
            +'hx-headers=\'{"X-CSRFToken": "' + document.querySelector('[name=csrfmiddlewaretoken]').value + '"}\' '
            +'hx-trigger="click">delete</button>';
            inner_html += '</div>';
        });
        
        evt.target.innerHTML = inner_html;
        // process all new elements
        htmx.process(document.body);
    } else if (evt.detail.target.id === "delete_target") {
        // get the processed path
        var processed_path = evt.detail.requestConfig.path;
        // get the id of the deleted item from the processed path. eg. /lunches/delete/2/
        var deleted_id = processed_path.split('/').filter(Boolean)[2];
        // remove the item from the list
        var element_to_delete = document.getElementById('lunch_'+deleted_id);
        element_to_delete.remove();
    }
});
