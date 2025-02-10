<?php
/**
 * PHP Categorized Quiz Application
 * Author: Munoim Shahriar
 * Date: Feb 25
 * Description: A simple PHP quiz application where users select a category and answer a randomly chosen question.
 */

session_start();

// Define Quiz Questions (Manually selected interesting topics)
$quizArray = [
    'Technology' => [
        [
            'question' => 'Which of the following are programming languages?',
            'answers' => ['Python', 'Java', 'HTML', 'CSS'],
            'correct' => ['Python', 'Java']
        ],
        [
            'question' => 'What does HTML stand for?',
            'answers' => ['Hyper Transfer Markup Language', 'Hyper Text Markup Language', 'High Tech Markup Language', 'None of the above'],
            'correct' => ['Hyper Text Markup Language']
        ]
    ],
    'Science' => [
        [
            'question' => 'Which of these are planets in our solar system?',
            'answers' => ['Earth', 'Mars', 'Sun', 'Venus'],
            'correct' => ['Earth', 'Mars', 'Venus']
        ],
        [
            'question' => 'What is H2O commonly known as?',
            'answers' => ['Oxygen', 'Water', 'Hydrogen Peroxide', 'Acid'],
            'correct' => ['Water']
        ]
    ],
    'History' => [
        [
            'question' => 'Who was the first President of the United States?',
            'answers' => ['George Washington', 'Abraham Lincoln', 'Thomas Jefferson', 'John Adams'],
            'correct' => ['George Washington']
        ],
        [
            'question' => 'In which year did World War II end?',
            'answers' => ['1945', '1939', '1918', '1950'],
            'correct' => ['1945']
        ]
    ]
];

// Handle Form Submission
$selectedCategory = $_POST['category'] ?? '';
$selectedAnswers = $_POST['answers'] ?? [];
$feedback = '';
$selectedQuestion = null;

// Randomly Select a Question if Category is Chosen
if (!empty($selectedCategory) && isset($quizArray[$selectedCategory])) {
    $questions = $quizArray[$selectedCategory];
    $selectedQuestion = $questions[array_rand($questions)];
}

// Validate and Compare Answers
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $selectedQuestion) {
    $correctAnswers = $selectedQuestion['correct'];
    $isCorrect = !array_diff($correctAnswers, $selectedAnswers) && !array_diff($selectedAnswers, $correctAnswers);
    $feedback = $isCorrect 
        ? '<p class="correct"> Well done! You got it right.</p>' 
        : '<p class="incorrect"> Oops! The correct answers are: ' . implode(', ', $correctAnswers) . '</p>';
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Quiz App</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        .correct { color: green; font-weight: bold; }
        .incorrect { color: red; font-weight: bold; }
    </style>
    <script>
        function validateForm() {
            let category = document.getElementById('category').value;
            if (!category) {
                alert('Please select a category before proceeding.');
                return false;
            }
            return true;
        }
    </script>
</head>
<body>
    <h1>PHP Quiz App</h1>
    <p><strong>Author:</strong> Munoim Shahriar</p>
    <p>Test your knowledge in various topics. Select a category and answer a random question.</p>

    <form method="POST" onsubmit="return validateForm();">
        <label for="category">Select a Category:</label>
        <select name="category" id="category">
            <option value="">-- Choose a category --</option>
            <?php foreach ($quizArray as $category => $questions): ?>
                <option value="<?= htmlspecialchars($category); ?>" <?= $category == $selectedCategory ? 'selected' : ''; ?>><?= htmlspecialchars($category); ?></option>
            <?php endforeach; ?>
        </select>
        <button type="submit">Start Quiz</button>
    </form>

    <?php if ($selectedQuestion): ?>
        <h2><?= htmlspecialchars($selectedQuestion['question']); ?></h2>
        <form method="POST">
            <?php foreach ($selectedQuestion['answers'] as $answer): ?>
                <label>
                    <input type="checkbox" name="answers[]" value="<?= htmlspecialchars($answer); ?>"> <?= htmlspecialchars($answer); ?>
                </label><br>
            <?php endforeach; ?>
            <input type="hidden" name="category" value="<?= htmlspecialchars($selectedCategory); ?>">
            <button type="submit">Submit Answer</button>
        </form>
    <?php endif; ?>

    <?= $feedback; ?>
    <hr>
    <footer>
        <p>Developed by <strong>Munoim Shahriar</strong> | PHP Quiz App | COMP1230</p>
        <p>&copy; <?= date('Y'); ?> All Rights Reserved</p>
    </footer>
    <?php show_source(__FILE__); ?>
</body>
</html>
