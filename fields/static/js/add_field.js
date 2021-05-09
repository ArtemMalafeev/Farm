const user = document.getElementById('id_user')
const name = document.getElementById('id_name')
const square_field = document.getElementById('id_square')
const cadastral_field = document.getElementById('id_cadastral_number')
const stop = document.getElementById('stopEditPolyline')
const form = document.getElementById('p-form')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

coordinate = [];
square = 0;

ymaps.ready(init);

// Рисуем многоугольник и возвращаем координаты списком по нажатию кнопки "Завершить редактирование"
function init () {
    var myMap = new ymaps.Map("map", {
        center: [44.781528, 44.165024],
        zoom: 15,
        type: 'yandex#satellite'
    }),

    firstButton = new ymaps.control.Button({
        data: {
            content: "<b style='color: #1E90FF;'>Сохранить объект</b>",
            title: "Нажми, чтобы сохранить",
            },
        options: {
            maxWidth: [28, 150, 178]
            }
        });

    secondButton = new ymaps.control.Button({
        data: {
            content: "<b style='color: #1E90FF;'>Удалить объект</b>",
            title: "Нажми, чтобы отменить",
            },
        options: {
            maxWidth: [28, 150, 178],
            }
        });

    myMap.controls.add(firstButton);
    myMap.controls.add(secondButton);
    myMap.controls.remove('trafficControl');

    polygon = new ymaps.GeoObject({
        geometry: {
            type: "Polygon",
            coordinates: []
        }
    });

    myMap.geoObjects.add(polygon);
    polygon.editor.startDrawing();

    // Сохраняем объект
    firstButton.events.add('press',
        function () {
            polygon.editor.stopEditing();
            coordinate = polygon.geometry.getCoordinates();

            // Посчитать площадь
            ymaps.ready(['util.calculateArea']).then(function () {
                var myPolygon = new ymaps.Polygon(coordinate);
                var area = ymaps.util.calculateArea(myPolygon);

                square = Math.floor(area);
                square_ha = (square / 10000).toFixed(2);
//                square_ha =  square / 10000;

                $('#id_square').val(square);
                $('#id_coordinate').val(coordinate);
                $('#id_square_ha').val(square_ha)

                firstButton.deselect()
            }
        );
    })

    secondButton.events.add('press',
        function () {
            myMap.geoObjects.remove(polygon);
            $('#id_square').val('');
            $('#id_coordinate').val('');
            $('#id_square_ha').val('')
            secondButton.select();

            polygon = new ymaps.GeoObject({
                geometry: {
                type: "Polygon",
                coordinates: []
            }
        }
    );

        myMap.geoObjects.add(polygon);
        polygon.editor.startDrawing();
    });
}