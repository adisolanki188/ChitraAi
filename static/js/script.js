async function generateImage() {

const prompt =
document.getElementById("prompt").value;

const result =
document.getElementById("result");

result.innerHTML =
"Generating...";

const response = await fetch(
"/generate-image",
{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
prompt
})
}
);

const data = await response.json();

result.innerHTML = `
<h3>Enhanced Prompt</h3>
<p>${data.prompt}</p>
`;
}
