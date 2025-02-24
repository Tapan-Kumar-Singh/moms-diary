document.getElementById("familyMemberCheck").addEventListener("change", function() {
    var relationshipField = document.getElementById("relationshipField");
    relationshipField.style.display = this.checked ? "block" : "none";
});