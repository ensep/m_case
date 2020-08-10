function getMaxValue(data, target) {
    function iter(index, bag, weight, total) {
        if (weight > target) return;
        if (weight === target) {
            if (!result || total < result.total) result = { bag, weight, total };
            return;
        }
        let temp = [...bag];
        temp[index]++;
        iter(index, temp, weight + data[index].kg, total + data[index].price);
        if (++index >= data.length) return;
        iter(index, bag, weight, total);
    }

    var result;
    iter(0, data.map(_ => 0), 0, 0);
    return result;
}

let carrotTypes = [{kg: 5, price: 100}, {kg: 7, price: 150}, {kg: 3, price: 70}], //types
    bagCapacity = 36, // kg
    bag = getMaxValue(carrotTypes, bagCapacity);

console.log(bag);