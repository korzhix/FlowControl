let ctx = document.getElementById('myChart1').getContext('2d');
let ctx2 = document.getElementById('myChart2').getContext('2d');

// Прием данных
    


// Обработка данных

let subjects = ['История', 'Мат. анализ', 'Физ-ра', 'АиГ', 'ОАиП', 'МЛиДМ', 'Англ. язык'];
let current_balls = [40, 16, 16, 31, 42, 40, 31];
let max_balls = [50, 30, 40, 35, 42, 45, 35];

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
});