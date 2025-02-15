function current_streak(currentDate: string, dateObject: { [key: string]: string }[]) {
    let streakCount = 0

    let monthDaysLst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    const dates = dateObject.map((e) => Object.values(e)[0])
    if (!dates.includes(currentDate)) {
        return streakCount;
    }

    let year: number = 0;
    let month: number = 0;
    let day: number = 0;

    for (let date of dates) {
        let splitDate = date.split("-").map((e) => parseInt(e));
        if (year == 0 || splitDate[0] !== year || splitDate[1] !== month || splitDate[2] !== day) {
            year = month == 12 && day == 31 ? splitDate[0] + 1 : splitDate[0]
            month = monthDaysLst[month - 1] == day ? month == 12 ? 1 : splitDate[1] + 1 : splitDate[1]
            day = monthDaysLst[month - 1] == splitDate[2] ? 1 : splitDate[2] + 1
            streakCount = 1
        }
        else {
            year = month == 12 && day == 31 ? splitDate[0] + 1 : splitDate[0]
            month = monthDaysLst[month - 1] == day ? month == 12 ? 1 : month + 1 : month
            day = monthDaysLst[month - 1] == splitDate[2] ? 1 : splitDate[2] + 1
            streakCount += 1
        }
    }

    return streakCount
}

// console.log(current_streak("2019-09-23", [
//     {
//         "date": "2019-09-18"
//     },
//     {
//         "date": "2019-09-19"
//     },
//     {
//         "date": "2019-09-21"
//     },
//     {
//         "date": "2019-09-22"
//     },
//     {
//         "date": "2019-09-23"
//     }
// ]))
// console.log(current_streak("2019-09-25", [
//     {
//         "date": "2019-09-16"
//     },
//     {
//         "date": "2019-09-17"
//     },
//     {
//         "date": "2019-09-21"
//     },
//     {
//         "date": "2019-09-22"
//     },
//     {
//         "date": "2019-09-23"
//     }
// ]))