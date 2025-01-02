function timeDifference(firstPlace: string, dateTime: string, secondPlace: string): string {
    const months: string[] = ["January", "February", "March", "April", "May", "June", "July", "August", "Sepetember", "October", "November", "December"];
    let monthDays: number[] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    const timeZone: { [place: string]: string } = {
        "Los Angeles": "- 08:00",
        "New York": "- 05:00",
        "Caracas": "- 04:30",
        "Buenos Aires": "- 03:00",
        "London": "+ 00:00",
        "Rome": "+ 01:00",
        "Moscow": "+ 03:00",
        "Tehran": "+ 03:30",
        "New Delhi": "+ 05:30",
        "Beijing": "+ 08:00",
        "Canberra": "+ 10:00"
    }

    const splitDateTime = dateTime.split(" ");
    let min: number = parseInt(splitDateTime[splitDateTime.length - 1].split(":")[1]);
    let hour: number = parseInt(splitDateTime[splitDateTime.length - 1].split(":")[0])
    let year: number = parseInt(splitDateTime[splitDateTime.length - 2]);
    let date: number = parseInt(splitDateTime[1].slice(0, -1));
    let month: number = months.indexOf(splitDateTime[0]) + 1;

    if (year % 400 == 0 || year % 4 == 0 && year % 100 !== 0) {
        monthDays[1] = 29
    }

    let dicCurrentDateTime: { [type: string]: number } = {
        "min": min,
        "hour": hour,
        "date": date,
        "month": month,
        "year": year,
    };

    let addingTimeGap: number[];
    let addMin: number = 0;
    let addHour: number = 0;
    const firstPlaceTimeGap = timeZone[firstPlace];
    const secondPlaceTimeGap = timeZone[secondPlace];

    const splitFirstPlaceTimeGap = firstPlaceTimeGap.split(":")
    const splitSecondPlaceTimeGap = secondPlaceTimeGap.split(":");

    if (firstPlaceTimeGap[0] == "-" && secondPlaceTimeGap[0] == "+") {
        const sumOfMin: number = parseInt(splitFirstPlaceTimeGap[1]) + parseInt(splitSecondPlaceTimeGap[1]);

        addHour = parseInt(splitFirstPlaceTimeGap[0].slice(2)) + parseInt(splitSecondPlaceTimeGap[0].slice(2));

        if (sumOfMin > 60) {
            addMin = sumOfMin % 60;
            addHour = Math.floor(sumOfMin / 60);
        }
    } else if (firstPlaceTimeGap[0] == "+" && secondPlaceTimeGap[0] == "-") {
        const totalMin: number = parseInt(splitSecondPlaceTimeGap[1])
        if (totalMin == 0) {
            addHour = -parseInt(splitSecondPlaceTimeGap[0].slice(2));
        } else if (totalMin > 60) {
            addMin = totalMin % 60;
            addHour = Math.floor(totalMin / 60);
        } else {
            addMin = totalMin % 60
        }
    } else if (firstPlaceTimeGap[0] == "-" && secondPlaceTimeGap[0] == "-") {
        let sumOfMin: number = parseInt(splitSecondPlaceTimeGap[1])
        if (sumOfMin == 0) {
            addHour = -parseInt(splitSecondPlaceTimeGap[0].slice(2));
        } else if (sumOfMin > 60) {
            addMin = sumOfMin % 60;
            addHour = Math.floor(sumOfMin / 60);
        } else {
            addMin = sumOfMin % 60
        }
    } else if (firstPlaceTimeGap[0] == "+" && secondPlaceTimeGap[0] == "+") {
        const sumOfMin: number = parseInt(splitSecondPlaceTimeGap[1])
        if (sumOfMin == 0) {
            addHour = parseInt(splitSecondPlaceTimeGap[0].slice(2));
        } else if (sumOfMin > 60) {
            addMin = sumOfMin % 60;
            addHour = Math.floor(sumOfMin / 60);
        } else {
            addMin = sumOfMin % 60
        }
    }

    addingTimeGap = [addHour, addMin];

    console.log(addingTimeGap)

    let remain: number = 0;

    for (let type in dicCurrentDateTime) {
        if (type == "min") {
            let minSum = dicCurrentDateTime[type] + addingTimeGap[1]
            minSum = minSum > 0 ? minSum : -minSum
            if (minSum > 60) {
                dicCurrentDateTime[type] = minSum % 60
                remain = Math.floor(minSum / 60);
            } else {
                dicCurrentDateTime[type] = minSum
                remain = 0
            }
        } else if (type == "hour") {
            let hourSum = dicCurrentDateTime[type] + addingTimeGap[0] + remain;
            hourSum = hourSum > 0 ? hourSum : -hourSum
            if (hourSum == 24 && dicCurrentDateTime["min"] > 0) {
                dicCurrentDateTime[type] = hourSum % 24
                remain = Math.floor(hourSum / 24);
            } else if (hourSum > 24) {
                dicCurrentDateTime[type] = hourSum % 24
                remain = Math.floor(hourSum / 24);
            } else {
                dicCurrentDateTime[type] = hourSum;
                remain = 0
            }
        } else if (type == "date") {
            let dateSum = dicCurrentDateTime[type] + remain;
            let currentMonthDays = monthDays[month - 1];
            if (currentMonthDays < dateSum) {
                dicCurrentDateTime[type] = dateSum % currentMonthDays
                remain = Math.floor(dateSum / currentMonthDays);
            } else {
                dicCurrentDateTime[type] = dateSum
                remain = 0
            }
        } else if (type == "month") {
            if (remain == 0) {
                break
            }
            let monthSum = dicCurrentDateTime[type] + remain;
            if (monthSum > 12) {
                dicCurrentDateTime[type] = monthSum % 12;
                remain = Math.floor(monthSum / 12);
            } else {
                dicCurrentDateTime[type] = monthSum
                remain = 0
            }
        } else if (type == "year") {
            if (remain == 0) {
                break
            }
            let yearSum = dicCurrentDateTime[type] + remain;
            dicCurrentDateTime[type] = yearSum
        }
    }

    return `${dicCurrentDateTime.year}-${dicCurrentDateTime.month}-${dicCurrentDateTime.date} ${dicCurrentDateTime.hour.toString().length == 1 ? "0" + dicCurrentDateTime.hour : dicCurrentDateTime.hour}:${dicCurrentDateTime.min.toString().length == 1 ? "0" + dicCurrentDateTime.min : dicCurrentDateTime.min}`
};

// console.log(timeDifference("Los Angeles", "April 1, 2011 23:23", "Canberra"));
// console.log(timeDifference("Los Angeles", "July 31, 1983 23:01", "New York"));
// console.log(timeDifference("London", "July 31, 1983 23:01", "Rome"));
// console.log(timeDifference("New York", "December 31, 1970 13:40", "Beijing"));

function validRondo(input_str: string): boolean {
    const alphabets: string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    if (input_str.length == 0 || input_str.length == 1 || input_str[0] !== alphabets[0] && input_str[-1] !== alphabets[0]) return false;

    let toggle: number = 0;
    let alphaIndex: number = 1;
    for (let letter of input_str) {
        if (toggle % 2 == 0) {
            if (letter != alphabets[0]) {
                return false;
            }
            toggle++;
        } else if (toggle % 2 != 0) {
            if (letter != alphabets[alphaIndex]) {
                return false;
            }
            alphaIndex++;
            toggle++;
        }
    }
    return true;
};

// console.log(validRondo("ABACADAEAFAGAHAIAJA"));
// console.log(validRondo("ABBACCA"));
// console.log(validRondo("ACAC"));
// console.log(validRondo("ABACADAEAFAGAHAA"));
// console.log(validRondo("A"));
// console.log(validRondo("ABACA"));
// console.log(validRondo("ABA"))