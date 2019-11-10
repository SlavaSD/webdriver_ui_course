import unittest
from random import randint
from selenium.webdriver.common.by import By
from fixtures.base import POMAdminLoginTestCase
from pages.new_report_page import NewReportPage
from pages.pim_page import PIMPage
from pages.report_run_page import ReportRunPage
from pages.reports_page import ReportsPage
from steps.common import is_element_present

class ReportTestCase(POMAdminLoginTestCase):
    def setUp(self):
        super(ReportTestCase, self).setUp()
        self.pim = PIMPage(self.driver)
        self.reports = ReportsPage(self.driver)
        self.new_report = NewReportPage(self.driver)
        self.report_run = ReportRunPage(self.driver)

    def test_create_report(self):
        report_name = "Rprt" + str(randint(1, 99))
        self.reports.goto_page()
        self.reports.add()
        self.new_report.set_name(report_name)
        self.new_report.select_selection_criteria("Job Title")
        self.new_report.select_display_field_groups("Personal")
        self.new_report.enable_display_fields()
        self.new_report.save()
        self.report_name = report_name
        self.reports.search(report_name)
        self.assertTrue(is_element_present(self.driver, By.XPATH, "//td[text()='{0}']".format(report_name)))
        self.reports.run(report_name)
        report_header = self.report_run.get_report_header()
        self.assertEqual('Report Name : {0}'.format(report_name), report_header)
        print ('Report Name : {0}'.format(report_name), report_header)

    def tearDown(self):
        if self.report_name:
            self.pim.goto_page()
            self.pim.goto_reports()
            self.reports.search(self.report_name)
            self.reports.delete_report(self.report_name)
        super(ReportTestCase, self).tearDown()

if __name__ == '__main__':
    unittest.main()
