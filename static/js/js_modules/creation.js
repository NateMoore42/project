function generateNumber() {
  return Math.floor(Math.random() * 13) + 7;
}

$(document).ready(function() {
  var race = $("#id_race");
  var subrace = $("#id_subrace");
  var flight = $("#id_can_fly");
  var alignment = $("#id_alignment");
  var background = $("#id_background");

  var language = $("#id_language");
  var c_class = $("#id_c_class").select2();
  var gender = $("#id_gender").select2({minimumResultsForSearch: Infinity})

  var lvl = $("#id_level");
  var dex = $("#id_dexterity");
  var wis = $("#id_wisdom");
  var cha = $("#id_charisma");
  var str = $("#id_strength");
  var con = $("#id_constitution");
  var inte = $("#id_intelligence");
  var dexVal = $(dex).val();
  var wisVal = $(wis).val();
  var chaVal = $(cha).val();
  var strVal = $(str).val();
  var conVal = $(con).val();
  var intVal = $(inte).val();


  $("#roll_dex").click(function() {
    dex.val(generateNumber());
    return dexVal;
  });

  $("#roll_wis").click(function() {
    wis.val(generateNumber());
    return wisVal;
  });

  $("#roll_int").click(function() {
    inte.val(generateNumber());
    return intVal;
  });

  $("#roll_str").click(function() {
    str.val(generateNumber());
    return strVal;
  });

  $("#roll_con").click(function() {
    con.val(generateNumber());
    return conVal;
  });

  $("#roll_cha").click(function() {
    cha.val(generateNumber());
    return chaVal;
  });

  $('.skillsField').change(function(event) {
    if ($(this).val().length > 3) {
      $(this).prop('disabled', true);
    };
  });

})
