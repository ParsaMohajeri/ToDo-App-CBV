document.addEventListener("DOMContentLoaded", function () {
    // Edit button
    document.querySelectorAll(".edit-btn").forEach(btn => {
        btn.addEventListener("click", e => {
            e.preventDefault();
            const id = btn.dataset.id;
            fetch(/work/${id}/edit/)
                .then(res => res.text())
                .then(html => {
                    document.getElementById("editModalBody").innerHTML = html;
                    new bootstrap.Modal(document.getElementById("editModal")).show();
                });
        });
    });

    // Delete button
    let deleteId = null;
    document.querySelectorAll(".delete-btn").forEach(btn => {
        btn.addEventListener("click", e => {
            e.preventDefault();
            deleteId = btn.dataset.id;
            new bootstrap.Modal(document.getElementById("deleteModal")).show();
        });
    });

    // Confirm delete
    document.getElementById("confirmDeleteBtn").addEventListener("click", function () {
        fetch(/work/${deleteId}/delete/, {
            method: "POST",
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        }).then(res => res.json()).then(data => {
            if (data.success) {
                location.reload();
            }
        });
    });
});