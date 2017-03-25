function generateNumber() {
  return Math.floor(Math.random() * 20) + 1;
}
function rerollAll() {
  document.getElementById('id_intelligence').value = generateNumber()
  document.getElementById('id_dexterity').value = generateNumber()
  document.getElementById('id_charisma').value = generateNumber()
  document.getElementById('id_constitution').value = generateNumber()
  document.getElementById('id_wisdom').value = generateNumber()
  document.getElementById('id_strength').value = generateNumber()
    }



document.getElementById('id_intelligence').value = generateNumber()
document.getElementById('id_dexterity').value = generateNumber()
document.getElementById('id_charisma').value = generateNumber()
document.getElementById('id_constitution').value = generateNumber()
document.getElementById('id_wisdom').value = generateNumber()
document.getElementById('id_strength').value = generateNumber()
