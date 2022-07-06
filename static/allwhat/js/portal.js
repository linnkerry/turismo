//Buscar Prsona en la BD
function loadDoc() {
    documento = document.getElementById("documento").value;
    console.log(documento);
    if (documento.length == '8') {
        $.ajax({
            url: "/persona/",
            type: "post",
            data: {
                "dni": documento,
                "csrfmiddlewaretoken": "{{csrf_token}}",
            },
            success: function (datos) {
                $("#nombres").val(datos.nombre);
                $("#apepaterno").val(datos.apepaterno);
                $("#apematerno").val(datos.apematerno);
            },  error: function (err) {
                  if (err.status == 500) {
                       $("#nombres").removeAttr("readonly");
                       $("#apepaterno").removeAttr("readonly");
                       $("#apematerno").removeAttr("readonly");

                  }else {
                      alert('Unexpected error.');
                  }
              }
        });
    }
}

function crearpersona() {
    var nombres = $("#nombres").val();
    var apepaterno = $("#apepaterno").val();
    var apematerno = $("#apematerno").val();
    $.ajax({
        url: "/crearpersona/",
        type: "post",
        data: {
            "dni": documento,
            "nombres": nombres,
            "apepaterno": apepaterno,
            "apematerno": apematerno,
            "csrfmiddlewaretoken": "{{ csrf_token }}",
        },
        success: function (datos) {
            console.log("Success");
        },
    });
}