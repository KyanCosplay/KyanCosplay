// Datos de las imágenes
let images = [
    {
        src: 'Images/Home/CosplayVikinga.jpg',
        text: 'Cosplay',
        additionalText: 'Te enseñamos todos los cosplays que tenemos disponibles y los que estan por venir.',
        buttonText: 'Ver más',
        buttonLink: 'html/cosplays.html'
    },
    {
        src: 'Images/Home/taller_costura.jpg',
        text: 'Talleres',
        additionalText: 'Aqui puedes informarte sobre como apuntarte a los talleres de cosplay.',
        buttonText: 'Descubre',
        buttonLink: 'https://ejemplo.com/evento'
    },
    {
        src: 'Images/Home/CosplayVikinga.jpg',
        text: 'Servicios Personalizados',
        additionalText: 'En caso que no tengas tiempo para hacerte tu propio cosplay, te ofrecemos nuestro servicio personalizado.',
        buttonText: 'Explora',
        buttonLink: 'https://ejemplo.com/coleccion'
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
