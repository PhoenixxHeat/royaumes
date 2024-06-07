document.getElementById('numberForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting the traditional way

    const number = parseInt(document.getElementById('numberInput').value);
    const responseElement = document.getElementById('response');

    if (isNaN(number) || number < 1 || number > 45) {
        responseElement.textContent = 'Erreur! SVP entrer un numéro valide entre 1 et 45!';
        return;
    }

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ number: number }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            responseElement.textContent = data.error;
        } else {
            responseElement.textContent = data.result;
        }
    })
    .catch(error => {
        responseElement.textContent = 'Une erreur est survenue. Réessayez plus tard.';
    });
});