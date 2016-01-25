<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
  <title>{{title}}</title>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700,600' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" type="text/css" href="http://localhost:8085/static/design.css">
</head>
<body>

<!-- Navbar -->

<ul class="navbar">
	<div class="logo">Domotique</div>
 	<li><a href="http://localhost:8085/">Home page</a></li>
 	<li><a href="http://localhost:8085/log">Log UDP</a></li>
	<li><a href="http://localhost:8085/log_server">Log Serveur</a></li>
	<li><a href="http://localhost:8085/log_module">Log Module</a></li>
	<li><a href="http://localhost:8085/xpl">Send XPL</a></li>
</ul>
<!-- Menu gauche --><div class="test">
<div class="menu">
	%for x in menu:
		<button onclick="location.href='http://localhost:8085/room/{{x['id']}}'">{{x["name"]}}</button>
	%end
</div>

<!-- Main content -->
<div class="content">
	<div class="main"><div class="prise"></div>
		<div class="main-bot"><div class="main-texte">Test</div>
		<img class="myImage" src="http://localhost:8085/static/button-on.png" width="70" height="50">
		</div>
	</div>
	<div class="main"><div class="prise"></div>
		<div class="main-bot"><div class="main-texte">Test</div>
				</div>
	</div>
	<div class="main"><div class="prise"></div>
		<div class="main-bot"><div class="main-texte">Test</div>
		<img class="myImage" src="http://localhost:8085/static/button-on.png" width="70" height="50">
		</div>
	</div>
	<div class="main"><div class="prise"></div>
		<div class="main-bot"><div class="main-texte">Test</div>
		<img class="myImage" src="http://localhost:8085/static/button-off.png" width="70" height="50">
		</div>
	</div>
	<div class="main"><div class="prise"></div>
		<div class="main-bot"><div class="main-texte">Test</div>
		<img class="myImage" src="http://localhost:8085/static/button-on.png" width="70" height="50">
		</div>
	</div>
	<div class="main"><div class="prise"></div>
		<div class="main-bot"><div class="main-texte">Test</div>
		<img class="myImage" src="http://localhost:8085/static/button-on.png" width="70" height="50">
		</div>
	</div>
</div>
</div>
</body>
</html>