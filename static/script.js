document.getElementById("callForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const phone = document.getElementById("phone").value;
  const message = document.getElementById("message").value;
  const time = document.getElementById("time").value;

  const response = await fetch("/schedule", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ phone, message, time })
  });

  const data = await response.json();
  document.getElementById("result").innerText = data.message;
});
