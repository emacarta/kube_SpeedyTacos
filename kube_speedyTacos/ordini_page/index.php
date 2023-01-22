<?php

function connectToDB() {
    $host = "10.106.242.28";
    $dbname = "ORDINI_database";
    $user = "SQLuser";
    $password = "1234";

    try {
        $conn = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
        echo "Connessione al database fallita: " . $e->getMessage();
        exit;
    }
    return $conn;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $conn = connectToDB();

    $tavolo = $_POST['tavolo'];
    $tacos = implode(",", $_POST['tacos']);

    try {
        $query = "INSERT INTO ORDINAZIONI (tavolo, tacos) VALUES (:tavolo, :tacos)";
        $stmt = $conn->prepare($query);
        $stmt->bindValue(':tavolo', $tavolo);
        $stmt->bindValue(':tacos', $tacos);
        $stmt->execute();
        echo "Nuova riga inserita con successo!";
    } catch (PDOException $e) {
        echo "Inserimento fallito: " . $e->getMessage();
    }
}
?>




<html>
<head>

  <meta charset="utf-8">

  <title>Ordini</title>

  <!-- Button -->
  <style>
    .button {
      border: none;
      color: white;
      padding: 16px 32px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-size: 16px;
      margin: 4px 2px;
      transition-duration: 0.4s;
      cursor: pointer;
    }
    
    .button1 {
      background-color: green; 
      color: black; 
      border: 2px solid green;
    }
    
    .button1:hover {
      background-color: #fc0303;
      color: white;
    }
  </style>

  <!-- Checkbox -->
  <style>
    /* The container */
    .container {
        display: block;
        position: relative;
        padding-left: 35px;
        margin-bottom: 12px;
        cursor: pointer;
        font-size: 22px;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    
    /* Hide the browser's default checkbox */
    .container input {
        position: absolute;
        opacity: 0;
        cursor: pointer;
        height: 0;
        width: 0;
    }
    
    /* Create a custom checkbox */
    .checkmark {
        position: absolute;
        top: 0;
        left: 0;
        height: 25px;
        width: 25px;
        background-color: #eee;
    }
    
    /* On mouse-over, add a grey background color */
    .container:hover input ~ .checkmark {
        background-color: #ccc;
    }
    
    /* When the checkbox is checked, add a blue background */
    .container input:checked ~ .checkmark {
        background-color: #2196F3;
    }
    
    /* Create the checkmark/indicator (hidden when not checked) */
    .checkmark:after {
        content: "";
        position: absolute;
        display: none;
    }
    
    /* Show the checkmark when checked */
    .container input:checked ~ .checkmark:after {
        display: block;
    }
    
    /* Style the checkmark/indicator */
    .container .checkmark:after {
        left: 9px;
        top: 5px;
        width: 5px;
        height: 10px;
        border: solid white;
        border-width: 0 3px 3px 0;
        -webkit-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
        transform: rotate(45deg);
    }
    </style>

    </head>
    <body>

        <h2> 
            <div style = "position:absolute; left:80px; top:100px;">    <!-- Posizione testo --> 
                <font size="">Con che cosa vuoi il tuo tacos?</font>   <!-- Grandezza testo --> 
            </div>
        </h2>

        <!-- Inserimento dati ordinazione --> 
        <form method="post" style = "position:absolute; left:80px; top:200px;">

            <label for="nome">TAVOLO: </label>
            <input type="text" id="tavolo" name="tavolo"><br>

            <label class="container">Taco con
            <input type="checkbox" name="tacos[]" value="carne"> Carne
            <span class="checkmark"></span>
            </label>

            <label class="container">Taco con
            <input type="checkbox" name="tacos[]" value="pollo"> Pollo
            <span class="checkmark"></span>
            </label>

            <label class="container">Taco con
            <input type="checkbox" name="tacos[]" value="pesce"> Pesce
            <span class="checkmark"></span>
            </label>


            <input type="submit" name="submit" value="Invia">
        </form>
        
        <!-- Opzioni button --> 
        <button onclick="location.href='http://localhost:8091'" class="button button1">Indietro</button>

    </body>
</html>

