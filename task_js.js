function count() {
    let count = 0
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < i; j++) {
            count++;
        }
    }

    return count;
}


console.log(count());