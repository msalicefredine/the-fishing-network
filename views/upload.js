$( document ).ready(function() {

    var form = document.getElementById('file-form');
    var fileSelect = document.getElementById('file-select');
    var uploadButton = document.getElementById('upload-button');

    // Upload a .csv file to the server
    form.onsubmit = function(event) {
        event.preventDefault();

        // Update button text.
        uploadButton.innerHTML = 'Uploading...';

        // The rest of the code will go here...
        // Get the selected files from the input.
        var file = fileSelect.files[0];

        var form_data = new FormData(file);
        console.log(form_data);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: 'text/csv',
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                console.log('Success!');
            },
        });
    }

});