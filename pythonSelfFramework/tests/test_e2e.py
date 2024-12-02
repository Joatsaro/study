from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_2e2(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card items")
        cards = checkOutPage.getCardTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        checkOutPage.checkoutShop().click()
        confirmPage = checkOutPage.checkoutItems()
        log.info("Entering country name as ind")
        confirmPage.deliveryLocation().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.indiaElement().click()
        confirmPage.agreeTerms().click()
        confirmPage.purchaseButton().click()
        success_text = confirmPage.endText().text
        log.info("Text received from application is: "+success_text)

        assert "Success! Tha$nk you" in success_text
