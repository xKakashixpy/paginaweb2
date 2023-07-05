function moveCard(card) {
    card.style.transform = 'translateY(-5px)';
    card.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
  }
  
  function resetCard(card) {
    card.style.transform = 'none';
    card.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
  }