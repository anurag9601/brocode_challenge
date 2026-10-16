function luhnAlgorithm(n: number){
    let totalSum: number = n % 10;
    let iCount = 0;
    n = Math.floor(n / 10);
    while(n > 0){
        const currNum = n % 10;
        if(iCount % 2 == 0){
            totalSum = totalSum + (currNum * 2);
        }else{
            totalSum = totalSum + currNum;
        };
        n = Math.floor(n / 10);
        iCount = iCount + 1;
    };
    return totalSum % 10 == 0 ? true : false;
};

// console.log(luhnAlgorithm(4111111111111111));
// console.log(luhnAlgorithm(6451623895684318));
// console.log(luhnAlgorithm(6451623895684318));

function bedTime(...args: string[][]){
    let result: string[] = [];

    function calculateSleepTime(alarmTime: string, sleepDuration: string){
        if(alarmTime == sleepDuration){
            return "00:00";
        };

        let hour: number = 0;
        let min: number = 0;

        let [alarmHour, alarmMin]: number[] = alarmTime.split(":").map((n) => Number(n));
        let [sleepHour, sleepMin]: number[] = sleepDuration.split(":").map((n) => Number(n));
        // calculate minutes
        hour = hour + Math.floor((alarmMin + sleepMin) / 60);
        min = (alarmMin + sleepMin) % 60;

        // calculate hours
        let hourDiff = (alarmHour - sleepHour);

        if(hourDiff < 0){
            hour = 24 - ( hourDiff * -1 )
        }else {
            hour = hour + hourDiff
        };

        return `${ hour < 10 ? "0" + hour : hour }:${ min < 10 ? "0" + min : min }`;
    };

    for(let time of args){
        let calculatedTime = calculateSleepTime(time[0], time[1]);

        result.push(calculatedTime);
    };

    return result;
};

console.log(bedTime(["07:50", "07:50"]))
console.log(bedTime(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]));
