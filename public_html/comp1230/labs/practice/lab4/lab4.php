<?php
// Set timezone
date_default_timezone_set('UTC');

// Task 1: Arguments passing and string functions

// Function to demonstrate pass by value
function increaseValue($num)
{
    $num += 10;
    echo "Inside function (pass by value): $num<br>";
}
$myNumber = 5;
increaseValue($myNumber);
echo "Outside function: $myNumber<br><br>";

// Function to demonstrate pass by reference
function increaseReference(&$num)
{
    $num += 10;
    echo "Inside function (pass by reference): $num<br>";
}
increaseReference($myNumber);
echo "Outside function: $myNumber<br><br>";

// String functions
$myText = "Hello, this is Munoim!";
echo "Uppercase: " . strtoupper($myText) . "<br>";
echo "Lowercase: " . strtolower($myText) . "<br>";
echo "String Length: " . strlen($myText) . "<br><br>";

// Task 2: Due Date Check
$due_date = strtotime("Tuesday May 23 2025 20:00:00");
$current_time = time();

if ($current_time > $due_date) {
    echo "<p>Your submission is late!</p>";
} else {
    echo "<p>You still have time!</p>";
}

// Show source code
echo "<hr>";
show_source(__FILE__);
