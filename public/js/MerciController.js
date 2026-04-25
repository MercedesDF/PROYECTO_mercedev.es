/**
 * MerciController.js
 * @description Controlador interactivo del asistente Merci.
 * Combina la máquina de estados con mensajes aleatorios bajo estricta accesibilidad (WAI-ARIA).
 */
class MerciController {
    
    constructor(containerId) {
        this.container = document.getElementById(containerId);

        if (!this.container) {
            console.warn(`[Merci] Contenedor #${containerId} no encontrado. El asistente permanecerá en reposo.`);
            return;
        }

        // Cacheamos los elementos BEM interactivos
        this.trigger = this.container.querySelector('.merci-ui__trigger');
        this.messageBox = this.container.querySelector('.merci-ui__message-box');
        this.messageText = this.container.querySelector('.merci-ui__message-text');

        // Matriz de conocimientos/saludos (Heredada del diseño original)
        this.messages = [
            '¡Hola! 👋',
            'Todo funcionando al 100/100 🚀',
            'Mi código es Vanilla JS puro 💻',
            'Soy Merci 🤖',
            'Protegida por DevSecOps 🛡️',
            '¿Qué tal el día? 💫'
        ];

        this.state = 'idle'; 
        this.timeoutId = null; // Guarda la referencia del temporizador para no superponer mensajes

        this.init();
    }

    init() {
        // QUÉ HACE: Escucha el evento 'click' en el avatar.
        // POR QUÉ: Al usar un <button>, esto también captura automáticamente la pulsación 
        // de la tecla "Enter" o "Espacio" de usuarios de teclado, gratis.
        if (this.trigger) {
            this.trigger.addEventListener('click', () => this.handleInteraction());
        }
        console.log('[Merci] Controlador inicializado correctamente.');
    }

    handleInteraction() {
        // Escoge un mensaje aleatorio de la matriz
        const randomMsg = this.messages[Math.floor(Math.random() * this.messages.length)];
        this.speak(randomMsg);
    }

    speak(text) {
        this.state = 'speaking';
        
        // 1. Inyecta el texto
        this.messageText.textContent = text;
        
        // 2. Modifica el DOM para que el CSS actúe (hace visible el globo)
        this.messageBox.setAttribute('aria-hidden', 'false');
        this.trigger.setAttribute('aria-expanded', 'true');

        // QUÉ HACE: Reinicia el reloj para ocultar el mensaje.
        // POR QUÉ: Si el usuario hace clic 3 veces seguidas rápido, clearTimeout evita 
        // que el mensaje parpadee y se asegura de que dure 3 segundos exactos desde el último clic.
        clearTimeout(this.timeoutId);
        this.timeoutId = setTimeout(() => this.sleep(), 3500);
    }

    sleep() {
        this.setState('idle');
        
        // Oculta el globo delegando la animación al CSS
        this.messageBox.setAttribute('aria-hidden', 'true');
        this.trigger.setAttribute('aria-expanded', 'false');
        
        // Nota: NO borramos el textContent aquí. 
        // Esto permite que el lector de pantalla termine de hablar y que 
        // la transición CSS de opacidad termine suavemente sin que el texto desaparezca de golpe.
    }
}
