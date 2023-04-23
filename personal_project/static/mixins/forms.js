const FormResponseMixin = {
    methods: {
        handleSuccess(form, alertSuccess, alertError,data) {
            form.reset();
            form.classList.remove('was-validated');
            alertError.classList.add('d-none');
            const alertMessage = alertSuccess.querySelector('#alert_message_id');
            alertMessage.innerHTML = data.message;
            alertSuccess.classList.remove('d-none');
        },
  
        handleError(alertSuccess, alertDanger, data) {
            // alert(data.message);
            alertSuccess.classList.add("d-none");
            const alertMessage = alertDanger.querySelector('#alert_message_id');
            alertMessage.innerHTML = data.message;
            alertDanger.classList.remove("d-none");
        },
    },
};

const FormSubmitMixin = {
    mixins: [FormResponseMixin],
    methods: {
        async submitForm(event) {
            event.preventDefault();
            const form = event.target;
            const url = form.action;
            const method = form.method
            const csrfToken = form.getAttribute("data-csrf");
            const alertSuccess = form.querySelector('#alert_success_id');
            const alertDanger = form.querySelector('#alert_danger_id');
            const formData = new FormData(form);
            const response = await fetch(url, {
                method: method,
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken,
                },
            });
            if (response.ok) {
                const data = await response.json();
                if (data.status == 201){
                    FormResponseMixin.methods.handleSuccess(form, alertSuccess, alertDanger, data);
                }else{
                    FormResponseMixin.methods.handleError(alertSuccess, alertDanger, data);
                }
            } else {
                alert(data.message);
                const alertMessage = alertDanger.querySelector('#alert_message_id');
                alertMessage.innerHTML = data.message;
                alertDanger.classList.remove("d-none");
            }
        },
    },
};

const ModalFormSubmitMixin = {
    mixins: [FormSubmitMixin],
    methods: {
        handleSuccess(form, alertSuccess, alertDanger, data) {
            // Your custom code here
            alert("Form submitted successfully!");
        }
    }
};

const modal_forms = document.querySelectorAll(".modal-form");

modal_forms.forEach(modal_form => {
    Object.assign(modal_form, ModalFormSubmitMixin.methods);
    modal_form.addEventListener("submit", modal_form.submitForm);
});

const forms = document.querySelectorAll("form");
forms.forEach(form => {
  Object.assign(form, FormSubmitMixin.methods);
  form.addEventListener("submit", form.submitForm);
});

// const form_cliente = document.getElementById("create_cliente_form_id");
// const form = document.querySelector("form");
// Object.assign(form, FormSubmitMixin.methods);
// form.addEventListener("submit", form.submitForm);

// const form_venda = document.getElementById("create_venda_form_id");
// Object.assign(form_venda, FormSubmitMixin.methods);
// form_venda.addEventListener("submit", form_venda.submitForm);

// const form_analise = document.getElementById("create_analise_form_id");
// Object.assign(form_analise, FormSubmitMixin.methods);
// form_analise.addEventListener("submit", form_analise.submitForm);


const closeButtons = document.querySelectorAll('.btn-close');
    closeButtons.forEach(function(closeButton) {
      closeButton.addEventListener('click', function() {
        const alert = this.parentNode;
        alert.classList.toggle('d-none');
    });
});