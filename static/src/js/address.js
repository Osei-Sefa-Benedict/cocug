$("#id_district").change(function () {
  var url = $("#StudentRegistrationForm").attr("data-Region-url");
  var districtId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'district': districtId
    },
    success: function (data) {
      $("#id_Region").html(data);
    }
  });

});
$("#id_Region").change(function () {
  var url = $("#StudentRegistrationForm").attr("data-Region-url");
  var RegionId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'Region': RegionId
    },
    success: function (data) {
      $("#id_Ministry").html(data);
    }
  });

});
