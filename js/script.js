import { baseAPIUrl } from './info.js';

//  Navigation menu

const menuOptions = document.querySelectorAll('nav > ul > li');
menuOptions.forEach(menuOption => {
    menuOption.addEventListener('click', function() {
        const menuOptions_ = document.querySelectorAll('nav > ul > li');
        menuOptions_.forEach(option => {
            option.classList.remove('selected');            
            document.querySelector('#section' + option.id.substring(4)).classList.remove('visible');
        });
        this.classList.add('selected');                       
    
        const currentSection = document.querySelector('#section' + this.id.substring(4));
        currentSection.classList.add('visible');
        console.log(currentSection);
        currentSection.querySelector('input[type="text"]').focus();
    });
});    

//  Length

document.querySelector('#sectionLength > form').addEventListener('submit', function(e) {
    e.preventDefault();
    const measure = e.target.txtLength.val;
    const system = document.querySelector('[name="radLengthSystem"]:checked').val;
    
    fetch(baseAPIUrl, {
        method: 'POST',
        data: {
            'conversion': 'length',
            'measure': measure,
            'system': system
        }
    })
    .then(response => response.json())
    .then((data) => {
        const text = measure + (system === 'M' ? ' centimeters' : ' inches') + ' is ' + data + (system === 'M' ? ' inches' : ' centimeters');

        document.querySelector('#sectionLength > div').innerText = text;
    });
});

//  Temperature

document.querySelector('#sectionTemperature > form').addEventListener('submit', function(e) {
    e.preventDefault();
    const measure = e.target.txtTemperature.val;
    const from = e.target.lstFrom.val;
    const to = e.target.lstTo.val;

    fetch(baseAPIUrl, {
        method: 'POST',
        data: {
            'conversion': 'temperature',
            'measure': measure,
            'originScale': from,
            'destinationScale': to
        }
    })
    .then(response => response.json())
    .then((data) => {
        const text = `${measure} &deg;${from} is ${data} &deg;${to}`;

        document.querySelector('#sectionTemperature > div').innerHTML = text;
    });
});

//  Currency

fetch(baseAPIUrl, {
    method: 'POST',
    data: {
        'conversion': 'currency',
        'action': 'getCurrencyList'
    }
})
.then(response => response.json())
.then((data) => {
    let currencyOptions = '';
    for (const [key, value] of Object.entries(data)) {
        currencyOptions += `
            <option value="${value[0]}">${value[0]} - ${value[1]}</option>
        `;
    }
    document.querySelector('#cmbFrom').innerHTML = currencyOptions;
    document.querySelector('#cmbTo').innerHTML = currencyOptions;
    // Default values
    document.querySelector('#cmbFrom > option[value="DKK"]').selected = true;
    document.querySelector('#cmbTo > option[value="EUR"]').selected = true;
});

document.querySelector('#sectionCurrency > form').addEventListener('submit', function(e) {
    e.preventDefault();
    const measure = e.target.txtCurrency.val;
    const from = e.target.cmbFrom.val;
    const to = e.target.cmbTo.val;

    fetch(baseAPIUrl, {
        method: 'POST',
        data: {
            'conversion': 'currency',
            'action': 'convert',
            'measure': measure,
            'baseCurrency': from,
            'destinationCurrency': to
        }    
    })
    .then(response = response.json())
    .then((data) => {
        const text = `${measure} ${from} is ${data} ${to}`;

        document.querySelector('#sectionCurrency > div').innerText = text;
    });
});

//  Grading population

document.querySelector('[name="radGradingSystem"]').addEventListener('change', () => {
    if (document.querySelector('[name="radGradingSystem"]:checked').val === 'Denmark') {
        document.querySelector('#cmbGrade').innerHTML = `
            <option value="12" selected>12</option>
            <option value="10">10</option>
            <option value="7">7</option>
            <option value="4">4</option>
            <option value="02">02</option>
            <option value="00">00</option>
            <option value="-3">-3</option>
        `;
    } else {
        document.querySelector('#cmbGrade').innerHTML = `
            <option value="A+" selected>A+</option>
            <option value="A">A</option>
            <option value="B">B</option>
            <option value="C">C</option>
            <option value="D">D</option>
            <option value="F">F</option>
        `;
    }
});

//  Grading

document.querySelector('#sectionGrading > form').addEventListener('submit', function(e) {
    e.preventDefault();
    const measure = e.target.cmbGrade.val;
    const country = document.querySelector('[name="radGradingSystem"]:checked').val;

    fetch(baseAPIUrl, {
        method: 'POST',
        data: {
            'conversion': 'grading',
            'measure': measure,
            'country': country
        }
    })
    .then(response => response.json())
    .then((data) => {
        let text = `${measure} in ${country} is ${data} in `;
        text += (country === 'Denmark' ? 'USA' : 'Denmark');

        document.querySelector('#sectionGrading > div').innerText = text;
    });
});

document.querySelector('nav > ul > li#menuLength').click();
document.querySelector('[name="radGradingSystem"]').dispatchEvent(new Event('change'));