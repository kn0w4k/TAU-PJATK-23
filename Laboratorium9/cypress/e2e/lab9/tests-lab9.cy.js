describe('test saucedemo page', () => {
  beforeEach(() => {
    cy.visit('https://example.cypress.io')
  })

  it('check if page loaded', () => {
    cy.get('.navbar-brand').should('have.text', "cypress.io")
  })

  it('commands list should display 17 items', () => {
    cy.get('[data-toggle="dropdown"]').click()
    cy.get('.dropdown-menu li').should('have.length', 17)
  })

  it('click eighth position in dropdown list', () => {
    cy.get('[data-toggle="dropdown"]').click()
    cy.get('.dropdown-menu').children('li').contains('Assertions').click()
  })

  it('click cy.location()', () => {
    cy.get('[data-toggle="dropdown"]').click()
    cy.get('.dropdown-menu').children('li').contains('Location').click()
    cy.get('#location a').click()
  })

  it('go to utilities and back to homepage', () => {
    cy.get('.navbar-nav').children('li').contains('Utilities').click(1)
    cy.get('.navbar-header').children('a').click()
  })

})