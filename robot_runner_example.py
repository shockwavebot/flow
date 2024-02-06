from robot.api import TestSuite
from robot.api import ResultWriter
from robot.conf.settings import RobotSettings

if __name__ == '__main__':
    options = {
        "output": "./results.xml",
        "log": "./log.html",
        "report": "./report.html",
        "loglevel": "TRACE"
    }
    settings = RobotSettings(options)

    # Create a test suite
    suite = TestSuite('ExampleSuite')

    # Create a test
    test = suite.tests.create('ExampleTest', doc='An example test case.')

    # Add keywords (these can be your custom keywords or built-in keywords)
    test.body.create_keyword('Log', args=['Just an example log message'])
    test.body.create_keyword('Evaluate', args=['1+1'], assign=['${result} ='])

    # Run the test suite
    result = suite.run(settings=settings)

    # Output xml and log files (optional)
    ResultWriter("results.xml").write_results(
        settings=settings.get_rebot_settings())
