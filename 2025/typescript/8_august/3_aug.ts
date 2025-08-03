//Creating a function which can give all the possible appointments after taking checkIn time checkOut time and appointment duration

class generateAllPossibleAppointments {
    private timeSlots: string[] = [];

    constructor(private checkIn: string, private checkOut: string, private duration: number) { };

    convertStringTimeInMinutes(time: string): number {
        const [hour, minute] = time.split(":").map(Number);
        return hour * 60 + minute;
    };

    convertMinutesIn24HourStringFormat(minutes: number): string {
        const hour = Math.floor(minutes / 60);
        const minute = minutes % 60;
        return `${hour < 10 ? "0" + hour : hour }:${minutes < 10 ? "0" + minute : minute }`;
    };

    convertMinutesInStandardWatchStringFormat(minutes: number): string {
        let hour = Math.floor(minutes / 60);
        let minute = minutes % 60;

        const period = hour >= 12 ? 'PM' : 'AM';

        if(hour === 0) {
            hour = 12;
        }else if(hour > 12) {
            hour = hour - 12;
        };

        return `${hour < 10 ? "0" + hour : hour }:${minute < 10 ? "0" + minute : minute } ${period}`;
    }

    startGenerating() {
        let startTime = this.convertStringTimeInMinutes(this.checkIn);
        let endTime = this.convertStringTimeInMinutes(this.checkOut);

        // this.timeSlots.push(this.convertMinutesIn24HourStringFormat(startTime))
        this.timeSlots.push(this.convertMinutesInStandardWatchStringFormat(startTime))

        while(startTime < endTime && startTime + this.duration <= endTime) {
            startTime = startTime + this.duration;
            // const currentSlot = this.convertMinutesIn24HourStringFormat(startTime);
            const currentSlot = this.convertMinutesInStandardWatchStringFormat(startTime);
            this.timeSlots.push(currentSlot);
        };

        return this.timeSlots;
    }
};

const timeSlots = new generateAllPossibleAppointments("9:00", "22:00", 45);

console.log(timeSlots.startGenerating());