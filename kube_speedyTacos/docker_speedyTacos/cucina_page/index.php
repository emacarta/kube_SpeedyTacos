<?php
    function connectToDB() {
        $host = "10.102.222.175";
        $dbname = "ORDINI_database";
        $user = "SQLuser";
        $password = "1234";
        try {
            $conn = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
            $conn->setattribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            return $conn;
        } catch (PDOException $e) {
            echo "Connessione al database fallita: " . $e->getMessage();
            exit;
        }
    }
    if(isset($_POST['delete'])) {
        $conn = connectToDB();
        $query = "DELETE FROM ORDINAZIONI";
        $stmt = $conn->prepare($query);
        $stmt->execute();
        $conn = null;
    }
?>
<!DOCTYPE html>
<html>
<head>
    <title>Comande Cucina</title>
</head>
<body>
    <form method="post">
        <input type="submit" name="submit" value="Visualizza ordini">
        <input type="submit" name="delete" value="Elimina" onclick="return confirm('Sei sicuro di voler eliminare tutti i dati dalla tabella?')">
    </form>
    <?php
        if(isset($_POST['submit'])) {
            $conn = connectToDB();
            $query = "SELECT * FROM ORDINAZIONI";
            $stmt = $conn->prepare($query);
            $stmt->execute();
            $result = $stmt->fetchAll();
            print_r($result);
            $conn = null;
        }
    ?>
</body>
</html>