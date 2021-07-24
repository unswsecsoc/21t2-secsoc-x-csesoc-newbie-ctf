let submitHandler = (e) => {
  e.preventDefault();

  let inp = document.querySelector("input[id=file]");
  if (!inp.files) {
    return;
  }
  let formData = new FormData();
  formData.append("file", inp.files[0]);

  // file name
  formData.append("filename", document.querySelector("#filename"));

  fetch("/upload", {
    method: "POST",
    body: formData,
  }).then(async (r) => {
    let text = await r.text();
    let elem = document.getElementById("done-box");
    let area = document.getElementById("done-area");
    let doneClasses = "alert";
    if (r.status >= 400) {
      elem.className = doneClasses + " alert-danger-custom";
      area.innerText = text;
    } else {
      // get the correct link
      let link = "https://" + window.location.hostname;
      if (window.location.port) {
        link += ":" + window.location.port;
      }
      link += text;
      let linkElem = document.createElement("a");
      linkElem.className = "link";
      linkElem.href = link;
      linkElem.innerText = link;
      elem.className = doneClasses + " alert-success";
      area.innerText = "Success: Your file can be downloaded at: ";
      area.appendChild(linkElem);
    }
  });
};

document.querySelector("#fileupload").addEventListener("submit", submitHandler);
