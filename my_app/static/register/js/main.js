function passwordVisibility() {
        var passwordField = document.getElementById("password");
        var eyeIcon = document.getElementById("showPass");
        var eyeSlashIcon = document.getElementById("hidePass");

        if (passwordField.type === "password") {
            passwordField.type = "text";
            eyeIcon.classList.add("d-none");
            eyeSlashIcon.classList.remove("d-none");
        } else {
            passwordField.type = "password";
            eyeIcon.classList.remove("d-none");
            eyeSlashIcon.classList.add("d-none");
        }
    }