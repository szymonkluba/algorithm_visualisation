document.addEventListener('DOMContentLoaded', function () {
            let arraySize = getMaxArraySize();
            let arraySizeInput = document.getElementById('arraySize')
            arraySizeInput.value = arraySize;
            arraySizeInput.addEventListener('input', function (event) {
                console.log(event.target.value);
                if (parseInt(event.target.value) > arraySize) {
                    console.log(event.target.value);
                    event.target.value = arraySize.toString();
                    alert(`Maximum array size is ${arraySize} due to aesthetics reason`)
                }
            });
            window.addEventListener('resize', function () {
                let maxArraySize = getMaxArraySize();
                let arraySizeInput = document.getElementById('arraySize')
                if (parseInt(arraySizeInput.value) > maxArraySize) {
                    arraySizeInput.value = maxArraySize;
                }
                getArray()
            })
        });

        var socket = io();

        socket.on('connect', function () {
            socket.emit('my event', {data: 'I\'m connected!'});
        });

        socket.on('generated array', data => {
            generateArray(data);
        });

        socket.on('update array', data => {
            generateArray(data);
            if (data.index1) {
                let bar = document.getElementById('bar' + data.index1.toString())
                bar.setAttribute('class', 'bar current')
            }
            if (data.index2) {
                let bar = document.getElementById('bar' + data.index2.toString())
                bar.setAttribute('class', 'bar swapped')
            }
        });

        socket.on('choose algorithm', function () {
            alert('Please choose the algorithm you want to visualize.')
        })

        function generateArray(data) {
            let canvas = document.getElementById('canvas');
            canvas.innerHTML = ''
            barWidth = (~~(canvas.clientWidth / data.array.length)) - 2;
            for (var i = 0; i < data.array.length; i++) {
                let node = document.createElement('div')
                node.setAttribute('id', 'bar' + i.toString());
                node.setAttribute('class', 'bar regular');
                node.style.width = barWidth.toString() + 'px';
                node.style.height = data.array[i].toString() + '%';
                if (barWidth > 50) {
                    node.innerHTML = data.array[i];
                }
                canvas.appendChild(node);
            }
        }

        function getArray() {
            stopAlgorithm()
            let arraySize = document.getElementById('arraySize').value
            if (!arraySize) {
                arraySize = getMaxArraySize()
            }
            socket.emit('generate array', {"size": arraySize});
        }

        function runAlgorithm() {
            let algorithm = document.getElementById('algorithms').value
            socket.emit('run algorithm', {'algorithm': algorithm})
        }

        function stopAlgorithm() {
            socket.emit('stop algorithm')
        }

        function getMaxArraySize() {
            let canvas = document.getElementById('canvas')
            let width = canvas.clientWidth;
            return ~~(width / 4)
        }

