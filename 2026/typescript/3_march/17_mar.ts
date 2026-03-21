// Map , Filter and Reduce methods in javascript

const list = [1,2,3,4,5];

function mapExample(list: number[]): number[] {
    const mapResult: number[] = list.map((n) => n * 2);
    return mapResult;
};

console.log("Map result:", mapExample(list));

function filterExample(list: number[]): number[] {
    const filterResult: number[] = list.filter((n) => n % 2 == 0);
    return filterResult;
}

console.log("Filter result:", filterExample(list));

function reduceExample(list: number[]): number {
    const reduceResult: number = list.reduce((a, b) => a + b );
    return reduceResult;
};

console.log("Reduce result:", reduceExample(list));