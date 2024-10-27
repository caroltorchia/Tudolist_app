document.addEventListener('DOMContentLoaded', function() {
    var timerElement = document.getElementById('timer');
    var resendButton = document.getElementById('resendButton');
    var timeLeft = 30; 

    var countdown = setInterval(function() {
        if (timeLeft <= 0) {
            clearInterval(countdown);
            resendButton.disabled = false;  
            timerElement.innerText = ''; 
        } else {
            resendButton.disabled = true; 
            timeLeft -= 1;
            timerElement.innerText = '00:' + (timeLeft < 10 ? '0' : '') + timeLeft;
        }
    }, 1000);

   
    resendButton.addEventListener('click', function() {
        timeLeft = 30;
        resendButton.disabled = true;
        countdown = setInterval(function() {
            if (timeLeft <= 0) {
                clearInterval(countdown);
                resendButton.disabled = false;
                timerElement.innerText = '';
            } else {
                timeLeft -= 1;
                timerElement.innerText = '00:' + (timeLeft < 10 ? '0' : '') + timeLeft;
            }
        }, 1000);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var inputs = document.querySelectorAll('.code-inputs input');
    inputs.forEach(function(input, index) {
        input.addEventListener('input', function() {
            if (input.value.length === 1 && index < inputs.length - 1) {
                inputs[index + 1].focus();
            }
        });
    });
});

document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault(); 

    var code = '';
    document.querySelectorAll('.code-inputs input').forEach(function(input) {
        code += input.value;
    });

    fetch('/confirm_code/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({ 'code': code })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Verificação concluída!');
            window.location.href = '/sucess/';
        } else {
            alert('Código inválido, tente novamente.');
        }
    });
});