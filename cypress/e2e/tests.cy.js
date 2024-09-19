const BASE_URL = 'http://localhost:5502';

beforeEach(() => {
    cy.visit(BASE_URL);
});

describe('length tests', () => {
    beforeEach(() => {
        cy.get('#menuLength').click();
        cy.get('#txtLength').clear();
    });

    it('test that 1500 centimetres is 590.55 inches', () => {
        cy.get('#txtLength').type('1500').debug();
        cy.get('#radMetric').check();
        cy.get('section#sectionLength input[type=submit]').click();
        cy.get('section#sectionLength > div').should('have.text', '1500 centimeters is 590.55 inches');
    });

    it('test that 590.55 inches is 1500 centimetres', () => {
        cy.get('#txtLength').type('590.55');
        cy.get('#radImperial').check();
        cy.get('section#sectionLength input[type=submit]').click();
        cy.get('section#sectionLength > div').should('have.text', '590.55 inches is 1500 centimeters');
    });
});

describe('temperature tests', () => {
    const temperatureConversions = [
        {'From': 'C', 'To': 'C', 'TempFrom': 30, 'TempTo': 30},        
        {'From': 'C', 'To': 'F', 'TempFrom': 30, 'TempTo': 86},        
        {'From': 'C', 'To': 'K', 'TempFrom': 30, 'TempTo': 303.15},
        {'From': 'F', 'To': 'C', 'TempFrom': 30, 'TempTo': -1.11},        
        {'From': 'F', 'To': 'F', 'TempFrom': 30, 'TempTo': 30},        
        {'From': 'F', 'To': 'K', 'TempFrom': 30, 'TempTo': 272.04},
        {'From': 'K', 'To': 'C', 'TempFrom': 30, 'TempTo': -243.15},        
        {'From': 'K', 'To': 'F', 'TempFrom': 30, 'TempTo': -443},        
        {'From': 'K', 'To': 'K', 'TempFrom': 30, 'TempTo': 30}
    ];

    beforeEach(() => {
        cy.get('#menuTemperature').click();
        cy.get('#txtTemperature').clear();
    });

    temperatureConversions.forEach((conversion) => {
        it(`test that ${conversion.TempFrom}º${conversion.From} is ${conversion.TempTo}º${conversion.To}`, () => {
            cy.get('#txtTemperature').type(conversion.TempFrom);
            cy.get('#lstFrom').select(conversion.From);
            cy.get('#lstTo').select(conversion.To);
            cy.get('section#sectionTemperature input[type=submit]').click();
            cy.get('section#sectionTemperature > div').should('have.text', `${conversion.TempFrom} °${conversion.From} is ${conversion.TempTo} °${conversion.To}`);
        });
    });
});

describe('currency tests', () => {
    it('test that a conversion from NOK to USD returns a number', () => {
        cy.get('#menuCurrency').click();
        cy.get('#txtCurrency').clear();
        cy.get('#txtCurrency').type('120');
        cy.get('#cmbFrom').select('NOK');
        cy.get('#cmbTo').select('USD');
        cy.get('section#sectionCurrency input[type=submit]').click();
        cy.get('section#sectionCurrency > div').contains('120 NOK is ').contains('USD');
    });
});

describe('grade tests', () => {
    const DK = 'Denmark';
    const US = 'USA';
    const gradeConversions = [
        {'From': DK, 'To': US, 'GradeFrom': '12', 'GradeTo': 'A+'},
        {'From': DK, 'To': US, 'GradeFrom': '10', 'GradeTo': 'A'},
        {'From': DK, 'To': US, 'GradeFrom': '7', 'GradeTo': 'B'},
        {'From': DK, 'To': US, 'GradeFrom': '4', 'GradeTo': 'C'},
        {'From': DK, 'To': US, 'GradeFrom': '02', 'GradeTo': 'D'},
        {'From': DK, 'To': US, 'GradeFrom': '00', 'GradeTo': 'F'},
        {'From': DK, 'To': US, 'GradeFrom': '-3', 'GradeTo': 'F'},
        {'From': US, 'To': DK, 'GradeFrom': 'A+', 'GradeTo': '12'},
        {'From': US, 'To': DK, 'GradeFrom': 'A', 'GradeTo': '10'},
        {'From': US, 'To': DK, 'GradeFrom': 'B', 'GradeTo': '7'},
        {'From': US, 'To': DK, 'GradeFrom': 'C', 'GradeTo': '4'},
        {'From': US, 'To': DK, 'GradeFrom': 'D', 'GradeTo': '02'},
        {'From': US, 'To': DK, 'GradeFrom': 'F', 'GradeTo': '00'},
    ];

    beforeEach(() => {
        cy.get('#menuGrading').click();
    });

    gradeConversions.forEach(conversion => {
        it(`test that ${conversion.GradeFrom} in ${conversion.From} is ${conversion.GradeTo} in ${conversion.To}`, () => {
            cy.get(`#rad${conversion.From}`).check();
            cy.get('#cmbGrade').select(conversion.GradeFrom);
            cy.get('section#sectionGrading input[type=submit]').click();
            cy.get('section#sectionGrading > div').should('have.text', `${conversion.GradeFrom} in ${conversion.From} is ${conversion.GradeTo} in ${conversion.To}`);
        });
    });
});