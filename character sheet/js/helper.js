/**
 * 模拟投骰子，提供多种类型及内嵌修正值
 */
castDice = function (mode = null) {
    // 获取修正值
    [mode, shift] = (mode + "+0").split("+");
    // 获取投掷次数及骰子类型，大小写不敏感
    [times, dice] = mode.toLocaleLowerCase().split("d");
    ret = []
    // judge dice
    if (["4", "6", "10", "8", "12", "20"].indexOf(dice) != -1) {
        // cast dice
        for (let _ = 0; _ < Number(times); _++) {
            ret.push(randInt(1, Number(dice)));
        }
        return sum(ret) + Number(shift);
    } else if ([times, dice, shift] == ["1", "2", "0"]) {
        // 1d2
        for (let _ = 0; _ < Number(times); _++) {
            ret.push(randInt(1, 6) % 2);
        }
        return sum(ret) + Number(shift);
    } else if ([times, dice, shift] == ["1", "3", "0"]) {
        // 1d3
        for (let _ = 0; _ < Number(times); _++) {
            ret.push(Math.ceil(randInt(1, 6) / 2));
        }
        return sum(ret) + Number(shift);
    } else if ([times, dice, shift] == ["1", "100", "0"]) {
        // 1d100
        for (let _ = 0; _ < 2; _++) {
            ret.push(randInt(1, 10));
        }
        return ret[0] * 10 + ret[1];
    } else {
        return "Error dice!";
    }
}

/**
 * 计算属性调整值
 */
abilityModifiers = function (value) {
    return num2str(Math.floor((value - 10) / 2));
}

/**
 * 产生[a,b]之间的随机整数
 * link:https://www.cnblogs.com/starof/p/4988516.html
 */
randInt = function (a, b) {
    return parseInt(Math.random() * (b - a + 1) + a, 10);
}

/**
 * 数组求和
 * link:http://www.cnblogs.com/younylight/p/7724733.html
 */
sum = function (array) {
    var ret = 0;
    array.forEach(element => {
        ret += element;
    });
    return ret;
}

/**
 * 数字转字符串，若为正数则带+号
 */
num2str = function (num) {
    if (num > 0) {
        ret = "+" + num.toString();
    } else {
        ret = num.toString();
    }
    return ret;
}

/**
 * 属性缩写映射表
 */
lookforAttr = function (attr) {
    switcher = {
        "Str":".Strength",
        "Dex":".Dexterity",
        "Con":".Constitution",
        "Int":".Intellgence",
        "Wis":".Wisdom",
        "Cha":".Charisma"
    };
    return switcher[attr];
}

/**
 * 计算等级
 */
levelupRequiredExp = function (level) {
    switcher = {
        "1": 0,
        "2": 300,
        "3": 900,
        "4": 2700,
        "5": 6500,
        "6": 14000,
        "7": 23000,
        "8": 34000,
        "9": 48000,
        "10": 64000,
        "11": 85000,
        "12": 100000,
        "13": 120000,
        "14": 140000,
        "15": 165000,
        "16": 195000,
        "17": 225000,
        "18": 265000,
        "19": 305000,
        "20": 355000
    };
    return switcher[level];
}

/**
 * 计算熟练加值
 */
proficiencyBonus = function (value) {
    return Math.ceil(value / 4) + 1;
}
