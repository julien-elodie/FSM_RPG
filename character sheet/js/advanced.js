/**
 * 属性值计算
 */
$(document).ready(function () {
    $(".CastAttributes").change(function () {
        castAttributes();
        calSavingThrows();
        calSkills();
        calPassiveWisdom();
        calArmorClass();
    })
});

/**
 * 豁免，技能联动熟练加值
 */
$(document).ready(function () {
    const throws = $(".SavingThrows").find("input:radio");
    const skills = $(".Skills").find("input:radio");
    $(throws).bind("mousedown", binding);
    $(skills).bind("mousedown", binding);
});

/**
 * 经验，等级，熟练加值
 */
$(document).ready(function () {
    calLevel();
    calProficiencyBonus();
});

/**
 * 被动感知
 */
$(document).ready(function () {
    
})

/**
 * 手动调整
 */
$(function () {
    $(".ExperiencePoints").change(function () {
        calLevel();
        calProficiencyBonus();
    })
});

/**
 * 投掷属性值
 */
castAttributes = function () {
    rule = $(".CastAttributes").find("option:selected").val();
    attributes = [".Strength", ".Dexterity", ".Constitution", ".Intellgence", ".Wisdom", ".Charisma"];
    switch (rule) {
        case "Original 3d6":
            for (let _ = 0; _ < attributes.length; _++) {
                const element = attributes[_];
                var Value = castDice("3d6")
                $(element).find(".Value").text(Value);
                $(element).find(".Modifier").text(abilityModifiers(Value));
            }
        default:
            break;
    }
}

/**
 * 调整豁免
 */
calSavingThrows = function () {
    const throws = $(".SavingThrows").find("label");
    const attributes = [".Strength", ".Dexterity", ".Constitution", ".Intellgence", ".Wisdom", ".Charisma"];
    for (let _ = 0; _ < throws.length; _++) {
        const element = throws[_];
        const value = $(attributes[_]).find(".Modifier").text();
        $(element).text(value);
    }
}

/**
 * 调整技能
 */
calSkills = function () {
    const skills = $(".Skills").find("label");
    for (let _ = 0; _ < skills.length; _++) {
        const element = skills[_];
        var attributes = $(element).attr("for");
        const value = $(lookforAttr(attributes)).find(".Modifier").text();
        $(element).text(value);
    }
}

/**
 * 联动函数
 */
binding = function (event) {
    var bonus = $(".ProficiencyBonus").find("label");
    var value = $(this).siblings("label");
    var radioChecked = $(this).prop("checked");
    if (radioChecked) {
        str = Number($(value).text()) + Number($(bonus).text());
    } else {
        str = Number($(value).text()) - Number($(bonus).text());
    }
    $(value).text(num2str(str));
    calPassiveWisdom();
}

/**
 * 计算等级
 */
calLevel = function () {
    const exp = $(".ExperiencePoints").val();
    for (let _ = 0; _ < 20; _++) {
        if (levelupRequiredExp(_ + 1) > exp) {
            $(".Level").text(_)
            break;
        } else {
            $(".Level").text(20)
        }
    }
}

/**
 * 计算熟练加值
 */
calProficiencyBonus = function () {
    const level = $(".Level").text();
    var Bonus = $(".ProficiencyBonus").find("label");
    str = proficiencyBonus(level);
    console.log(num2str(str));
    $(Bonus).text(num2str(str));
}

/**
 * 计算被动感知
 */
calPassiveWisdom = function () {
    const bonus = $("#PreceptionBonus").siblings("label");;
    const passwis = $(".PassiveWisdom").find("label");
    str = 10 + Number($(bonus).text());
    $(passwis).text(str);
}

/**
 * 计算护甲等级
 */
calArmorClass = function () {
    const bonus = $(".Dexterity").find(".Modifier");;
    const ac = $(".ArmorClass");
    // 没有护甲,TODO
    armor = 10
    str = armor + Number($(bonus).text());
    $(ac).text(str);
}
