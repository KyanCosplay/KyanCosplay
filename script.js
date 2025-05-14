// Datos de las imágenes
let images = [
    {
        src: 'Images/Home/CosplayVikinga.jpg',
        text: 'Cosplay',
        additionalText: 'Te enseñamos todos los cosplays que tenemos disponibles y los que estan por venir.',
        buttonText: 'Ver más',
        buttonLink: 'paginas/cosplays.html'
    },
    {
        src: 'Images/Home/taller_costura.jpg',
        text: 'Talleres',
        additionalText: 'Aqui puedes informarte sobre como apuntarte a los talleres de cosplay.',
        buttonText: 'Descubre',
        buttonLink: 'paginas/talleres.html'
    },
    {
        src: 'Images/ServiciosPersonalizados/tijeraspersonalizado.jpg',
        text: 'Servicios Personalizados',
        additionalText: 'En caso que no tengas tiempo para hacerte tu propio cosplay, te ofrecemos nuestro servicio personalizado.',
        buttonText: 'Explora',
        buttonLink: 'paginas/serviciospersonalizados.html'
    }
];

let slider = document.querySelector('#slider-js');
let sliderImages = document.querySelector('.slider_images');

// Agregar imágenes con capa oscura, texto y botón
images.forEach((item, i) => {
    const slide = document.createElement('div');
    slide.classList.add('slider_slide');

    slide.innerHTML = `
        <img src="${item.src}" alt="Imagen ${i + 1}">
        <div class="slider_overlay">
            <h2>${item.text}</h2>
            <p>${item.additionalText}</p> <!-- Texto adicional -->
            <a href="${item.buttonLink}" class="slider_button" target="_blank">${item.buttonText}</a>
        </div>
    `;

    sliderImages.appendChild(slide);
});

// Establecer el ancho del contenedor
sliderImages.style.width = `${images.length * 100}%`;

let prevButton = document.querySelector('#prev');
let nextButton = document.querySelector('#next');
let navDots = document.querySelectorAll('.slider_nav');

let currentIndex = 0;

function updateSlider() {
    sliderImages.style.transform = `translateX(-${(100.9 / images.length) * currentIndex}%)`;

    navDots.forEach(dot => dot.classList.remove('active'));
    if (navDots[currentIndex]) {
        navDots[currentIndex].classList.add('active');
    }
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    updateSlider();
}

function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateSlider();
}

function goToImage(index) {
    currentIndex = index;
    updateSlider();
}

let active = true;
slider.addEventListener("mouseover", () => active = false);
slider.addEventListener("mouseout", () => active = true);

setInterval(() => {
    if (active) {
        nextImage();
    }
}, 5000);

updateSlider();

nextButton.addEventListener('click', nextImage);
prevButton.addEventListener('click', prevImage);
navDots.forEach(dot => {
    dot.addEventListener('click', (e) => {
        let index = parseInt(e.target.getAttribute('data-index'));
        goToImage(index);
    });
});


// ======================
// BUSCADOR FLOTANTE
// ======================

const contenedorBuscador = document.querySelector('.contenedor-buscador');
const botonBuscador = document.getElementById('boton-buscador');
const inputBuscador = contenedorBuscador.querySelector('.input-buscador');
const menuInferior = contenedorBuscador.querySelector('.menu-inferior');
const resultadosBusqueda = document.getElementById('resultados-busqueda');

// Función para obtener los elementos que deben ser considerados para la búsqueda
function obtenerElementosDeBusqueda() {
  // Aquí especificas los elementos que deseas buscar en la página
  // Por ejemplo, títulos, párrafos, enlaces, etc.
  const elementos = [
    ...document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, a') // Títulos, párrafos, enlaces
  ];

  return elementos;
}

// Función para actualizar los resultados de la búsqueda
function mostrarResultados(query) {
  // Limpiar resultados previos
  resultadosBusqueda.innerHTML = '';

  // Obtener los elementos de búsqueda de la página
  const elementos = obtenerElementosDeBusqueda();

  // Filtrar los elementos que coinciden con la consulta
  const resultadosFiltrados = elementos.filter(elemento =>
    elemento.textContent.toLowerCase().includes(query.toLowerCase())
  );

  // Mostrar los resultados
  if (resultadosFiltrados.length > 0) {
    resultadosFiltrados.forEach(elemento => {
      const li = document.createElement('li');
      li.innerHTML = `<a href="#${elemento.id}">${elemento.textContent}</a>`;
      resultadosBusqueda.appendChild(li);
    });
  } else {
    resultadosBusqueda.innerHTML = '<li>No se encontraron resultados</li>';
  }
}

// Activar el buscador cuando se haga clic en el botón
botonBuscador.addEventListener('click', () => {
  contenedorBuscador.classList.toggle('activo');
  if (contenedorBuscador.classList.contains('activo')) {
    inputBuscador.focus();
  } else {
    inputBuscador.value = ''; // Limpiar el valor si el buscador se cierra
    resultadosBusqueda.innerHTML = ''; // Limpiar los resultados
  }
});

// Mostrar el contenido del menú inferior solo cuando haya texto
inputBuscador.addEventListener('input', () => {
  const query = inputBuscador.value.trim();
  
  if (query !== '') {
    menuInferior.style.display = 'block'; // Mostrar el menú inferior
    mostrarResultados(query); // Mostrar los resultados filtrados
  } else {
    menuInferior.style.display = 'none'; // Ocultar el menú si el campo está vacío
  }
});

// Cerrar el buscador si se hace clic fuera de él
document.addEventListener('click', (e) => {
  if (!contenedorBuscador.contains(e.target) && !botonBuscador.contains(e.target)) {
    contenedorBuscador.classList.remove('activo');
    inputBuscador.value = ''; // Limpiar el valor cuando el buscador se cierra
    resultadosBusqueda.innerHTML = ''; // Limpiar los resultados
    menuInferior.style.display = 'none'; // Asegurarse de ocultar el menú
  }
});

//Botones de Añadir al carrito y Saber mas
// Escuchar clicks en los botones "Añadir a la cesta"
document.querySelectorAll('.btn-anadir').forEach(btn => {
  btn.addEventListener('click', () => {
    const nombre = btn.getAttribute('data-nombre');
    añadirProducto(nombre);
  });
});

// Saber más: puedes redirigir a otra página o mostrar más info
document.querySelectorAll('.btn-saber-mas').forEach(btn => {
  btn.addEventListener('click', () => {
    alert("Aquí iría la página con más información del producto.");
    // O bien: window.location.href = 'detalle-producto.html';
  });
});

// No mostrar la cesta al cargar la página
modalCesta.style.display = 'none';

// Abrir la cesta al hacer clic en el botón
cestaBtn.addEventListener('click', (e) => {
  e.stopPropagation(); // Prevenir que el clic propague al document
  modalCesta.style.display = 'block';
});

// Cerrar la cesta al hacer clic en el icono de cerrar
cerrarModalIcono.addEventListener('click', () => {
  modalCesta.style.display = 'none';
});

// Cerrar la cesta al hacer clic fuera de ella
document.addEventListener('click', (e) => {
  const clickFuera = !modalCesta.contains(e.target) && !cestaBtn.contains(e.target);
  if (modalCesta.style.display === 'block' && clickFuera) {
    modalCesta.style.display = 'none';
  }
});

