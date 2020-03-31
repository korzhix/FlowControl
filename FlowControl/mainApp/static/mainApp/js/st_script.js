let ctx = document.getElementById('myChart1').getContext('2d');
let ctx2 = document.getElementById('myChart2').getContext('2d');

// Прием данных

let subjects = document.getElementsByClassName('schadule-string')[0];
subjects = subjects.innerHTML.trim();
subjects = JSON.parse(subjects);

let current_balls = document.getElementsByClassName('current-scores-string')[0];
current_balls = current_balls.innerHTML.trim();
current_balls = JSON.parse(current_balls);

let max_balls = document.getElementsByClassName('max-current-scores-string')[0];
max_balls = max_balls.innerHTML.trim();
max_balls = JSON.parse(max_balls);

// Обработка данных
/*
for(let i = 0; i < current_balls.length; i++){
    current_balls[i] = Number.parseInt(current_balls[i]);
    max_balls[i] = Number.parseInt(max_balls[i]);
}
let lost_balls = [];
for (let i = 0; i < max_balls.length; i++){
    lost_balls.push(-(max_balls[i]-current_balls[i]));
};

let lost_color = [];
let got_color = [];
let lost_border = [];
let got_border = [];

for (let i = 0; i < lost_balls.length; i++){
    lost_color.push('rgba(255, 0, 0, 0.2)');
    lost_border.push('rgba(255, 0, 0, 0.8)');
    got_color.push('rgba(0, 255, 51, 0.2)');
    got_border.push('rgba(0, 162, 32, 1)');
};


let myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: subjects,
        datasets: [{
            label: '',
            data: current_balls,
            backgroundColor: [
                'rgba(255, 0, 0, 0.1)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
            ],
            pointBackgroundColor: 'rgba(255, 0, 0, 0.3)',
            pointBorderColor: 'rgba(255, 0, 0, 0.6)',
            borderWidth: 3,

        }]
    },
    options: {
        legend: {
            display: false,
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    suggestedMax: 100,
                    stepSize: 20,
                }
            }]
        }
    }
});

let myChartBar = new Chart(ctx2, {
    type: 'horizontalBar',
    data: {
        labels: subjects,
        datasets: [{
            label: 'Потеряно',
            data: lost_balls,
            backgroundColor: lost_color,
            borderColor: lost_border,
            borderWidth: 1
        },{
            label: 'Получено',
            data: current_balls,
            backgroundColor: got_color,
            borderColor: got_border,
            borderWidth: 1
        },]
    },
    options: {
        scales: {
            xAxes: [{
                stacked: true,
            }],
            yAxes: [{
                stacked: true,
                ticks: {
                    suggestedMax: 50,
                }
            }]
        }
    }
}); */