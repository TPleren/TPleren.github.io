// script.js
const flashcards = [
    { front: "Front of Card 1", back: "Back of Card 1" },
    { front: "Front of Card 2", back: "Back of Card 2" },
    // Add more flashcards as needed
];

const flashcardContainer = document.getElementById('flashcard-container');
const nextCardButton = document.getElementById('next-card');
const showBackButton = document.getElementById('show-back');
const currentFlashcard = document.getElementById('current-flashcard');

let currentCardIndex = -1;

function showCard() {
    currentCardIndex = (currentCardIndex + 1) % flashcards.length;
    const card = flashcards[currentCardIndex];
    currentFlashcard.innerHTML = card.front;
    showBackButton.style.display = 'block';
    nextCardButton.style.display = 'none';
}

function showBack() {
    const card = flashcards[currentCardIndex];
    currentFlashcard.innerHTML = card.back;
    showBackButton.style.display = 'none';
    nextCardButton.style.display = 'block';
}

showBackButton.addEventListener('click', showBack);
nextCardButton.addEventListener('click', showCard);

// Initially, show the first card
showCard();
