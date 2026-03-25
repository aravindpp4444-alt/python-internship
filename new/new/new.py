<!DOCTYPE html>
<html>
<head>
<title>Login Page</title>

<style>
body {
  font-family: Arial;
  height: 100vh;
  margin: 0;

  background-image: url("messi.jpeg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.login-box {
  width: 300px;
  margin: 100px auto;
  padding: 20px;
  background: rgba(255,255,255,0.5);
  backdrop-filter:blur(10px);
  text-align: center;
  border-radius: 15px;
  box-shadow: 0 0 20px rgba(0,0,0,0.3);
  color:white;
}

input {
  width: 90%;
  padding: 10px;
  margin: 10px 0;
}

button {
  padding: 10px 20px;
  border:none;
  border-radius:10px;
  background: rgba(0,123,255,0.6);
  color: white;
  backdrop-filter:blur(5px);
  box-shadow:0 4px 15px rgba(0,123,255,0.5);
  cursor:pointer;
}

button:hover {
  background: darkgreen;
}
</style>

</head>

<body>

<div class="login-box">
  <h2>Login</h2>
  <input type="text" placeholder="Username"><br>
  <input type="password" placeholder="Password"><br>
  <button>Login</button>
</div>

</body>
</html>
