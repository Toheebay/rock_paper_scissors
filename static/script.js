function playGame(choice) {
    fetch("/play", {
        method: "POST",
        body: new URLSearchParams({ "choice": choice }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("user-choice").innerText = "Your Choice: " + data.user_choice;
        document.getElementById("computer-choice").innerText = "Computer's Choice: " + data.computer_choice;
        document.getElementById("result").innerText = data.result;
    });
}
