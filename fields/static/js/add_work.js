const alertBox = document.getElementById('alert-box')
const imgBox = document.getElementById('img-box')
const formJob = document.getElementById('p-form')

const categoryJob = document.getElementById('id_category')
const seasonJob = document.getElementById('id_season')
const startJob = document.getElementById('id_start_job')
const endJob = document.getElementById('id_end_job')
const fieldsJob = document.getElementById('id_fields')
const workersJob = document.getElementById('id_workers')
const commentJob = document.getElementById('id_comment')

const csrfJob = document.getElementsByName('csrfmiddlewaretoken')
const url = ""

const handleAlerts = (type, text) => {
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">${text}</div>`
}

formJob.addEventListener('submit', e=> {
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrfJob[0].value)
    fd.append('category', categoryJob.value)
    fd.append('season', seasonJob.value)
    fd.append('start_job', startJob.value)
    fd.append('end_job', endJob.value)
    fd.append('fields', fieldsJob.value)
    fd.append('workers', workersJob.value)
    fd.append('comment', commentJob.value)

    $.ajax({
        type: 'POST',
        url: '/fields/work/add/',
        enctype: 'multipart/form-data',
        data: fd,
        success: function(response) {
            handleAlerts('success', 'Работа успешно добавлена!')
            console.log('----');
            console.log(response);
        },
        error: function(error) {
            handleAlerts('danger', 'Не добавлено')
            console.log(url);
            console.log(error);
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

