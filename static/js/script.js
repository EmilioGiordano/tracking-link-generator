document.addEventListener('DOMContentLoaded', function() {
    const numeroPedidoInput = document.getElementById('numero-pedido');
    const nroPrestashop = document.getElementById('nro-prestashop');
    const nroTrello = document.getElementById('nro-trello');
    const linkPrestashop = document.getElementById('link-prestashop');
    const linkTrello = document.getElementById('link-trello');
    
    // Validar que solo se ingresen números
    numeroPedidoInput.addEventListener('input', function(e) {
        // Remover cualquier carácter que no sea número
        this.value = this.value.replace(/[^0-9]/g, '');
        
        // Limitar a máximo 6 dígitos
        if (this.value.length > 6) {
            this.value = this.value.slice(0, 6);
        }
    });
    
    // Prevenir pegar texto que no sean números
    numeroPedidoInput.addEventListener('paste', function(e) {
        e.preventDefault();
        const pastedText = (e.clipboardData || window.clipboardData).getData('text');
        const numbersOnly = pastedText.replace(/[^0-9]/g, '');
        if (numbersOnly.length <= 6) {
            this.value = numbersOnly;
        }
    });
    
    function actualizarEnlaces() {
        const numero = numeroPedidoInput.value.trim();
        
        if (numero && numero.length === 6) {
            nroPrestashop.textContent = numero;
            nroTrello.textContent = numero;
            
            // Aquí puedes personalizar las URLs según tus necesidades
            linkPrestashop.href = `https://tu-prestashop.com/admin/orders?search=${numero}`;
            linkTrello.href = `https://trello.com/search?q=${numero}`;
            
            linkPrestashop.style.display = 'inline-block';
            linkTrello.style.display = 'inline-block';
        } else {
            nroPrestashop.textContent = '---';
            nroTrello.textContent = '---';
            linkPrestashop.href = '#';
            linkTrello.href = '#';
            linkPrestashop.style.display = 'none';
            linkTrello.style.display = 'none';
        }
    }
    
    // Actualizar enlaces cuando se ingresa el número
    numeroPedidoInput.addEventListener('input', actualizarEnlaces);
    
    // Actualizar enlaces al cargar la página si ya hay un valor
    actualizarEnlaces();
}); 