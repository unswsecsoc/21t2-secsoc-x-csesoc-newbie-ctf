const express = require("express");
const path = require("path");
const fs = require("fs");
const multer = require("multer");

const storeLocation = "uploads/";
const storePath = path.join(__dirname, storeLocation);

const app = express();
const port = process.env.PORT || 8000;

const publicDir = path.join(__dirname, "public");
app.use(express.static(publicDir));

const pagesDir = path.join(publicDir, "pages");
app.get("/", (_, res) => {
  res.sendFile(path.join(pagesDir, "index.html"));
});

// some sanitization for my sanity
const getFilename = (fname) =>
  fname.replace(/[^\w]+/gi, "") + "t-" + Date.now().toString();

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, storePath);
  },
  filename: function (req, file, cb) {
    let fname = getFilename(file.originalname);
    cb(null, fname);
  },
});

const uploader = multer({
  storage,
  limits: {
    fileSize: 1024 * 2,
  },
}).single("file");

app.post("/upload", (req, res) => {
  uploader(req, res, (err) => {
    if (err) {
      console.log("cs " + err);
      res
        .status(400)
        .send("File might be too big. (limit: 2KB). Kindly try again");
    } else {
      try {
        console.log(req.body);
        console.log(req.file.originalname);
        console.log(req.file.filename);

        return res
          .status(200)
          .send("/download?file=" + req.file.filename)
          .toString();
      } catch (e) {
        console.log(e);
        res.status(400).send("Could not upload file, try again?");
      }
    }
  });
});

app.get("/download", (req, res) => {
  // just take the file and go
  try {
    let r = fs.readFileSync(path.join(storePath, req.query.file)).toString();
    res.header("Content-Type", "text/plain");
    res.send(r);
  } catch (err) {
    res.send("Could not find the file you're looking for");
  }
});

app.listen(port, () => {
  console.log(`Server listening on ${port}`);
});
