document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.getElementById('toggleButton');

    toggleButton.addEventListener('click', function() {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/users/edit/');
        xhr.onload = function() {
            if (xhr.status === 200) {
                console.log('Access toggled successfully.');
                // Тут можна виконати додаткові дії після успішного змінення доступу
            } else {
                console.log('Error toggling access.');
                // Обробка помилки
            }
        };
        xhr.send();
    });
});
