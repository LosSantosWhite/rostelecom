const formEl = document.querySelector('.form')

formEl.addEventListener('submit', event => {
    event.preventDefault();

    const formData = new FormData(formEl);
    const data = Object.fromEntries(formData);

    fetch('http://localhost:8000/api/user/appeal/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)

    })
});