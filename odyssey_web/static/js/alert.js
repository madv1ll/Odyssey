function AlertEliminarProducto(id) {
  Swal.fire({
    title: 'Estas seguro?',
    text: "Esta accion es irreversible",
    icon: 'Atencion',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!',
    cancelButtonColor: '#d33',
  }).then(function(result){
      if (result.isConfirmed) {
        window.location.href = "/productos/eliminar-producto/" + id + "/"
      }
    })
}

function AlertEliminarProveedor(id) {
  Swal.fire({
    title: 'Estas seguro?',
    text: "Esta accion es irreversible",
    icon: 'Atencion',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!',
    cancelButtonColor: '#d33',
  }).then((result) => {
    if (result.isConfirmed) {

      window.location.href = "/productos/eliminar-proveedor/" + id + "/"

    }
  })
}



function AlertEliminarCategoria(id) {
  Swal.fire({
    title: 'Estas seguro?',
    text: "Esta accion es irreversible",
    icon: 'Atencion',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!'
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = "/productos/eliminar-categoria/" + id + "/"
    }
  })
}

function AlertEliminarUser(id) {
  Swal.fire({
    title: 'Estas seguro?',
    text: "Esta accion es irreversible",
    icon: 'Atencion',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!',
    cancelButtonColor: '#d33',
  }).then(function(result){
      if (result.isConfirmed) {
        window.location.href = "/user/eliminar_usuario/" + id + "/"
      }
    })
}

function AlertAgregarCarrito(id) {
  Swal.fire({
    title: 'Estas seguro?',
    text: "El producto se agregar al carrito de compras",
    icon: 'Atencion',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Agregar!'
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = "/carrito/agregar/" + id + "/"
    }
  })
}




