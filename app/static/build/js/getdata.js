$(document).ready(function() {
    $('#outroex').dataTable({
        // serverSide: true,
        "ajax": {
            "url": "static/files/data.json",
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