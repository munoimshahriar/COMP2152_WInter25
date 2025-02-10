<?php
// Array of numbers for demonstration (includes negative, zero, and positive values)
$values = [-3, 0, 5, 10, 15];

// Membership type for demonstration in the switch-case
$userMembership = "basic";

echo "=== FOR LOOP EXAMPLE ===<br>";

foreach ($values as $index => $value) {
    echo "Processing Value: $value<br>";

    // Skip to the next iteration if the value is negative
    if ($value < 0) {
        echo " -> Skipping negative number...<br>";
        continue;
    }

    // End the loop if the value is zero
    if ($value === 0) {
        echo " -> Found zero, exiting loop...<br>";
        break;
    }

    // Highlight when the value is considered a "bulk quantity"
    if ($value >= 10) {
        echo " -> Large value detected: $value<br>";
    }
}

echo "<br>";
echo "=== MEMBERSHIP CHECK (SWITCH CASE) ===<br>";

switch ($userMembership) {
    case "none":
        echo "No membership benefits available.<br>";
        break;
    case "basic":
        echo "Basic membership benefits apply.<br>";
        break;
    case "premium":
        echo "Premium membership benefits apply.<br>";
        break;
    default:
        echo "Unknown membership type.<br>";
}

echo "<br>";
echo "=== WHILE LOOP DEMO ===<br>";

$count = 0;
while ($count < 3) {
    echo "While Loop Step: $count<br>";
    $count++;

    // Skip the final output message for a specific case
    if ($count == 2) {
        echo " -> Skipping special output on this step.<br>";
        continue;
    }

    echo "Completed step $count in the loop.<br>";
}

echo "<br>";
echo "=== DO-WHILE LOOP EXAMPLE ===<br>";

$doCounter = 0;
do {
    echo "Running Do-While Step: $doCounter<br>";
    $doCounter++;
} while ($doCounter < 2);

echo "<br>";
echo "=== COMPARISON DEMO ===<br>";

$numString = "5"; // String representation of the number 5

// Loose comparison
if ($numString == 5) {
    echo "'$numString' loosely equals 5.<br>";
} else {
    echo "'$numString' does not loosely equal 5.<br>";
}

// Strict comparison
if ($numString === 5) {
    echo "'$numString' strictly equals 5.<br>";
} else {
    echo "'$numString' does not strictly equal 5.<br>";
}

echo "<br>";
echo "=== LOGICAL OPERATORS DEMO ===<br>";

$totalItems = 7;
$discountAvailable = true;

// Checking for combined conditions
if ($totalItems > 7 && $discountAvailable) {
    echo "Eligible for a bulk AND discount offer!<br>";
} else {
    echo "Not eligible for combined discount.<br>";
}

echo "<br>";
echo "=== CONDITIONAL EXIT EXAMPLE ===<br>";

$exitEarly = false;

if ($exitEarly) {
    echo "Terminating script early as requested.<br>";
    exit;
}

echo "Script continues as exit condition was not met.<br>";
echo "<br>=== END OF SCRIPT ===<br>";
