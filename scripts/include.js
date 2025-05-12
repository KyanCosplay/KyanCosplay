document.addEventListener("DOMContentLoaded", () => {
    const includes = document.querySelectorAll("[data-include]");
    includes.forEach(async (el) => {
        const file = el.getAttribute("data-include");
        try {
            const res = await fetch(file);
            if (res.ok) {
                el.innerHTML = await res.text();
            } else {
                el.innerHTML = "No se pudo cargar: " + file;
            }
        } catch (err) {
            el.innerHTML = "Error al cargar " + file;
        }
    });
});
