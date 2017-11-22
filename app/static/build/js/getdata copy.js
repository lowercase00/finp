$(document).ready(function() {
    $('#outroex').dataTable({
        "serverSide": true,
        "processing": true,
        "ajax": {
            "url": "/base_completa2",
            "type": "POST",
            "columns": [
                { "data": "data" },
                { "data": "dsc" },
                { "data": "valor" },
                { "data": "deb" },
                { "data": "cred" }
            ]
        }
    });
});