document.body.addEventListener('htmx:afterSwap', function(evt) {
    if (evt.detail.target.id === "lunches_container") {
        var data = JSON.parse(evt.detail.xhr.responseText);

        var menu_list = document.createElement('div');
        data.forEach(function(item) {
            var item_element = document.createElement('div');
            item_element.textContent = item.name;
            menu_list.appendChild(item_element);
        });
        
        evt.target.innerHTML = '';
        evt.target.appendChild(menu_list);
    }
});