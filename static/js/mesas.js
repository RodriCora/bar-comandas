document.addEventListener('DOMContentLoaded', () => {
  const panelOrden = document.getElementById('panel-orden');
  const btnCerrarOrden = document.getElementById('btn-cerrar-orden');
  const ordenMesaNum = document.getElementById('orden-mesa-num');
  const nombreMeseraSpan = document.getElementById('nombre-mesera');
  const formOrden = document.getElementById('form-orden');
  const listaOrdenes = document.getElementById('lista-ordenes');
  const btnEnviarCobro = document.getElementById('btn-enviar-cobro');

  let mesaSeleccionada = null;
  let ordenActual = [];

  // Abrir panel con mesa seleccionada
  function abrirPanelOrden(numero) {
    mesaSeleccionada = numero;
    ordenMesaNum.textContent = numero;
    ordenActual = [];
    listaOrdenes.innerHTML = '<p>No hay productos agregados.</p>';
    panelOrden.classList.add('abierto');
  }

  // Cerrar panel
  function cerrarPanelOrden() {
    panelOrden.classList.remove('abierto');
    mesaSeleccionada = null;
    ordenActual = [];
    listaOrdenes.innerHTML = '<p>No hay productos agregados.</p>';
  }

  // Agregar producto a la orden
  function agregarProducto(producto, cantidad) {
    const index = ordenActual.findIndex(item => item.producto === producto);
    if (index >= 0) {
      ordenActual[index].cantidad += cantidad;
    } else {
      ordenActual.push({ producto, cantidad });
    }
    renderizarOrden();
  }

  // Mostrar lista en el div
  function renderizarOrden() {
    if (ordenActual.length === 0) {
      listaOrdenes.innerHTML = '<p>No hay productos agregados.</p>';
      return;
    }
    listaOrdenes.innerHTML = '';
    ordenActual.forEach(({ producto, cantidad }) => {
      const div = document.createElement('div');
      div.textContent = `${producto} x ${cantidad}`;
      listaOrdenes.appendChild(div);
    });
  }

  // Click en mesas
  document.querySelectorAll('.salon a').forEach(mesa => {
    mesa.addEventListener('click', e => {
      e.preventDefault();
      const numero = parseInt(mesa.querySelector('.mesa').dataset.numero);
      abrirPanelOrden(numero);
    });
  });

  // Cerrar panel
  btnCerrarOrden.addEventListener('click', cerrarPanelOrden);

  // Form submit
  formOrden.addEventListener('submit', e => {
    e.preventDefault();
    const producto = formOrden.producto.value;
    const cantidad = parseInt(formOrden.cantidad.value);
    if (!producto || cantidad < 1) return;
    agregarProducto(producto, cantidad);
    formOrden.reset();
    formOrden.cantidad.value = 1;
  });

  // Botón enviar a cobrar
  btnEnviarCobro.addEventListener('click', () => {
    if (!mesaSeleccionada) return alert('No hay mesa seleccionada');
    if (ordenActual.length === 0) return alert('No hay productos en la orden');

    // Acá podés mandar la orden al backend
    alert(`Enviar orden de la mesa ${mesaSeleccionada} a cobrar.`);

    cerrarPanelOrden();
  });
});
