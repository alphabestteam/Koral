const findSeashellsIndicies = (target , values) => {
    const answer = []

    for (let i = 0; i < values.length; i++){
        for (let j = i; j < values.length; j++){

            if (values[i] + values[j] == target && i != j)
                {
                    answer.push(i, j);
                   
                }
        }
    }
    return answer;
}